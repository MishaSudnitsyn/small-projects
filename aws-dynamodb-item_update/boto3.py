import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table_name')

response = table.update_item(
    Key={
        'ItemKeyID': 'ItemKeyName'
    },
    UpdateExpression='SET item_attribute_name.#new_field = :new_value, item_attribute_name2.#new_field = :new_value, item_attribute_name3.#new_field = :new_value',
    ExpressionAttributeNames={
        '#new_field': 'field_name'
    },
    ExpressionAttributeValues={
        ':new_value': 'field_value'
    }
)

print(response)
