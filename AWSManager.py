import boto3
import uuid
import glob


class AWSManager:
    def __init__(self):
        self.s3 = boto3.resource('s3')

    def bucketGen(self, name):
        return ''.join([name, str(uuid.uuid4())])

    def listBucket(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)

    def upload(self, bucketName, fileName):
        try:
            with open(fileName, 'r') as f:
                data = f.read()
                self.s3.Bucket(bucketName).put_object(Key=fileName, Body=data)
        except Exception as e:
            print(e)
        else:
            print("File uploaded")
