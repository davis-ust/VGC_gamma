import boto3, json

from app_vgc import BotoManager, recursive_process


def _get_ec2_boto_data(region):
    print('getting _get_ec2_boto_data...')
    output_list = []
    ec2 = region.client('ec2')
    instance_details = ec2.describe_instances()
    for instance in instance_details['Reservations']:
        for instance_item in instance['Instances']:
            instance_id = instance_item['InstanceId']
            instance_detail = {
                'InstanceId': instance_id,
                'VM Name': instance_item['KeyName'],
                'InstanceType': instance_item['InstanceType'],
                'Availability Zone': instance_item['Placement']['AvailabilityZone'],
                'Subnet ID': instance_item['SubnetId'],
                'VPC ID': instance_item['VpcId'],
                'OwnerId': instance['OwnerId'],
                'Instances': instance['Instances'],
                'Root Device Name': instance_item['RootDeviceName'],
                'Root Device Type': instance_item['RootDeviceType'],
                'CPU Cores': instance_item['CpuOptions']['CoreCount'],
                'Threads per core': instance_item['CpuOptions']['ThreadsPerCore']
            }

            if 'Platform' in instance_item.keys():
                instance_detail['Platform OS'] = instance_item['Platform']
            if 'PublicIpAddress' in instance_item.keys():
                instance_detail['Public IP'] = instance_item['PublicIpAddress']
            if 'IamInstanceProfile' in instance_item.keys():
                instance_detail['Custom Permissions'] = instance_item['IamInstanceProfile']

            for sg_details in instance_item['SecurityGroups']:
                instance_detail.update({'Security Groups': sg_details['GroupName']})
                instance_detail.update({'Security Group ID': sg_details['GroupId']})

            # for ipub in inst['NetworkInterfaces']:
            #     if 'Association' in ipub.keys():
            #         instID.update({'Public IP':ipub['Association']['PublicIp']})

            root_device_type = instance_item['RootDeviceType']
            if root_device_type == 'ebs':
                root_volume_id = instance_item['BlockDeviceMappings'][0]['Ebs']['VolumeId']
                instance_detail['Root Volume ID'] = root_volume_id
                instance_detail['Root Device Size in GB'] = ec2.describe_volumes(
                    VolumeIds=[root_volume_id],
                    DryRun=False
                )['Volumes'][0]['Size']

                for volume_list in ec2.describe_volumes()['Volumes']:
                    for attachment_detail in volume_list['Attachments']:
                        additional_disk_id = attachment_detail['VolumeId']
                        if attachment_detail['InstanceId'] == instance_id and additional_disk_id != root_volume_id:
                            # todo: the following details of this loop might supposed to be appended to a list
                            #  to get multiple additional disks data
                            instance_detail.update({'Additional Data Disk IDs': additional_disk_id})
                            additional_disk_volume = ec2.describe_volumes(VolumeIds=[additional_disk_id])
                            instance_detail['Additional Data Device Name'] = \
                            additional_disk_volume['Volumes'][0]['Attachments'][0]['Device']
                            instance_detail['Additional Data Disk Size'] = additional_disk_volume['Volumes'][0]['Size']
                            instance_detail['Additional Disk Availability Zone'] = additional_disk_volume['Volumes'][0][
                                'AvailabilityZone']

            bkp = region.client('backup')
            for bkp_plan_list in bkp.list_backup_plans()['BackupPlansList']:
                bkp_plan_id = bkp_plan_list['BackupPlanId']
                for selection_list in bkp.list_backup_selections(BackupPlanId=bkp_plan_id)['BackupSelectionsList']:
                    selection_id = selection_list['SelectionId']
                    bkp_instance_list = \
                    bkp.get_backup_selection(BackupPlanId=bkp_plan_id, SelectionId=selection_id)['BackupSelection'][
                        'Resources']
                    for arn in bkp_instance_list:
                        if '/' not in arn:
                            continue

                        if instance_id == arn.split('/')[1]:
                            bkp_plan = bkp.get_backup_plan(BackupPlanId=bkp_plan_id)
                            instance_detail.update({'Backup Plan Name': bkp_plan['BackupPlan']['BackupPlanName']})
                            instance_detail.update({'Backup Retention': bkp_plan['BackupPlan']['Rules'][0]['Lifecycle'][
                                'DeleteAfterDays']})
                            instance_detail.update({'Backup Rule Name': bkp_plan['BackupPlan']['Rules'][0]['RuleName']})
                            instance_detail.update(
                                {'Backup Target Vault': bkp_plan['BackupPlan']['Rules'][0]['TargetBackupVaultName']})

            output_list.append(instance_detail)
    return output_list


def get_ec2_df(region):
    print('processing get_ec2_df...')
    ec2_vm_list = _get_ec2_boto_data(region)
    vms_ec2_lst = []
    for ec2 in ec2_vm_list:
        owner_id = {'owner_id': ec2['OwnerId']}
        for i_ec2 in ec2['Instances']:
            owner_id['Name'] = ''
            for i_t in i_ec2['Tags']:
                if i_t['Key'] == 'Name':
                    owner_id['Name'] = i_t['Value']
                    break

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
            owner_id.update({'PublicDnsName': i_ec2.get('PublicDnsName') or '--'})
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


if __name__ == '__main__':
    region = 'us-east-1'
    session = boto3.Session(region_name=region, aws_access_key_id='AKIAXUJZERGG4ZB2XJNX', aws_secret_access_key='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')
    print(get_ec2_df(session))

