from pathlib import Path
from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
from threading import Thread
import time
from app_vgc import BotoManager, app_main
from tools import handle_json_file


app = Flask(__name__, static_url_path='/static')
app.secret_key = "RANDOMSTRING"
SAVED_DATA_FOLDER = "saved_data"
SAVED_DATA_SCANS_JSON = SAVED_DATA_FOLDER + r"/scans.json"


def timestamp_check():
    loaded_json = handle_json_file(SAVED_DATA_SCANS_JSON)

    if not (len(loaded_json)):
        handle_get_latest_data()
        loaded_json = handle_json_file(SAVED_DATA_SCANS_JSON)
        assert len(loaded_json)

    processing_data = list(loaded_json.values())[-1]
    filename = list(loaded_json.keys())[-1]
    ts = filename.replace('aws_resource_inventory-', '')
    ts = ts.replace('.xlsx', '')
    ts = ts.split('--')
    ts = ts[0] + ' ' + ts[1].replace('-', ':')
    return ts, processing_data, filename


def run(interval):
    print("thread running")
    if not BotoManager.boto_session:
        print('No boto session, thread exiting!')
        return

    while interval:
        print("thread at interval", interval, "seconds")
        try:
            handle_thread_data()
            print("threaded scan completed")
        except Exception as e:
            print('threaded scan interrupted due to error: ' + str(e))
        time.sleep(interval)


@app.route('/')
def handle_root():
    if 'key_id' not in session:
        return redirect(url_for('handle_login'))

    return redirect(url_for('handle_dashboard'))


@app.route('/dashboard')
def handle_dashboard():
    if 'region' not in session:
        return redirect(url_for('handle_login'))
    if not BotoManager.boto_session:
        BotoManager.boto_key_region = session['region']
        BotoManager.set_boto_session()

    ts, processing_data, filename = timestamp_check()
    return render_template('admin.html', processing_data=processing_data, ts=ts, filename=filename)


@app.route('/get_latest_ts')
def get_latest_timestamp():
    ts, _, _ = timestamp_check()
    return ts


@app.route('/get_latest_data')
def handle_get_latest_data():
    if 'region' not in session:
        return redirect(url_for('handle_login'))
    if not BotoManager.boto_session:
        BotoManager.boto_key_region = session['region']
        BotoManager.set_boto_session()

    handle_thread_data()

    return redirect(url_for('handle_dashboard'))


def handle_thread_data():
    print('fetching boto3 for new values...')
    rel_path, processing_data = app_main.main()
    file_name = Path(rel_path).name
    print('=========> scan COMPLETE')

    loaded_json = handle_json_file(SAVED_DATA_SCANS_JSON)
    loaded_json[file_name] = processing_data
    handle_json_file(SAVED_DATA_SCANS_JSON, loaded_json)


@app.route('/downloads/<filename>')
def handle_downloads(filename):
    return send_from_directory(
        directory=app_main.download_folder_path,
        path=filename,
        as_attachment=True
    )


@app.route('/login', methods=['GET', 'POST'])
def handle_login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == 'POST':
        session['key_id'] = request.form.get('key_id')
        session['access_key'] = request.form.get('access_key')
        session['region'] = request.form.get('region')
        BotoManager.boto_key_id = session['key_id']
        BotoManager.boto_access_key = session['access_key']
        BotoManager.boto_key_region = session['region']
        BotoManager.set_boto_session()
        return redirect(url_for('handle_dashboard'))


@app.route('/logout')
def handle_logout():
    session.pop('key_id')
    session.pop('access_key')
    session.pop('region')
    return redirect(url_for('handle_root'))


if __name__ == '__main__':
    s = Thread(target=run, args=(120,))
    s.start()
    app.run(host='0.0.0.0', port=7000, debug=True)


