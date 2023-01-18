from app_vgc import BotoManager


def _get_transfer_service_boto_data():
    print('getting _get_transfer_service_boto_data...')
    transfer_service = BotoManager.boto_session.client('transfer')
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
        #print(transfer_service.describe_server(ServerId=ServerID))
        transfer_list.append(transfer_service.describe_server(ServerId=ServerID))
    #print(transfer_list)

    return transfer_list


def get_transfer_service_df():
    print('processing get_transfer_service_df...')
    # Transfer Service Data Prepration
    transfer_service = _get_transfer_service_boto_data()
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
