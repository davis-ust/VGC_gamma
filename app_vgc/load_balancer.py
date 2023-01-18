from app_vgc import BotoManager, recursive_process


def get_load_balancer():
    print('getting get_load_balancer...')
    lb_list = []

    elb_classic = BotoManager.boto_session.client('elb')
    elb_application = BotoManager.boto_session.client('elbv2')

    lb_classic_lst = elb_classic.describe_load_balancers()
    lb_lst = elb_application.describe_load_balancers()

    lb_classic_dict = {'lb_classic': lb_classic_lst}
    lb_dict = {'lb_lst': lb_lst}
    lb_list.append(lb_classic_dict)
    lb_list.append(lb_dict)

    return lb_list


def get_load_balancer_pd():
    print('processing get_load_balancer_pd...')
    loadBalancer_list = []
    lb_data = get_load_balancer()

    for i in lb_data:
        for key, values in i.items():
            if key == 'lb_lst':
                lb_app = values['LoadBalancers']
                for ilbl in lb_app:
                    Name = {'Name': ilbl['LoadBalancerName']}
                    DNSName = {'DNS Name': ilbl['DNSName']}
                    Name.update(DNSName)
                    stateCode = {'State': ilbl['State']['Code']}
                    Name.update(stateCode)
                    VPCID = {'VPC ID': ilbl['VpcId']}
                    Name.update(VPCID)
                    zone = []
                    for iaz in ilbl['AvailabilityZones']:
                        zone.append(iaz['ZoneName'])
                    zone_dict = {'Availability Zones': zone}
                    Name.update(zone_dict)
                    Type = {'Type': ilbl['Type']}
                    Name.update(Type)
                    CreatedTime = {'Created At': ilbl['CreatedTime']}
                    Name.update(CreatedTime)
                    loadBalancer_list.append(Name)

            elif key == 'lb_classic':
                lb_classic = values['LoadBalancerDescriptions']
                for ilbl in lb_classic:
                    Name2 = {'Name': ilbl['LoadBalancerName']}
                    DNSName = {'DNS Name': ilbl['DNSName']}
                    Name2.update(DNSName)
                    VPCID = {'VPC ID': ilbl['VPCId']}
                    Name2.update(VPCID)
                    zone = []
                    for iaz in ilbl['AvailabilityZones']:
                        zone.append(iaz)
                    zone_dict = {'Availability Zones': zone}
                    Name2.update(zone_dict)
                    Type = {'Type': "Classic"}
                    Name2.update(Type)
                    CreatedTime = {'Created At': ilbl['CreatedTime']}
                    Name2.update(CreatedTime)
                    loadBalancer_list.append(Name2)

    loadBalancer_list = recursive_process(loadBalancer_list)
    return loadBalancer_list


if __name__ == "__main__":
    result = get_load_balancer_pd()
    print(result)
