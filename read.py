import boto3

def read_all_files(bucket_name, prefix=""):

    s3 = boto3.client('s3')

    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    if 'Contents' not in response:
        print("No files found.")
        return

    for obj in response['Contents']:
        key = obj['Key']
        print(f"\n Reading file: {key}")

        file_obj = s3.get_object(Bucket=bucket_name, Key=key)

        content = file_obj['Body'].read().decode('utf-8', errors='ignore')

        print(content)
        print("-" * 50)
bucket = "demo-s3-file-storage"
prefix_path = ""

read_all_files(bucket, prefix_path)
