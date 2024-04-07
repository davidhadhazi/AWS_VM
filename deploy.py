import boto3
import sys

aws_access_key_id = str(sys.argv[1])
aws_secret_access_key = str(sys.argv[2])
region_name = 'eu-central-1'

ec2_client = boto3.client('ec2',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name)

instance_params = {
    'ImageId' : 'ami-0aeb27e6921bb826a',
    'InstanceType' : 't2.micro',
    'KeyName' : 'deploy',
    'MinCount' : 1,
    'MaxCount' : 1
}

response = ec2_client.run_instances(**instance_params)

instance_id = response['Instances'][0]['InstanceId']

ec2_client.get_waiter('instance_running').wait(InstanceIds=[instance_id])

print(f"Instance {instance_id} is now running.")