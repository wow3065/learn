#!/bin/env python
# -*- coding: utf-8 -*-
import boto3
import sys
from pprint import pprint

class EC2():
  def __init__(self, status):
    self.instancestate = status
    session = boto3.session.Session(profile_name="**********")
    self.client = session.client('ec2', region_name="**********")

  def describe_instances(self):
    # need to add retry logic
    response = self.client.describe_instances(Filters=[
      {
        'Name': 'instance-state-name',
        'Values': self.instancestate
      }],
    )

    ec2_lists = {}
    for d in response['Reservations']:
      for ec2 in d['Instances']:
        private_ip = ec2['PrivateIpAddress']
        instance_type = ec2['InstanceType']
        for tag in ec2['Tags']:
          if tag['Key'] == 'Name':
            ec2_lists[tag['Value']] = [private_ip,instance_type]
    pprint(ec2_lists)
    return ec2_lists

def main():
  if len(sys.argv) > 1 :
    ec2 = EC2(sys.argv[1:])
    ec2.describe_instances()
  else:
    ec2 = EC2(['running'])
    ec2.describe_instances()

if __name__ == '__main__':
  main()
