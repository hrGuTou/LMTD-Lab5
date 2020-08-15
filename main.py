from HtmlManager import HtmlManager
from AWSManager import AWSManager
import glob


def createHTML():
    html = HtmlManager(input("Input the title for html file: "))

    while True:
        choice = input("Enter 1 to add tag, q to save: ")

        if choice == "1":
            tag, word = input("Input tag and word follows by a space: ").split(' ')
            html.addTag(tag, word)
        elif choice == "q":
            html.saveHTML()
            break
        else:
            print("Invalid input")


def upload():
    s3 = AWSManager()
    s3.listBucket()
    bucketName = input("Enter your bucket name, press 'g' to create a new one: ")

    if bucketName == "g":
        bucketName = s3.bucketGen(input("Enter your name: "))

    files = glob.glob("*.html")
    for i, file in enumerate(files):
        print(i, " ", file)

    choice = input("Which file? Enter the number: ")

    s3.upload(bucketName=bucketName, fileName=files[int(choice)])


def showFiles():
    s3 = AWSManager()
    s3.listBucket()
    s3.listBucketFile(input("Enter bucket name: "))


if __name__ == "__main__":
    createHTML()
    upload()
    showFiles()
