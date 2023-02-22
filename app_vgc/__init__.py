import datetime
import boto3
from dotenv import dotenv_values

persistent_key_id = None
persistent_access_key = None
persistent_region = None

env_values = dotenv_values(".env")


def recursive_process(inp):
    # add conditions to check in other iterables (eg: set, tuple, etc..) if necessary
    if isinstance(inp, list):
        inp = [recursive_process(item) for item in inp]
    elif isinstance(inp, dict):
        inp = {key: recursive_process(value) for key, value in inp.items()}

    elif isinstance(inp, datetime.datetime):
        inp = inp.replace(tzinfo=None)

    return inp


class BotoManager:
    boto_key_id = "AKIAXUJZERGG4ZB2XJNX"
    boto_access_key = "JwdnIZ33ZzWDALMDiHcO28fQ76W4Q0mJkZRuD2q/"
    boto_key_region = 'eu-west-1'
    boto_session = None

    @classmethod
    def set_boto_session(cls):
        if cls.boto_key_id and cls.boto_access_key:
            cls.boto_session = boto3.Session(
                aws_access_key_id=cls.boto_key_id,
                aws_secret_access_key=cls.boto_access_key,
                region_name=cls.boto_key_region
            )
        else:
            cls.boto_session = boto3.Session(region_name=cls.boto_key_region)

        return cls.boto_session

