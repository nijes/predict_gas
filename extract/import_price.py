import json
import requests

url = requests.get("http://ecos.bok.or.kr/api/StatisticSearch/0GK5VA3EB3WSUUSD9C2Q/json/kr/1/100000/401Y015/M/198801/202202")
text = url.text

data = json.loads(text)

with open("/home/big/predict_gas/raw_data/import_price/import_price1.json", "w") as json_file: json.dump(data, json_file, ensure_ascii=False)



url = requests.get("http://ecos.bok.or.kr/api/StatisticSearch/0GK5VA3EB3WSUUSD9C2Q/json/kr/1/100000/401Y015/M/202203/202206")
text = url.text

data = json.loads(text)

with open("/home/big/predict_gas/raw_data/import_price/import_price2.json", "w") as json_file: json.dump(data, json_file, ensure_ascii=False)
