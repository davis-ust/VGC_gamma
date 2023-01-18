from app_vgc import BotoManager


def _get_dynamodb():
    print('getting _get_dynamodb...')
    result_ddb = []
    dynamodb = BotoManager.boto_session.client('dynamodb')
    response = dynamodb.list_tables()
    table_list = response['TableNames']
    for table in table_list:
        table_info = dynamodb.describe_table(TableName=table)
        result_ddb.append(table_info['Table'])

    return result_ddb


def get_dynamo_db_df():
    print('processing get_dynamo_db_df...')
    dynamo_db_data = _get_dynamodb()
    db_table_lst = []
    for iidb in dynamo_db_data:
        #print(iidb['ProvisionedThroughput'])
        TableName = {'Table Name': iidb['TableName']}
        for ikey in iidb['KeySchema']:
            TableName.update({'Key Name': ikey['AttributeName']})
            TableName.update({'Key Table': ikey['KeyType']})
        TableName.update({'Table Status': iidb['TableStatus']})
        TableName.update({'Creation DateTime': str(iidb['CreationDateTime'])})
        TableName.update({'LastDecrease DateTime': str(iidb['ProvisionedThroughput'].get('LastDecreaseDateTime'))})
        TableName.update({'ReadCapacityUnits': iidb['ProvisionedThroughput'].get('ReadCapacityUnits')})
        TableName.update({'WriteCapacityUnits': iidb['ProvisionedThroughput'].get('WriteCapacityUnits')})
        TableName.update({'TableSizeBytes': iidb['TableSizeBytes']})
        TableName.update({'ItemCount': iidb['ItemCount']})
        TableName.update({'TableArn': iidb['TableArn']})
        TableName.update({'TableId': iidb['TableId']})
        db_table_lst.append(TableName)
    #print(db_table_lst)

    return db_table_lst
