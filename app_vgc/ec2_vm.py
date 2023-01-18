from app_vgc import BotoManager, recursive_process


def _get_ec2_boto_data():
    print('getting _get_ec2_boto_data...')
    inst_list = []
    ec2 = BotoManager.boto_session.client('ec2')
    instance_details = ec2.describe_instances()
    for instance in instance_details['Reservations']:
        for inst in instance['Instances']:
            instID = {'InstanceId': inst['InstanceId']}
            instance_id = inst['InstanceId']
            if 'Platform' in inst.keys():
                instID.update({'Platform OS': inst['Platform']})
            instID.update({'VM Name': inst['KeyName']})
            instID.update({'InstanceType': inst['InstanceType']})
            instID.update({'Availability Zone': inst['Placement']['AvailabilityZone']})
            if 'PublicIpAddress' in inst.keys():
                instID.update({'Public IP': inst['PublicIpAddress']})
            instID.update({'Subnet ID': inst['SubnetId']})
            instID.update({'VPC ID': inst['VpcId']})
            # for ipub in inst['NetworkInterfaces']:
            #     if 'Association' in ipub.keys():
            #         instID.update({'Public IP':ipub['Association']['PublicIp']})
            instID.update({'OwnerId': instance['OwnerId']})
            instID.update({'Instances': instance['Instances']})
            instID.update({'Root Device Name': inst['RootDeviceName']})
            instID.update({'Root Device Type': inst['RootDeviceType']})
            root_device_type = inst['RootDeviceType']
            if root_device_type == 'ebs':
                instID.update({'Root Volume ID': inst['BlockDeviceMappings'][0]['Ebs']['VolumeId']})
                root_vol_id = inst['BlockDeviceMappings'][0]['Ebs']['VolumeId']
                root_volume_id = inst['BlockDeviceMappings'][0]['Ebs']['VolumeId']
                instID.update({'Root Device Size in GB': ec2.describe_volumes(VolumeIds=[root_volume_id], DryRun=False)['Volumes'][0]['Size']})
                for volume_list in ec2.describe_volumes()['Volumes']:
                    for attachment_list in volume_list['Attachments']:
                        if attachment_list['InstanceId'] == instance_id and attachment_list['VolumeId'] != root_vol_id:
                            instID.update({'Additional Data Disk IDs': attachment_list['VolumeId']})
                            additional_disk_id = attachment_list['VolumeId']
                            additional_disk_volume = ec2.describe_volumes(VolumeIds=[additional_disk_id])
                            additional_disk_name = additional_disk_volume['Volumes'][0]['Attachments'][0]['Device']
                            additional_disk_size = additional_disk_volume['Volumes'][0]['Size']
                            additional_disk_az = additional_disk_volume['Volumes'][0]['AvailabilityZone']
                            instID.update({'Additional Data Device Name': additional_disk_name})
                            instID.update({'Additional Data Disk Size': additional_disk_size})
                            instID.update({'Additional Disk Availability Zone': additional_disk_az})

            for sg_details in inst['SecurityGroups']:
                instID.update({'Security Groups': sg_details['GroupName']})
                instID.update({'Security Group ID': sg_details['GroupId']})
            instID.update({'CPU Cores': inst['CpuOptions']['CoreCount']})
            instID.update({'Threads per core': inst['CpuOptions']['ThreadsPerCore']})
            if 'IamInstanceProfile' in inst.keys():
                instID.update({'Custom Permissions': inst['IamInstanceProfile']})
            bkp = BotoManager.boto_session.client('backup')
            for bkp_plan_list in bkp.list_backup_plans()['BackupPlansList']:
                bkp_plan_id = bkp_plan_list['BackupPlanId']
                for selection_list in bkp.list_backup_selections(BackupPlanId=bkp_plan_id)['BackupSelectionsList']:
                    selection_id = selection_list['SelectionId']
                    bkp_instance_list = bkp.get_backup_selection(BackupPlanId=bkp_plan_id, SelectionId=selection_id)['BackupSelection']['Resources']
                    for arn in bkp_instance_list:
                        if '/' not in arn:
                            continue

                        id = arn.split('/')[1]
                        if id == instance_id:
                            bkp_plan = bkp.get_backup_plan(BackupPlanId=bkp_plan_id)
                            instID.update({'Backup Plan Name': bkp_plan['BackupPlan']['BackupPlanName']})
                            instID.update({'Backup Retention': bkp_plan['BackupPlan']['Rules'][0]['Lifecycle']['DeleteAfterDays']})
                            instID.update({'Backup Rule Name': bkp_plan['BackupPlan']['Rules'][0]['RuleName']})
                            instID.update({'Backup Target Vault': bkp_plan['BackupPlan']['Rules'][0]['TargetBackupVaultName']})
                        inst_list.append(instID)
                        return inst_list


