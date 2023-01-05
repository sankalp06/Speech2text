from Speech2txt import speech2text, determine_grade, conv_mp3_to_wav 
import json
import boto3

def handler(event, context):
    body = json.loads(event['body'])
    mp3_file_path = body['mp3S3location']
    transcript_file_path = body['transcriptS3location']
    s3 = boto3.resource('s3')
    bucket_name = body['sagemaker-sankalp']
    
    transcript = s3.Object(bucket_name, transcript_file_path).get()['Body'].read().decode('utf-8')
    s3.Bucket(bucket_name).download_file(mp3_file_path,'/tmp/essay.mp3')

    conv_mp3_to_wav(event['/tmp/essay.mp3'],event['/temp/wav_file'])

    res = speech2text(event['/temp/wav_file'],event['transcript'],student_name=event['student_name'])
    print(res)
    return {
        'statusCode': 200,
        'body': json.dumps(res),
        'headers': {'Content-Type': 'application/json'}
    }
