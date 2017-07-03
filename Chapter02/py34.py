from urllib.request import urlopen
from urllib.error import URLError

def fetch_email(url):
    try:
        data = urlopen(url).read().decode('utf8')
        return data.split('mailto:')[1].split('"')[0]
    except (IndexError, URLError) as error:
        print(error)
        return 'invalid@example.com'
