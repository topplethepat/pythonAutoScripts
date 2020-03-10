# batch download for media stored in s3 bucket

import boto3
import botocore
import csv
import json
import requests
import os
from boto.s3.connection import S3Connection

access_key = ''
secret_key = ''
bucket_name = ''


conn = S3Connection(access_key,secret_key)
prefix = 'my_prefix/'
bucket = conn.get_bucket(bucket_name)
path = 'path/to/media_folder'

for key in bucket.list(prefix = prefix):
    if key.name.endswith('/'):
        if not os.path.exists('./'+key.name):
            os.makedirs('./'+key.name)
    else:
    	if key.name.startswith('company/'):
    		print key.name
    		res = key.get_contents_to_filename('./'+key.name[-34:]) #truncates last part of key to make a neat filename
    
                            







