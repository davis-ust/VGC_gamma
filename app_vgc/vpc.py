# from app_vgc import BotoManager, NewBotoManager
import ipaddress, boto3

# manager = NewBotoManager()
# session = manager.set_boto_session()


def get_vpc_list(region):
    print('getting get_vpc_list...')
    ec2 = region.client('ec2')
    vpc_details = ec2.describe_vpcs()
    list_output = list(vpc_details['Vpcs'])
    # print(list_output)
    # vpc_list = '\n\n'.join([str(i) for i in list_output])

    return list_output


def get_vpc_pd(tup_args):
    region, route_table, net_vpc = tup_args
    print('processing get_vpc_pd...')
    vpc_list = get_vpc_list(region)

    vpc_detail_set = []
    for i_vpc in vpc_list:
        vpcID = {'VPC ID': i_vpc['VpcId']}
        vpcID['Name'] = '-'
        if 'Tags' in i_vpc.keys():
            for i_tags in i_vpc['Tags']:
                if i_tags['Key'] == 'Name':
                    Name = {'Name': i_tags['Value'] or '-'}
                    vpcID.update(Name)
                    break

        State = {'State': i_vpc['State']}
        vpcID.update(State)
        IPv4CIDR = {'IPv4 CIDR': i_vpc['CidrBlock']}
        vpcID.update(IPv4CIDR)
        n = ipaddress.IPv4Network(i_vpc['CidrBlock'])
        first, last = n[1], n[-2]
        HostIp = {'Host Min': str(first), 'Host Max': str(last)}
        vpcID.update(HostIp)
        DhcpOptionsId = {'DHCP options set': i_vpc['DhcpOptionsId']}
        vpcID.update(DhcpOptionsId)
        Tenancy = {'Tenancy': i_vpc['InstanceTenancy']}
        vpcID.update(Tenancy)
        OwnerId = {'Owner ID': i_vpc['OwnerId']}
        vpcID.update(OwnerId)
        vpc_detail_set.append(vpcID)
    # print(vpc_detail_set)

    # join vpc with route table
    vpc_route = []
    innerJoined = vpc_detail_set.copy()
    for ind, s in enumerate(innerJoined):
        iek = route_table['RouteTables']
        for ieki in iek:
            if 'VpcId' in ieki.keys():
                if ieki['VpcId'] == s['VPC ID']:
                    RouteTableID = {'Main route table': ieki['RouteTableId']}
                    s.update(RouteTableID)
        vpc_route.append(s)
    # print(vpc_route)

    # join vpc with networkACL
    vpc_ACL_list = []
    innerJoinedACl = vpc_route.copy()
    for ind, s in enumerate(innerJoinedACl):
        for ie in net_vpc:
            if ie['vpcID'] == s['VPC ID']:
                s.update({'Main network ACL': ie['NetworkACL']})
        vpc_ACL_list.append(s)
    # print(vpc_ACL_list)

    return vpc_ACL_list


if __name__ == '__main__':
    session = boto3.Session(
        aws_access_key_id="AKIAXUJZERGG4ZB2XJNX",
        aws_secret_access_key="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",
        region_name='us-east-1'
    )
