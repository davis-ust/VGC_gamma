from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from app_vgc import app_main
from tools import handle_json_file
from automate_region_scan import ScheduleManager

app = Flask(__name__, static_url_path='/static')
app.secret_key = "RANDOMSTRING"
SAVED_DATA_FOLDER = "saved_data"
SAVED_DATA_SCANS_JSON = SAVED_DATA_FOLDER + r"/scans.json"
SAVED_DATA_Automate_JSON = SAVED_DATA_FOLDER + r"/scheduler.json"
schedule_man = ScheduleManager()


def validate_region(region=None):
    region_list = [
        'ap-south-1', 'eu-north-1', 'eu-west-3', 'eu-west-2', 'eu-west-1',
        'ap-northeast-3', 'ap-northeast-2', 'ap-northeast-1', 'ca-central-1',
        'sa-east-1', 'ap-southeast-1', 'ap-southeast-2',
        'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
    return region if region in region_list else 'us-east-1'


def get_latest_data(region):
    """
    Fetching New data for a Region
    """
    print(f'fetching new details for----> {region}')
    rel_path, processing_data = app_main.main(region)
    print(f'=========> scan COMPLETE for--> {region}')
    loaded_json = handle_json_file(SAVED_DATA_SCANS_JSON)
    loaded_json[region] = processing_data
    handle_json_file(SAVED_DATA_SCANS_JSON, loaded_json)
    return processing_data


def get_data(region):
    """
    Getting existing Region from JSON
    :param- region
    :return: json data of region
    """
    loaded_json = handle_json_file(SAVED_DATA_SCANS_JSON)
    if region in loaded_json.keys():
        print("Loaded Region Data from JSON FIle")
        data = loaded_json[region]
        return data
    print("New Region scan Started")
    return get_latest_data(region)


def get_scheduler_data():
    """
    Stores JSON for Scheduled regions with interval and units
    """
    data = handle_json_file(SAVED_DATA_Automate_JSON)
    if data:
        print('The file has data', data)
    else:
        print('The file is empty')
        data = {}
    return data


@app.route('/')
@app.route('/dashboard/us-east-1')
@app.route('/dashboard/<region>')
def handle_new_dashboard(region='us-east-1'):
    """
    Main function which handles the dashboard, region validation,
    checks region previously scanned or not.Else scans for the new region
    """
    region = request.view_args.get('region', 'us-east-1')
    region_check = validate_region(region)
    data = get_data(region_check)
    automated_data = get_scheduler_data()
    return render_template('admin.html', processing_data=data, ts=data['timestamp'], filename=data['filename'],
                           reg=region, scheduler_data=automated_data)


@app.route('/get_latest_data/<region>')
def handle_get_latest_data(region):
    """
    Refresh scan for the selected region
    :param- region
    :return: latest scanned data for the region
    """
    print("get latest data Block entered")
    region = validate_region(region)
    get_latest_data(region)
    return redirect(url_for('handle_new_dashboard', region=region))


@app.route('/downloads/<filename>')
def handle_downloads(filename):
    return send_from_directory(
        directory=app_main.download_folder_path,
        path=filename,
        as_attachment=True
    )


@app.route('/automate_refresh', methods=['POST', 'GET'])
def add_automated_regions():
    """
    Adds regions to automate scan at given interval.
    """
    req_data = request.form.to_dict()
    print(req_data, "add regions data")
    try:
        interval = int(req_data.get('interval'))
        print(interval)
        print(type(interval))
    except Exception as e:
        print(e)
        return 'error converting interval to integer'

    schedule_man.add_job(
        region=req_data.get('region'),
        interval=interval,
        interval_units=req_data.get('units'),
    )

    return redirect(url_for('handle_new_dashboard', region=req_data.get('region')))


@app.route('/delete_region', methods=['POST'])
def delete_automated_region():
    """
    Delete regions from automated scan
    """
    req_data = request.form.to_dict()
    print(req_data, 'data to delete')

    try:
        interval = int(req_data.get('time-interval'))
        print(interval)
    except Exception as e:
        print(e)
        return 'error converting interval to integer'
    schedule_man.remove_job(
        region=req_data.get('region_name'),
        interval=interval,
        interval_units=req_data.get('interval-units')
    )
    return redirect(url_for('handle_new_dashboard', region=req_data.get('region_name')))


@app.errorhandler(404)
def handle_custom_error(error):
    return render_template('404error.html', error=error), 404


@app.errorhandler(500)
def handle_custom_error(error):
    return render_template('500error.html', error=error), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)
