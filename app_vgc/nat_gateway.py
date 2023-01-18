from app_vgc import BotoManager


def _get_aws_nat_gateway_data():
    print('getting _get_aws_nat_gateway_data...')
    ec2 = BotoManager.boto_session.client('ec2')
    nat_gw = ec2.describe_nat_gateways()
    return nat_gw


def get_nat_gateway_df():
    print('processing get_nat_gateway_df...')
    inat = _get_aws_nat_gateway_data()
    NAT_lst = []
    for inatd in inat['NatGateways']:
        natID = {'NAT gateway ID': inatd['NatGatewayId']}
        if len(inatd['Tags']) == 0:
            natID.update({'Name': ' '})
        for it in inatd['Tags']:
            natID.update({'Name': it['Value']})
        for iep in inatd['NatGatewayAddresses']:
            natID.update({
                'Elastic IP Address': iep['PublicIp'], 'Private IP address': iep['PrivateIp'],
                'Network interface ID': iep['NetworkInterfaceId']
            })
        natID.update({'VPC ID': inatd['VpcId'], 'Subnet ID': inatd['SubnetId']})
        NAT_lst.append(natID)
    # print(NAT_lst)

    return NAT_lst
