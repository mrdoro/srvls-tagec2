import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    userType = event['detail']['userIdentity']['type']

    if userType == 'IAMUser':
        user = event['detail']['userIdentity']['userName']
    elif userType == 'Root':
        user = "Root"
    elif userType == 'AssumedRole':
        user = event['detail']['userIdentity']['principalId']
        user = user.split(':',1)[1]
    else:
        user = 'N/A'

    items = event['detail']['responseElements']['instancesSet']['items']

    for item in items:
        instanceId = item['instanceId']

        ec2.create_tags(
            Resources=[instanceId],
            Tags=[{
                'Key': 'Creator',
                'Value': user
            }]
        )



    return 'OK'
