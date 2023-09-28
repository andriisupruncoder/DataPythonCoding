import boto3

ec2 = boto3.client('ec2')
paginator = ec2.get_paginator('describe_instances')

count = 0
for page in paginator.paginate():
    for reservation in page['Reservations']:
        count += len(reservation['Instances'])

print(count)
