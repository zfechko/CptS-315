"""
Zach Fechko
CptS 315
Feature Extraction

This file contains the functions that extract features from the data that coincide with the dataset
"""

"""
Criteria for feature extraction:
- Has IP address in url
- URL is longer than 54 characters
- URL uses a shortening service
- URL has a @ symbol
- Redirects using //
- URL has a dash
- URL has a subdomain and multi subdomains
"""

"""
- 1 if the url is phishy
- -1 if the url is not phishy
"""


import numpy as np
import pandas as pd
from urllib.parse import urlparse, urlencode
import ipaddress
import re
import whois

def has_ip(url):
    """
    Returns 1 if the url has an IP address in the url, -1 otherwise
    """
    try:
        ipaddress.ip_address(url)
        return 1
    except:
        return -1

def url_length(url):
    """
    Returns 1 if the url is longer than or equal to 54 characters, -1 otherwise
    """
    if len(url) <= 54:
        return -1
    else:
        return 1

def uses_shortening_service(url):
    """
    returns 1 if the url uses a shortening service, -1 otherwise
    """
    if re.search(r'(bit.ly|goo.gl|tinyurl.com|ow.ly|bitly.com|t.co|bit.do|adf.ly|is.gd|cutt.ly|v.gd|buff.ly|q.gs|lnkd.in|tr.im|tiny.cc|tinyurl.com|ow.ly|bitly.com|t.co|bit.do|adf.ly|is.gd|cutt.ly|v.gd|buff.ly|q.gs|lnkd.in|tr.im|tiny.cc)', url):
        return 1
    else:
        return -1

def has_at_symbol(url):
    """
    Returns 1 if the url has an @ symbol in the url, -1 otherwise
    """
    if re.search(r'@', url):
        return 1
    else:
        return -1

def has_double_slash(url):
    """
    Returns 1 if the url redirects using //, -1 otherwise
    """
    if re.search(r'//', url):
        return 1
    else:
        return -1

def has_dash(url):
    """
    Returns 1 if the url has a dash in the url, -1 otherwise
    """
    if '-' in urlparse(url).netloc: # checks if the domain has a dash as a prefix or suffix
        return 1
    else:
        return -1

def has_subdomain(url):
    """
    Returns 1 if the url has a subdomain, -1 otherwise
    """
    if len(urlparse(url).netloc.split('.')) == 3: # checks if the domain has a subdomain
        return 1
    else:
        return -1

def has_multi_subdomains(url):
    """
    Returns 1 if the url has multiple subdomains, -1 otherwise
    """
    if len(urlparse(url).netloc.split('.')) > 3: # checks if the domain has multiple subdomains
        return 1
    else:
        return -1

def has_https(url):
    """
    Returns 1 if the url uses https, -1 otherwise
    """
    if urlparse(url).scheme == 'https':
        return 1
    else:
        return -1

def extract_features(url: pd.DataFrame):
    """
    Returns a dataframe containing the extracted features
    """
    features = pd.DataFrame(columns = ['having_IP_Address', 'URL_Length', 'Shortining_Service', 'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix', 'having_Sub_Domain'])
    features['having_IP_Address'] = url.apply(lambda x: has_ip(x['url']), axis = 1)
    features['URL_Length'] = url.apply(lambda x: url_length(x['url']), axis = 1)
    features['Shortining_Service'] = url.apply(lambda x: uses_shortening_service(x['url']), axis = 1)
    features['having_At_Symbol'] = url.apply(lambda x: has_at_symbol(x['url']), axis = 1)
    features['double_slash_redirecting'] = url.apply(lambda x: has_double_slash(x['url']), axis = 1)
    features['Prefix_Suffix'] = url.apply(lambda x: has_dash(x['url']), axis = 1)
    features['having_Sub_Domain'] = url.apply(lambda x: has_subdomain(x['url']), axis = 1)

    return features



