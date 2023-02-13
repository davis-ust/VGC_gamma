from app_vgc import BotoManager


def _get_igw():
    print('getting _get_igw...')
    ec2 = BotoManager.boto_session.client('ec2')
    igw_details = ec2.describe_internet_gateways()
    return igw_details


def get_internet_gateway():
    print('processing get_internet_gateway...')
    igw_lst = []
    igw_data = _get_igw()
    for iint in igw_data['InternetGateways']:
        # print(iint)
        intGat = {'Internet Gateway Id': iint['InternetGatewayId']}
        intGat['Name'] = '-'
        for ita in iint['Tags']:
            if ita['Key'] == 'Name':
                intGat.update({'Name': ita['Value']} or '-')
        for iat in iint['Attachments']:
            intGat.update(iat)
        igw_lst.append(intGat)
    # print(igw_lst)

    return igw_lst