def get_ec2_df():
    print('processing get_ec2_df...')
    ec2_vm_list = _get_ec2_boto_data()
    vms_ec2_lst = []
    for ec2 in ec2_vm_list:
        owner_id = {'owner_id': ec2['OwnerId']}
        for i_ec2 in ec2['Instances']:
            for i_t in i_ec2['Tags']:
                owner_id.update({'Name': i_t['Value']})
            owner_id.update({'AmiLaunch Index': i_ec2['AmiLaunchIndex']})
            owner_id.update({'Image Id': i_ec2['ImageId']})
            owner_id.update({'Instance Id': i_ec2['InstanceId']})
            owner_id.update({'Instance Type': i_ec2['InstanceType']})
            owner_id.update({'Key Name': i_ec2['KeyName']})
            owner_id.update({'LaunchTime': i_ec2['LaunchTime']})
            owner_id.update({'State': i_ec2['Monitoring']['State']})
            owner_id.update({'AvailabilityZone': i_ec2['Placement']['AvailabilityZone']})
            owner_id.update({'Tenancy': i_ec2['Placement']['Tenancy']})
            owner_id.update({'PrivateDnsName': i_ec2['PrivateDnsName']})
            owner_id.update({'PrivateIpAddress': i_ec2['PrivateIpAddress']})
            if 'PublicIpAddress' in i_ec2.keys():
                owner_id.update({'PublicIpAddress': i_ec2['PublicIpAddress']})
            owner_id.update({'SubnetId': i_ec2['SubnetId']})
            owner_id.update({'VpcId': i_ec2['VpcId']})
            owner_id.update({'Architecture': i_ec2['Architecture']})

            owner_id.update({'Hypervisor': i_ec2['Hypervisor']})
            owner_id.update({'Platform': i_ec2['PlatformDetails']})
            owner_id.update({'RootDeviceName': i_ec2['RootDeviceName']})
            owner_id.update({'RootDeviceType': i_ec2['RootDeviceType']})
        owner_id.update({'Root Volume ID': ec2['Root Volume ID']})
        owner_id.update({'Root Device Size in GB': ec2.get('Root Device Size in GB') or '--'})
        owner_id.update({'Additional Data Disk IDs': ec2.get('Additional Data Disk IDs') or '--'})
        owner_id.update({'Additional Data Device Name': ec2.get('Additional Data Device Name') or '--'})
        owner_id.update({'Additional Data Disk Size': ec2.get('Additional Data Disk Size') or '--'})
        owner_id.update({'CPU Core': ec2['CPU Cores']})
        owner_id.update({'CPU ThreadsPerCore': ec2['Threads per core']})
        owner_id.update({'SecurityGroups-name': ec2['Security Groups']})
        owner_id.update({'SecurityGroups-id': ec2['Security Group ID']})
        owner_id.update({'Backup Plan Name': ec2.get('Backup Plan Name') or '--'})
        owner_id.update({'Backup Retention': ec2.get('Backup Retention') or '--'})
        owner_id.update({'Custom Permissions - Arn': ec2.get('Custom Permissions', {}).get('Arn') or '--'})
        owner_id.update({'Custom Permissions - Id': ec2.get('Custom Permissions', {}).get('Id') or '--'})

        vms_ec2_lst.append(owner_id)

    vms_ec2_lst = recursive_process(vms_ec2_lst)
    return vms_ec2_lst
