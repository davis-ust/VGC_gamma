def get_network_acl_df(network_acl):
    print('processing get_network_acl_df...')
    network_acl_lst = []
    for inet in network_acl['NetworkAcls']:
        NetworkAclId = {'Network ACL ID': inet['NetworkAclId']}
        for tn in inet['Tags']:
            NetworkAclId.update({'Name': tn['Value']})
        NetworkAclId.update({'VPC ID': inet['VpcId']})
        NetworkAclId.update({'Default': inet['IsDefault']})
        a = inet['Entries']
        outbound = len([d for d in a if d.get('Egress') == True])
        inbound = len([d for d in a if d.get('Egress') == False])
        NetworkAclId.update({'Inbound rules count': inbound})
        NetworkAclId.update({'Outbound rules count': outbound})
        asso_list = inet['Associations']
        key_artists = [k['SubnetId'] for k in asso_list if k.get('SubnetId')]
        if len(key_artists) == 1:
            subnet_associate = [k['SubnetId'] for k in asso_list if k.get('SubnetId')]
            NetworkAclId.update({'Associated with': subnet_associate})
        NetworkAclId.update({'Associated with': len(key_artists)})
        network_acl_lst.append(NetworkAclId)
    #print(network_acl_lst)

    return network_acl_lst
