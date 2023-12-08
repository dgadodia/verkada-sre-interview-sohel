import json
import requests
from collections import defaultdict


URL = "http://localhost:8080/logs"
text = requests.get(URL).text
output = json.loads(text)
data = output["logs"]
counts = defaultdict(int)
for item in data:
    if "event" in item.keys():
        counts[item["event"]] += 1

print(counts)
