from app_vgc import BotoManager
import datetime


def _get_sqs_boto_data():
    print('getting _get_sqs_boto_data...')
    sqs = BotoManager.boto_session.client('sqs')
    # sqs_details = sqs.list_queues()
    sqs_list = []
    for queue_url in sqs.list_queues()['QueueUrls']:
        sqs_name = queue_url.split('/')[-1]
        name = {'Name': sqs_name}
        Created_Timestamp = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['CreatedTimestamp'])
        epoch_time = int(Created_Timestamp['Attributes']['CreatedTimestamp'])
        Created_Time = datetime.datetime.fromtimestamp(epoch_time)
        name.update({'Created':str(Created_Time)})
        name.update({'Type': 'FIFO' if sqs_name[-4:] == "fifo" else 'Standard'})
        SSE_Status = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['SqsManagedSseEnabled'])['Attributes']['SqsManagedSseEnabled']
        kms_dict = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['KmsMasterKeyId'])
        kms = list(kms_dict.values())[0].keys()

        if SSE_Status == 'true':
            name.update({'Encryption': 'SSE-SQS'})
        elif 'KmsMasterKeyId' in kms:
            name.update({'Encryption': 'SSE-KMS'})
        else:
            name.update({'Encryption': 'disabled'})
        sqs_list.append(name)

    return sqs_list


def get_sqs_df():
    print('processing get_sqs_df...')
    # SQS Dataset preparation
    sqs_data = _get_sqs_boto_data()
    sqs_lst = []
    for i_sqs in sqs_data:
        sqs_lst.append(i_sqs)

    return sqs_lst
