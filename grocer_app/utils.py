from pandas._config.config import T
import requests
from bs4 import BeautifulSoup
import pandas as pd
import socket

"""
Step 1: 
- request base URL
- send request tp 
"""
# Where to navigate
baseurl = 'https://www.checkers.co.za/c-2256/All-Departments?q=%3Arelevance%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff&page=0'
# laat requests soos browser lyk en nie python
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'}

requests = requests.get(baseurl, headers= user_agent).text
url_html = BeautifulSoup(requests,'html.parser')

product_name = url_html.find_all(string='18.99')

def get_requests_url_html(baseurl = None, user_agent = None):
    """
    Definition: this function parses the url_html value that is needed to find product name.
    ----------
    Inputs:
    baseurl: str
    user_agent: dict
    ----------
    Returns:
    url_html: (MORNE ASB VUL IN, ek het nie context oor wat presies BeautifulSoup doen nie)
    """
    requests = requests.get(baseurl, headers= user_agent).text
    url_html = BeautifulSoup(requests,'html.parser')
    return url_html



def get_local_ip():

    #get the local host name
    host_name = socket.gethostname()
    
    # Use the local host name to get the local IP
    local_ip = socket.gethostbyname(host_name)

    # Print the IP address
    print("Local IP Address: ", local_ip)
    return local_ip


