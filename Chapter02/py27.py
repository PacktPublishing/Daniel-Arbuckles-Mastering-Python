from urllib2 import urlopen, URLError


def fetch_email(url):
    try:
        data = urlopen(url).read()
        return data.split('mailto:')[1].split('"')[0]
    except (IndexError, URLError), error:
        print error
        return 'invalid@example.com'
