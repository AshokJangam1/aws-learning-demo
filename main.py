import boto3

def read_single_file(bucket_name, file_key):
    
    s3 = boto3.client('s3')

    print(f"\n📄 Reading file: {file_key}")

  
    file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)

    
    content = file_obj['Body'].read().decode('utf-8', errors='ignore')

    print("\n------- File Content ------\n")
    print(content)
    print("\n------------------------")


bucket = "taxi-data-s3-storage"
file_key = "taxi_zone_lookup.csv"  

read_single_file(bucket, file_key)
