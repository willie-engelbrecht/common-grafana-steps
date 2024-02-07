# example of usage grafana/loki api when you need push any log/message from your python scipt
import requests
import json
import time

# push msg log into grafana-loki
url = 'http://localhost:3100/loki/api/v1/push'
headers = {
    'Content-type': 'application/json',
    'X-Scope-OrgID': 'tenant-1'
}


payload = {
    'streams': [
    {
        'stream': {'foo': 'bar'},
        'values': [
            [   str(time.time_ns()), 'fizzbuzz'
            ]
        ]
    }
  ]
}

payload = json.dumps(payload)
print()
print(payload)

answer = requests.post(url, data=payload, headers=headers)
print("response code: " + str(answer))
