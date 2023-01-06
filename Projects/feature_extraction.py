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
- -1 if the url is phishy
- 1 if the url is not phishy
"""


import numpy as np
import pandas as pd
from urllib.parse import urlparse, urlencode
import urllib.request, urllib.parse, urllib.error
import ipaddress
import re
import whois
from bs4 import BeautifulSoup
import datetime

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
        return -1
    else:
        return 1

def has_at_symbol(url):
    """
    Returns -1 if the url has an @ symbol in the url, 1 otherwise
    """
    if re.search(r'@', url):
        return -1
    else:
        return 1

def has_double_slash(url):
    """
    Returns -1 if the url redirects using //, 1 otherwise
    """
    if re.search(r'//', url):
        return -1
    else:
        return 1

def has_dash(url):
    """
    Returns 1 if the url has a dash in the url, -1 otherwise
    """
    if '-' in urlparse(url).netloc: # checks if the domain has a dash as a prefix or suffix
        return -1 #phishy
    else:
        return 1 #not phishy

def has_subdomain(url):
    """
    Returns 1 if the url has a subdomain, -1 otherwise
    """
    if len(urlparse(url).netloc.split('.')) == 3: # checks if the domain has a subdomain
        return -1 #phishy
    else:
        return 1 #not phishy

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

def page_rank(url):
    """
    - Returns -1 if the url ranks low on Alexa, 1 otherwise
    - Low ranking means the rank is greater than 100,000
    """
    url = urllib.parse.quote(url)
    try:
        rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
        if int(rank) > 100000:
            return -1
        else:
            return 1
    except TypeError:
        return 1

def domain_registration(url):
    """
    - extracts how long the domain has been registered for from whois
    - returns -1 if the domain has been registered for less than 6 months, 1 otherwise
    """
    creation_date = whois.whois(urlparse(url).netloc).creation_date
    expiration_date = whois.whois(urlparse(url).netloc).expiration_date
    if type(creation_date) == str or type(expiration_date) == str:
        try:
            creation_date = datetime.datetime.strptime(creation_date, '%Y-%m-%d')
            expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
        except:
            return 1
    if expiration_date is None or creation_date is None:
        return 1
    elif type(expiration_date) == list or type(creation_date) == list:
        return 1
    else:
        if (expiration_date - creation_date).days <= 180:
            return -1
        else:
            return 1

def favicon(url):
    """
    - Checks if the favicon is the same as the domain
    - Returns 1 if it is, -1 otherwise
    """
    try:
        favicon = BeautifulSoup(urllib.request.urlopen(url).read(), "xml").find("link", rel="shortcut icon")['href']
        if favicon == url + '/favicon.ico':
            return 1
        else:
            return -1
    except:
        return 1

def port(url):
    """
    - Checks if the url uses a non-standard port
    - Returns -1 if it does, 1 otherwise
    """
    if urlparse(url).port:
        return -1
    else:
        return 1

def iframe(response):
    if response == "":
        return 1
    else:
        if re.findall(r"[<iframe>|<frameBorder>]", response.text):
            return -1
        else:
            return 1

def popup(response):
    if response == "":
        return 1
    else:
        if re.findall(r"alert\(", response.text):
            return -1
        else:
            return 1

def on_mouseover(response):
    if response == "":
        return 1
    else:
        if re.findall(r"onmouseover", response.text):
            return -1
        else:
            return 1

def disable_right_click(response):
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return -1
        else:
            return 1


def num_forwards(response):
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 1
        elif 2 < len(response.history) <= 4:
            return 0
        else:
            return -1


def extract_features(url):
    features = []
    features.append(has_ip(url))
    features.append(url_length(url))
    features.append(uses_shortening_service(url))
    features.append(has_at_symbol(url))
    features.append(has_double_slash(url))
    features.append(has_dash(url))
    features.append(has_subdomain(url))
    features.append(has_https(url))

    dns = 0
    try:
        domain_name = whois.whois(urlparse(url).netloc)
    except:
        dns = 1
    features.append()




