## Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
## SPDX-License-Identifier: MIT-0

import datetime
import json
import boto3
from faker import Faker

# Modify to match your source stream name
SOURCE_STREAM_NAME = "us-east-1-stream"


fake = Faker()

def get_data():
    return {
        'name': fake.name(),
        'event_time': datetime.datetime.now().isoformat(),
        'city': fake.city()
    }

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")

if __name__ =='__main__':
    my_kinesis_client = boto3.client('kinesis')
    generate(SOURCE_STREAM_NAME, my_kinesis_client)