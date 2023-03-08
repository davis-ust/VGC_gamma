# from app_vgc import BotoManager, NewBotoManager
import boto3

# manager = NewBotoManager()
# session = manager.set_boto_session()


def _get_transfer_service_boto_data(region):
    print('getting _get_transfer_service_boto_data...')
    transfer_service = region.client('transfer')
    server_details = transfer_service.list_servers()
    response = server_details['Servers']
    transfer_list = []
    # print(response)
    # for ServerID in server_details['Servers'][0]['ServerId']:
    #  print(ServerID)
    #  print(transfer_service.describe_server(ServerId=ServerID))
    for item in response:
        # ServerID = response[0]['ServerId']
        # print(transfer_service.describe_server(ServerId = ServerID))
        ServerID = item['ServerId']
        # print(transfer_service.describe_server(ServerId=ServerID))
        transfer_list.append(transfer_service.describe_server(ServerId=ServerID))
    # print(transfer_list)

    return transfer_list


def get_transfer_service_df(region):
    print('processing get_transfer_service_df...')
    transfer_service = _get_transfer_service_boto_data(region)
    transfer_service_lst = []
    for itrans in transfer_service:
        server = itrans['Server']
        Arn = {'Arn': server['Arn']}
        for i_tag_a in server['Tags']:
            Arn.update({'Name': i_tag_a['Value']})
        Arn.update({'Domain': server['Domain']})
        Arn.update({'EndpointType': server['EndpointType']})
        Arn.update({'HostKeyFingerprint': server['HostKeyFingerprint']})
        Arn.update({'IdentityProviderType': server['IdentityProviderType']})
        Arn.update({'LoggingRole': server['LoggingRole']})
        Arn.update({'Protocols': server['Protocols']})
        Arn.update({'SecurityPolicyName': server['SecurityPolicyName']})
        Arn.update({'ServerId': server['ServerId']})
        Arn.update({'State': server['State']})
        Arn.update({'UserCount': server['UserCount']})
        transfer_service_lst.append(Arn)
    # print(transfer_service_lst)

    return transfer_service_lst


if __name__ == '__main__':
    session = boto3.Session(
        aws_access_key_id="AKIAXUJZERGG4ZB2XJNX",
        aws_secret_access_key="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",
        region_name='us-east-1'
    )
    val = get_transfer_service_df()
    print(val)

