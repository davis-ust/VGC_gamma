from app_vgc import BotoManager


# import json
# import boto3


def get_sns():
    # aws_access_key_id = "AKIAXUJZERGG4ZB2XJNX"
    # aws_secret_access_key = "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"
    # region_name = "us-east-1"
    print('processing get_sns...')
    #
    # session = boto3.Session(region_name=region_name, aws_access_key_id=aws_access_key_id,
    #                         aws_secret_access_key=aws_secret_access_key)
    #
    # client = session.client('sns')
    client = BotoManager.boto_session.client('sns')

    sns_list = []

    sns_det = client.list_subscriptions()
    # sns_demo = client.list_subscriptions()
    # print(sns_demo)
    for i in sns_det['Subscriptions']:
        sns_dict = {'SubscriptionArn': i['SubscriptionArn'],
                    'Owner': i['Owner'],
                    'Protocol': i['Protocol'],
                    'Endpoint': i['Endpoint'],
                    'TopicArn': i['TopicArn']
                    }
        sns_list.append(sns_dict)
    return sns_list


if __name__ == "__main__":
    result = get_sns()
    print(result)
