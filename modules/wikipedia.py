import urllib2


def returnurl(searchterm):
    wiki="http://en.wikipedia.org/w/index.php?search=%s" % searchterm
    return urllib2.urlopen(wiki).geturl()

def randompage():
    return urllib2.urlopen("http://en.wikipedia.org/wiki/Special:Random").geturl()
