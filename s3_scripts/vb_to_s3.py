# gets streaming URL for each file from VB, 
# uploads to s3 bucket as audio file

import csv
import smart_open
import boto3
import boto3.session
from botocore.client import Config
from VoiceBaseClient import VoiceBaseClient


access_key = ''
secret_key = ''
					
s3c = boto3.client('s3',
							aws_access_key_id=access_key,
							aws_secret_access_key=secret_key,region_name='',
							)


client = VoiceBaseClient(token = '')
media = client.media()

def s3_upload(listfile,resfile):

	with open(listfile, 'r') as list_file:
		list_reader = csv.DictReader(list_file, delimiter = ',')
		for row in list_reader:
			media_id = row['mediaId']
			external_id = row['externalId']
			with open(resfile, 'a') as results_file:
				file_is_empty = os.stat(resfile).st_size == 0
				results_writer = csv.writer(
				results_file, delimiter = ',', quotechar = '"'
				)
				if file_is_empty:
					results_writer.writerow(['fileURL','key', 'mediaId','externalId'])
				key = 'path/folder/' + external_id + '/' + external_id + '.flac'
				bucketname = ''
				# uses method from VoiceBaseClient.py to GET the media from VB API
				media_stream = media.get_item(media_id)
				stream_url = media_stream['streams'][0]['streamLocation']
				# uses smart_open module method to download file without saving it
				with smart_open.open(stream_url, 'rb',buffering=0) as fake_handle:
					print (fake_handle)
					s3c.put_object(Bucket=bucketname, Key=key, Body=fake_handle.read())

					results_writer.writerow([stream_url,key,media_id,external_id])

s3_upload('list.csv','res.csv')				
				