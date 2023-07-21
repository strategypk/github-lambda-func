import json
def lambda_handler(event, context):
    data=json.dumps(event)
    downloadlink = "https://finance.yahoo.com/quote/TSLA"
    return {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': json.dumps(downloadlink)}

print('Recommended Stock of the Day July 22 : TSLA')