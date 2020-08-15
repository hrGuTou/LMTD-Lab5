import boto3
import uuid


class AWSManager:
    def __init__(self):
        self.s3 = boto3.resource('s3')

    def bucketGen(self, name):
        return ''.join([name, str(uuid.uuid4())])

    def listBucket(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)

    def listBucketFile(self, bucketName):
        bucket = self.s3.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key)

    def upload(self, bucketName, fileName):
        try:
            with open(fileName, 'r') as f:
                data = f.read()
                self.s3.Bucket(bucketName).put_object(Key=fileName, Body=data)
        except Exception as e:
            print(e)
        else:
            print("File uploaded")

    def download(self,bucketName, fileName):
        try:
            self.s3.Bucket(bucketName).download_file(fileName, "downloaded.html")
        except Exception as e:
            print(e)




#DEBUG CODE

if __name__ == "__main__":
    app = AWSManager()
    app.listBucket()
    app.listBucketFile(input("Bucket Name: "))
    app.download("lmtd-class", input("File Name: "))
