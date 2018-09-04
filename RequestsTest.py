import requests
import pandas as pd
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
print(resp)
data = resp.json()
data[0]['title']
# print(data)
issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues)