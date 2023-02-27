# from app_vgc import BotoManager
# import json
import boto3


def get_s3():
    # aws_access_key_id = "AKIAXUJZERGG4ZB2XJNX"
    # aws_secret_access_key = "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"
    # region_name = "us-east-1"
    # print('processing get_s3...')
    # 
     # session = boto3.Session(region_name=region_name, aws_access_key_id=aws_access_key_id,
    #                         aws_secret_access_key=aws_secret_access_key)

    # s3_details = session.client('s3')
    boto_session = boto3.Session(region_name='us-east-1')
    s3_details = boto_session.client('s3')


    s3_list = []
    name_list = []

    s3_det = s3_details.list_buckets()
    # print(s3_det)
    for i in s3_det['Buckets']:
        s3_dict = {'Name': i['Name'],
                   'CreationDate': i['CreationDate']
                   }
        name_list.append(i['Name'])
        s3_list.append(s3_dict)
    print(name_list)
    print("################")

    s3_bitc_list = []
    for name in name_list:
        s3_bitc_det = s3_details.list_bucket_intelligent_tiering_configurations(Bucket=name)
        s3_bitc_list.append(s3_bitc_det)
    print(s3_bitc_list)
    # for i in s3_bitc_det['Buckets']:
    #     s3_bitc_dict = {'Name': i['Name'],
    #                     'CreationDate': i['CreationDate']
    #                      }
    #     s3_list.append(s3_bitc_dict)
    # print(s3_bitc_list)
    return s3_bitc_list


if __name__ == "__main__":
    result = get_s3()
    print(result)


