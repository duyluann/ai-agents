import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

# Create a new EC2 instance
def create_ec2_instance():
    try:
        instance = ec2.create_instances(
            ImageId='ami-0c55b159cbfafe1f0',  # Replace with your desired AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',  # Replace with your desired instance type
            KeyName='your-key-pair',  # Replace with your key pair name
            SecurityGroupIds=['sg-xxxxxxxx'],  # Replace with your security group ID
            SubnetId='subnet-xxxxxxxx'  # Replace with your subnet ID
        )
        print(f'EC2 Instance Created with ID: {instance[0].id}')
    except Exception as e:
        print(f"Error creating EC2 instance: {e}")

# Call the function
create_ec2_instance()
