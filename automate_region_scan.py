import schedule, time

from tools import handle_json_file
from app_vgc import BotoManager, app_main
from threading import Thread


class ScheduleManager:
    saved_data_json_path = 'saved_data/scheduler.json'
    SAVED_DATA_SCANS_JSON = 'saved_data/scans.json'

    def __init__(self, scanner_func=None, skip_auto_run=False):
        self.scanner_func = self.get_latest_data
        self.skip_auto_run = skip_auto_run
        if scanner_func:
            self.set_scanner_func(scanner_func)

        if not self.skip_auto_run:
            Thread(target=self.schedule_watcher, daemon=True).start()

    def load_jobs_from_file(self):
        saved_data = handle_json_file(ScheduleManager.saved_data_json_path)
        for region, value in saved_data.items():
            self.add_job(
                region=region,
                interval=int(value['interval']),
                interval_units=value['interval_units'],
                is_internal_call=True
            )
        schedule.run_all(delay_seconds=1)

    def set_scanner_func(self, scanner_func):
        self.scanner_func = scanner_func
        self.load_jobs_from_file()

    @staticmethod
    def schedule_watcher():
        schedule.run_all(1)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def add_job(self, region, interval, interval_units, is_internal_call=False):
        schedule.clear(region)
        if interval_units == 'minutes':
            schedule.every(interval).minutes.do(self.scanner_func, region)
        elif interval_units == 'hours':
            schedule.every(interval).hours.do(self.scanner_func, region)
        else:
            print('SCHEDULER => unhandled interval units received: ' + str(interval_units))
        if not is_internal_call:
            saved_data = handle_json_file(self.saved_data_json_path)
            saved_data[region] = {
                'interval': interval,
                'interval_units': interval_units,
            }
            handle_json_file(self.saved_data_json_path, saved_data)

    def remove_job(self, region, interval, interval_units):
        filtered_jobs = [job for job in schedule.get_jobs()
                         if job.job_func.args[0] == region and job.interval == interval and job.unit == interval_units]

        for job in filtered_jobs:
            schedule.cancel_job(job)

        saved_data = handle_json_file(self.saved_data_json_path)
        if region in saved_data:
            del saved_data[region]
            handle_json_file(self.saved_data_json_path, saved_data)

    @staticmethod
    def get_jobs():
        all_jobs = schedule.get_jobs()
        jobs_output = [
            {
                "region": this_job.job_func.args[0],
                "time-interval": this_job.interval,
                "interval-units": this_job.unit
            }
            for this_job in all_jobs
        ]
        return jobs_output

    @staticmethod
    def get_latest_data(region):
        """
        Auto scan the  Region
        """
        print(f'Started scheduling for----> {region}')
        rel_path, processing_data = app_main.main(region)
        print(f'=========> Scheduled scan COMPLETE for--> {region}')
        loaded_json = handle_json_file(ScheduleManager.SAVED_DATA_SCANS_JSON)
        loaded_json[region] = processing_data
        handle_json_file(ScheduleManager.SAVED_DATA_SCANS_JSON, loaded_json)
