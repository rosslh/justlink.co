import re
import urllib

import urllib3
from bs4 import BeautifulSoup

import certifi

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Force certificate check.
    ca_certs=certifi.where(),  # Path to the Certifi bundle.
)


def notAnAd(tag):
    if tag.name == 'a' and tag.get('class') == [u'result__a']:
        for parent in tag.parents:
            try:
                if u'result--ad' in parent.get('class'):
                    return False
            except Exception as e:
                pass
        return True


def getLink(query):
    query = "%20".join(re.findall(r"[\w']+", query))
    try:
        r = http.request('GET', 'https://duckduckgo.com/html/?q=' + query)
    except Exception as e:  # urllib3.exceptions.SSLError
        print(str(e))
    soup = BeautifulSoup(r.data, 'html.parser')
    urls = ["{}{}".format('http', link.get('href').split('http')[-1]) for link in soup.find_all(notAnAd)]
    return urllib.unquote(urls[0])


print(getLink("facebook privacy policy"))
