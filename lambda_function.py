import json
def lambda_handler(event, context):
    data=json.dumps(event)
    downloadlink = "https://finance.yahoo.com/quote/MSFT"
    return {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': json.dumps(downloadlink)}

print('Recommended Stock of the Day July 21 sec : MSFT')
# downloadlink = "https://finance.yahoo.com/quote/TSLA"
# downloadlink = "https://finance.yahoo.com/quote/AMZN"
# downloadlink = "https://finance.yahoo.com/quote/MSFT"
# downloadlink = "https://finance.yahoo.com/quote/NFLX"
# downloadlink = "https://finance.yahoo.com/quote/NVDA"
# downloadlink = "https://finance.yahoo.com/quote/CRM"