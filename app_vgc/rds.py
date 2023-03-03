from app_vgc import BotoManager
import json
import boto3


def get_rds_df(region):
    print('processing get_rds_df...')
    rds = region.client('rds')
    dbtype_file = 'app_vgc/db_instance_types.json'
    with open(dbtype_file, 'r') as json_file:
        db_types_json = json.load(json_file)
    set_db = ()
    lst_db_key = []
    for db_class in db_types_json:
        s = list(db_class.keys())
        sd_key = s[0]
        lst_db_key.append(sd_key)
        set_db = set(lst_db_key)

    dynamo_db = []
    for db_details in rds.describe_db_instances()['DBInstances']:
        DB_Name = {'DB Name': db_details['DBInstanceIdentifier']}
        DB_Name.update({'Instance Type': db_details['DBInstanceClass']})
        DB_Inst = db_details['DBInstanceClass']
        vcpu_mem = {}
        if DB_Inst in set_db:
            for ddb in db_types_json:
                for key, val in ddb.items():
                    if DB_Inst == val['Model']:
                        VCPU = val['vCPU']
                        memory = val['Memory (GiB)']
                        vcpu_mem.update({'vCPU': VCPU, 'Memory in GB': memory})
        DB_Name.update(vcpu_mem)

        DB_Name.update({'Engine': db_details['Engine']})
        DB_Name.update({'DB Status': db_details['DBInstanceStatus']})
        DB_Name.update({'Admin User': db_details['MasterUsername']})
        DB_Name.update({'End Point': db_details['Endpoint']['Address']})
        DB_Name.update({'Storage Amount': db_details['AllocatedStorage']})
        DB_Name.update({'Storage Type': db_details['StorageType']})
        for sg in db_details['VpcSecurityGroups']:
            DB_Name.update({'VPC Security Groupd ID': sg['VpcSecurityGroupId']})

        DB_Name.update({'Availability Zone': db_details['AvailabilityZone']})
        DB_Name.update({'DB Subnet Name': db_details['DBSubnetGroup']['DBSubnetGroupName']})
        DB_Name.update({'VPC ID': db_details['DBSubnetGroup']['VpcId']})
        dbtype = db_details['DBInstanceClass']

        # for subnet_info in db_details['DBSubnetGroup']['Subnets']:
        # print("Subnet ID:: ", subnet_info['SubnetIdentifier'])
        # print("Subnet Availability Zone:: ", subnet_info['SubnetAvailabilityZone']['Name'])
        # print("Subnet Status:: ", subnet_info['SubnetStatus'])

        DB_Name.update({'Prefered Maintenance Window': db_details['PreferredMaintenanceWindow']})
        DB_Name.update({'LatestRestorableTime': str(db_details.get('LatestRestorableTime'))})
        DB_Name.update({'MultiAZ': db_details['MultiAZ']})
        DB_Name.update({'EngineVersion': db_details['EngineVersion']})
        DB_Name.update({'AutoMinorVersionUpgrade': db_details['AutoMinorVersionUpgrade']})
        DB_Name.update({'LicenseModel': db_details['LicenseModel']})
        DB_Name.update({'PubliclyAccessible': db_details['PubliclyAccessible']})
        DB_Name.update({'StorageType': db_details['StorageType']})
        DB_Name.update({'StorageEncrypted': db_details['StorageEncrypted']})
        DB_Name.update({'KmsKeyId': db_details.get('KmsKeyId')})
        DB_Name.update({'MonitoringInterval': db_details['MonitoringInterval']})
        DB_Name.update({'DBInstanceArn': db_details['DBInstanceArn']})
        DB_Name.update({'IAMDatabaseAuthenticationEnabled': db_details['IAMDatabaseAuthenticationEnabled']})
        DB_Name.update({'DeletionProtection': db_details['DeletionProtection']})
        dynamo_db.append(DB_Name)

    return dynamo_db


if __name__ == "__main__":
    result = get_rds_df(boto3.Session(region_name='us-east-1'))
    print(result)
