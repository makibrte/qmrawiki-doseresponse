import requests
from bs4 import BeautifulSoup
import pandas as pd

# The target URL
url = 'https://qmrawiki.org/node/402'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find elements by HTML tags, attributes, or CSS class
    titles = soup.find_all('h1')
    for title in titles:
        print(title.get_text())
    tables_data = soup.find_all('table')
    
    for table_data in tables_data[3]:
        table_row_data = [row for row in table_data.get_text().split('\n') if row != '']
        if len(table_row_data):
            columns = table_row_data[1:5]
            experiment_data = []
            print(columns)
            i = 5
            while i <= len(table_row_data):
                experiment_data
                row_data = table_row_data[i:i+4]
                i+=4 
                if(len(row_data) > 0):
                    experiment_data.append(row_data)
    df = pd.DataFrame(columns=columns, data=experiment_data)
    print(df)         
else:
    print('Failed to retrieve the webpage')

