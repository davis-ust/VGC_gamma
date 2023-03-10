from app_vgc import BotoManager


def get_nacl_aws_data():
    print('getting get_nacl_aws_data...')
    ec2 = BotoManager.boto_session.client('ec2')
    nacl_details = ec2.describe_network_acls()
    return nacl_details


def get_route_table():
    print('getting get_route_table...')
    ec2 = BotoManager.boto_session.client('ec2')
    route_table_details = ec2.describe_route_tables()
    return route_table_details


def get_subnet_list():
    print('getting get_subnet_list...')
    ec2 = BotoManager.boto_session.client('ec2')
    subnet_details = ec2.describe_subnets()
    list_output = list(subnet_details['Subnets'])
    return list_output


def get_subnet_pd(route_table, network_acl):
    print('processing get_subnet_pd...')
    # network acl dataset
    # extract vpcID and subnetID along with NetworkACL_ID
    subnet_list = get_subnet_list()

    net_vpc = []
    sub_net_l = []
    for neta in network_acl['NetworkAcls']:
        NetworkACL = {'NetworkACL': neta['NetworkAclId']}
        VpcId = {'vpcID': neta['VpcId']}
        NetworkACL.update(VpcId)
        net_vpc.append(NetworkACL)
        asso = neta['Associations']
        for i_asso in asso:
            sub_acl = {'SubnetId': i_asso['SubnetId'], 'NetworkAclId': i_asso['NetworkAclId']}
            sub_net_l.append(sub_acl)
    #print(net_vpc)
    #print(sub_net_l)

    # Collect Route Table data

    # Collect subnet details
    # subnet_list = [{ sample subnet details }]
    # subnet data preparation
    subnet_detail_set = []
    for i_sub in subnet_list:
        # print(i_sub)
        SubnetId = {'Subnet ID': i_sub['SubnetId']}
        SubnetId['Name'] = '-'
        SubnetId['Environment'] = '-'
        if 'Tags' in i_sub.keys():
            for i_tag in i_sub['Tags']:
                if i_tag['Key'] == 'Name':
                    Name = {'Name': i_tag['Value'] or '-'}
                    SubnetId.update(Name)
                elif i_tag['Key'] == 'Environment':
                    Environment = {'Environment': i_tag['Value'] or '-'}
                    SubnetId.update(Environment)
                    break

        State = {'State': i_sub['State']}
        SubnetId.update(State)
        vpcID = {'VPC': i_sub['VpcId']}
        SubnetId.update(vpcID)
        ipV4CIDR = {'IPv4 CIDR': i_sub['CidrBlock']}
        SubnetId.update(ipV4CIDR)
        AvailabilityZone = {'Availability Zone': i_sub['AvailabilityZone']}
        SubnetId.update(AvailabilityZone)
        AvailabilityZoneId = {'Availability Zone ID': i_sub['AvailabilityZoneId']}
        SubnetId.update(AvailabilityZoneId)
        Networkbordergroup = {'Network border group': i_sub['AvailabilityZone'][:-1]}
        SubnetId.update(Networkbordergroup)
        # print(SubnetId)
        subnet_detail_set.append(SubnetId)
    #print(subnet_detail_set)

    # join subnet with routeTable
    subnet_route = []
    innerJoined = subnet_detail_set.copy()
    for ind, s in enumerate(innerJoined):
        iek = route_table['RouteTables']
        for ieki in iek:
            for ia in ieki['Associations']:
                if 'SubnetId' in ia.keys():
                    if ia['SubnetId'] == s['Subnet ID']:
                        RouteTableID = {'Route Table': ia['RouteTableId']}
                        s.update(RouteTableID)
        subnet_route.append(s)
    # print(subnet_route)

    # join subnet with network ACL
    subnet_ACL = []
    innerJoinedsubACl = subnet_route.copy()
    for ind, s in enumerate(innerJoinedsubACl):
        for ie in sub_net_l:
            if ie['SubnetId'] == s['Subnet ID']:
                s.update({'Network ACL': ie['NetworkAclId']})
        subnet_ACL.append(s)

    return subnet_ACL, net_vpc

