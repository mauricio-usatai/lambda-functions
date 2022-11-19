from redis.cluster import RedisCluster as Redis
import json

def lambda_handler(event, context):    
  client = Redis(
    host='monitoring.fowglj.clustercfg.memorydb.sa-east-1.amazonaws.com',
    port=6379,
  )

  service_name = event['name']
  if service_name == 'status':
    data = event['status']
  else:
    data = {
      'date': event['date'],
      'machine': event['machine'],
    }

  client.set(service_name, json.dumps(data))

  return json.dumps(data)