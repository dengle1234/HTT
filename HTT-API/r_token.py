import requests
import time
import hashlib


def token(APIKey, APISecret, url):
    timestamp = int(time.time())
    APISign = 'APIKey=' + APIKey + '&APISecret=' + APISecret + '&Timestamp=' + str(timestamp)
    print(APISign)
    md = hashlib.md5(APISign.encode())
    md5_APISign = md.hexdigest()
    token_url = url + '/api/Token?APIKey={0}&Timestamp={1}&APISign={2}'.format(APIKey, timestamp, md5_APISign)
    print(token_url)
    r = requests.get(token_url)
    htt_json = r.json()
    tk = htt_json['Data']['Token']
    return tk
