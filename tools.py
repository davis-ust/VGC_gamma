import json
from pathlib import Path


def handle_json_file(json_file_rel_path: str, write_data: dict = None):
    json_file_rel_path_obj = Path(json_file_rel_path)
    if not json_file_rel_path_obj.parent.exists():
        json_file_rel_path_obj.parent.mkdir()
    if not json_file_rel_path_obj.exists():
        json_file_rel_path_obj.write_text('{}')

    # lock_obj = cls.DEVICE_ID_LOCK if json_file_rel_path == cls.DEVICE_ID_JSON_FILE_PATH else cls.SUBNET_ID_LOCK
    # lock_obj.acquire()
    if write_data:  # writes to file if this variable has value and returns nothing
        # print('json write ', write_data)
        with open(json_file_rel_path, 'w') as f:
            json.dump(write_data, f, indent=4, default=str)
        # lock_obj.release()
    else:  # reads from file and returns json/dict()
        with open(json_file_rel_path) as f:
            data_json = json.load(f)
        # lock_obj.release()
        return data_json
