import boto3

def create_s3_bucket(bucket_name, region=None):
    s3 = boto3.client('s3', region_name=region) if region else boto3.client('s3')
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print(f'S3 Bucket Created: {bucket_name}')
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

if __name__ == "__main__":
    # Example usage
    create_s3_bucket('your-unique-bucket-name', region='us-west-2')
