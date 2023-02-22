import threading
import pytz
import datetime
import pandas as pd
from pathlib import Path
from app_vgc import BotoManager, subnet, vpc, load_balancer, internet_gateway, sqs, nat_gateway, \
    transit_gateway, rds, dynamo_db, transfer_service, ec2_vm, network_acl, sns


download_folder_path = "generated_files"


def main():
    if not BotoManager.boto_session:
        BotoManager.set_boto_session()
    route_table = subnet.get_route_table()
    network_acl_data = subnet.get_nacl_aws_data()
    subnet_data, net_vpc = subnet.get_subnet_pd(route_table, network_acl_data)
    region = BotoManager.boto_key_region
    print("REGION", region)
    all_data_meta = (
        ('vpc_details', vpc.get_vpc_pd, (route_table, net_vpc)),
        ('load_balancer', load_balancer.get_load_balancer_pd, None),
        ('network_acl_details', network_acl.get_network_acl_df, network_acl_data),
        ('igw_details', internet_gateway.get_internet_gateway, None),
        ('sqs_details', sqs.get_sqs_df, None),
        ('NAT_details', nat_gateway.get_nat_gateway_df, None),
        ('tgw_details', transit_gateway.get_transit_gateway_df, None),
        ('rds_details', rds.get_rds_df, None),
        ('dynamodb_details', dynamo_db.get_dynamo_db_df, None),
        ('ts_details', transfer_service.get_transfer_service_df, None),
        ('ec2_details', ec2_vm.get_ec2_df, None),
        ('sns_details', sns.get_sns, None)
    )

    all_data = {'subnet_details': subnet_data}

    def general_thread(data_set_in_func):
        key, func, supports = data_set_in_func
        try:
            all_data[key] = func(supports) if supports else func()
        except Exception as e:
            print('error on ', key)
            print(e)

    all_threads = []
    for data_set in all_data_meta:
        t = threading.Thread(target=general_thread, args=(data_set,), daemon=True)
        t.start()
        all_threads.append(t)

    for all_thread in all_threads:
        all_thread.join()

    Path(download_folder_path).mkdir(exist_ok=True)
    tz = pytz.timezone('Asia/Kolkata')
    current_date = datetime.datetime.now(tz=tz).strftime("%Y-%m-%d--%H-%M-%S")
    excel_filename = region + current_date + ".xlsx"
    # print("Excel Filename", excel_filename)
    relative_path = fr"{download_folder_path}/aws_resource_inventory-{excel_filename}"
    print("Excel Filename", relative_path)
    with pd.ExcelWriter(relative_path) as writer:
        if 'subnet_details' in all_data:
            pd.DataFrame(data=all_data['subnet_details']).to_excel(writer, sheet_name="Subnet", index=False)
        if 'vpc_details' in all_data:
            pd.DataFrame(data=all_data['vpc_details']).to_excel(writer, sheet_name="VPC Details", index=False)
        if 'load_balancer' in all_data:
            pd.DataFrame(data=all_data['load_balancer']).to_excel(writer, sheet_name="Load Balancer", index=False)
        if 'network_acl_details' in all_data:
            pd.DataFrame(data=all_data['network_acl_details']).to_excel(writer, sheet_name="NACL", index=False)
        if ' in all_data' in all_data:
            pd.DataFrame(data=all_data['igw_details']).to_excel(writer, sheet_name="IGW", index=False)
        if 'sqs_details' in all_data:
            pd.DataFrame(data=all_data['sqs_details']).to_excel(writer, sheet_name="SQS", index=False)
        if 'NAT_details' in all_data:
            pd.DataFrame(data=all_data['NAT_details']).to_excel(writer, sheet_name="NAT Gateway", index=False)
        if 'tgw_details' in all_data:
            pd.DataFrame(data=all_data['tgw_details']).to_excel(writer, sheet_name="TGW", index=False)
        if 'rds_details' in all_data:
            pd.DataFrame(data=all_data['rds_details']).to_excel(writer, sheet_name="RDS", index=False)
        if 'dynamodb_details' in all_data:
            pd.DataFrame(data=all_data['dynamodb_details']).to_excel(writer, sheet_name="Dynamo DB", index=False)
        if 'ts_details' in all_data:
            pd.DataFrame(data=all_data['ts_details']).to_excel(writer, sheet_name="AWS Transfer Service", index=False)
        if 'ec2_details' in all_data:
            pd.DataFrame(data=all_data['ec2_details']).to_excel(writer, sheet_name="VMs", index=False),
        if 'sns_details' in all_data:
            pd.DataFrame(data=all_data['sns_details']).to_excel(writer, sheet_name="SNS", index=False)

    return relative_path, all_data


if __name__ == '__main__':
    main()
