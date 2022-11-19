from redis.cluster import RedisCluster as Redis
import json

def lambda_handler(event, context):    
  client = Redis(
    host='monitoring.fowglj.clustercfg.memorydb.sa-east-1.amazonaws.com',
    port=6379,
  )

  service_name = event['queryStringParameters']['name']
  data = client.get(service_name)
  if data:
    data = json.loads(client.get(service_name).decode('utf-8'))
    data['name'] = service_name
  else:
    data = '{}'

  return {
    'statusCode': 200,
    'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    },
    'body': json.dumps(data),
    "isBase64Encoded": False
  }