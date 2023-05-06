import requests
import pandas as pd

response = requests.get('https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv')

if response.status_code != 200:
    print(f'Etwas ist nicht okay wegen Status Code: {response.status_code}')
    exit()
else:
    content = response.content

print(content)

# df = pd.read_csv(content)
#
# df.describe()

