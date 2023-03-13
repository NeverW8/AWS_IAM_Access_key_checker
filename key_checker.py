import boto3
from datetime import datetime, timezone

iam = boto3.client('iam')

users = iam.list_users()['Users']

for user in users:
    username = user['UserName']


    access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']


    for access_key in access_keys:
        access_key_id = access_key['AccessKeyId']


        creation_date = access_key['CreateDate']


        age = datetime.now(timezone.utc) - creation_date


        last_used = iam.get_access_key_last_used(AccessKeyId=access_key_id)


        if 'LastUsedDate' not in last_used['AccessKeyLastUsed']:
            used = 'Never Used'
        else:
            used = 'Used on {}'.format(last_used['AccessKeyLastUsed']['LastUsedDate'])


        print('Access key ID: {}, Age: {}, Status: {}'.format(access_key_id, age, used))
