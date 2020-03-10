# creates presigned URL using s3 key
# uploads media files to VoiceBase API
# -*- coding: utf-8 -*-

import csv
import json
import os
import boto3
import boto3.session
from botocore.client import Config
from VoiceBaseClient import VoiceBaseClient

AWS_SERVER_PUBLIC_KEY = ''
AWS_SERVER_SECRET_KEY = ''

s3 = boto3.client('s3', aws_access_key_id=AWS_SERVER_PUBLIC_KEY,
					 aws_secret_access_key=AWS_SERVER_SECRET_KEY,
					 region_name='', config=Config(signature_version='s3v4'))

client = VoiceBaseClient(token = '')
media = client.media()

counter = 0
# configuration file for upload 
def generate_configuration():

  return json.dumps({
	  "speechModel": {
	  "language": "en-US"
  		}
  	}
	)
def post2VB(listfile,resfile):
	with open(listfile, 'r') as list_file:
		list_reader = csv.DictReader(list_file, delimiter = ',')
		with open(resfile, 'a') as results_file:
			results_writer = csv.writer(
			results_file, delimiter = ',', quotechar = '"'
			)
			results_writer.writerow(['fileURL','key', 'mediaId','status'])
			for row in list_reader:
				key = row['s3key'].rstrip()
				filename = row['file']
				fileURL = s3.generate_presigned_url(
				ClientMethod='get_object',
				Params={
		
				'Bucket': '',
				'Key': key
				},
				ExpiresIn=604800
				)
				response = media.post(
					fileURL,None, None,configuration = generate_configuration(), metadata = None
					)
				if response['status'] !='accepted':
					media_id = 0
					status = 'error'
				else: 
					media_id = response['mediaId']
					status = response['status']	
				results_writer.writerow([fileURL, key, media_id, status])

post2VB('list.csv','res.csv')
