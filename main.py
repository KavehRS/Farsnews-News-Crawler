#Libs
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get Portal Data & Create DataFrame
link = requests.get('https://farsnews.ir/')
soup_link = BeautifulSoup(link.text, 'html.parser')
fna1 = pd.DataFrame()
