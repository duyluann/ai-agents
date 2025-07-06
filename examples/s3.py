import boto3

def create_s3_bucket(bucket_name, region=None):
    """
    Create an S3 bucket with optional region specification.
    
    Args:
        bucket_name (str): Name of the S3 bucket to create
        region (str, optional): AWS region for the bucket
    
    Raises:
        ValueError: If bucket_name is empty or invalid
    """
    if not bucket_name or not isinstance(bucket_name, str):
        raise ValueError("bucket_name must be a non-empty string")
    
    s3 = boto3.client('s3', region_name=region)
    try:
        if region and region != 'us-east-1':
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        else:
            s3.create_bucket(Bucket=bucket_name)
        print(f'S3 Bucket Created: {bucket_name}')
    except ClientError as e:
        print(f"Error creating S3 bucket: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise



if __name__ == "__main__":
    # Example usage
    import uuid
    unique_bucket_name = f'example-bucket-{uuid.uuid4().hex[:8]}'
    create_s3_bucket(unique_bucket_name, region='us-west-2')
