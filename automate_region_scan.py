import schedule, time

from tools import handle_json_file
from app_vgc import BotoManager, app_main
from threading import Thread


class ScheduleManager:
    saved_data_json_path = 'saved_data/scheduler.json'

    def __init__(self, scanner_func=None, skip_auto_run=False):
        self.scanner_func = lambda x: None
        self.skip_auto_run = skip_auto_run
        if scanner_func:
            self.set_scanner_func(scanner_func)

        if not self.skip_auto_run:
            Thread(target=self.schedule_watcher, daemon=True).start()

    def load_saved_data(self, skip_auto_run_now=False):
        saved_data = handle_json_file(ScheduleManager.saved_data_json_path)
        for key, value in saved_data.items():
            print(saved_data)
            self.add_job(
                region=key,
                interval=int(value['interval']),
                interval_units=value['interval_units'],
                is_internal_call=True
            )
        if not skip_auto_run_now:
            def for_non_blocker():
                schedule.run_all(delay_seconds=1)

            Thread(target=for_non_blocker, daemon=True).start()

    def set_scanner_func(self, scanner_func):
        self.scanner_func = scanner_func
        self.load_saved_data(self.skip_auto_run)

    @staticmethod
    def schedule_watcher():
        schedule.run_all(1)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def add_job(self, region, interval, interval_units, is_internal_call=False):
        print(region)
        print("scheduler jobs", schedule.get_jobs())
        for this_job in schedule.get_jobs():
            if this_job.job_func.args[0] == region:
                schedule.cancel_job(this_job)
        # if scan_type == 'timeseries_scheduling':
        #     print("Scheduling Timeseries")
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
        filtered_jobs = [
            this_job
            for this_job in schedule.get_jobs()
            if
            this_job.job_func.args[0] == region and this_job.interval == interval and this_job.unit == interval_units
        ]
        for this_job in filtered_jobs:
            schedule.cancel_job(this_job)
        saved_data = handle_json_file(self.saved_data_json_path)
        if region in saved_data:
            saved_data.pop(region)
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

