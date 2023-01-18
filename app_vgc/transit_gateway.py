from app_vgc import BotoManager


def get_tgw():
    print('getting get_tgw...')
    tgw_list = []
    ec2 = BotoManager.boto_session.client('ec2')
    tgw_details = ec2.describe_transit_gateways()
    tgw_vpc_attachments = ec2.describe_transit_gateway_vpc_attachments()
    tgw_attachments = ec2.describe_transit_gateway_attachments()
    #print(tgw_details)
    #print(tgw_vpc_attachments)
    #print(tgw_attachments)
    # tgw_dict = {'TransitGateways': tgw_details,
    #             'TransitGatewayVpcAttachments': tgw_vpc_attachments,
    #             'TransitGatewayAttachments': tgw_attachments
    #             }
    tgw_list.append(tgw_details)
    tgw_list.append(tgw_vpc_attachments)
    tgw_list.append(tgw_attachments)
    return tgw_list


def get_transit_gateway_df():
    print('processing get_transit_gateway_df...')
    # Transit gateway data preparation
    transit_gate = get_tgw()
    transit_gate_list = []
    for itran in transit_gate:
        if 'TransitGatewayAttachments' in itran.keys():
            for itga in itran['TransitGatewayAttachments']:
                transitGateway = {'Transit gateway attachment ID': itga['TransitGatewayAttachmentId']}
                for itgs in itga['Tags']:
                    transitGateway.update({'Name': itgs['Value']})
                transitGateway.update({'Transit gateway ID': itga['TransitGatewayId']})
                transitGateway.update({'Resource type': itga['ResourceType']})
                transitGateway.update({'Resource ID': itga['ResourceId']})
                transitGateway.update({'State': itga['State']})
                transitGateway.update({'Association route table ID': itga['Association']['TransitGatewayRouteTableId']})
                transit_gate_list.append(transitGateway)

    return transit_gate_list
