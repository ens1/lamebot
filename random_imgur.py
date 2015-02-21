import random
import string
import urllib
import hashlib


def randomurl():
    file=[]
    for i in range(0,5):
        file.append(random.choice(string.ascii_letters + string.digits))
    file=string.join(file, "")
    return "http://i.imgur.com/" + file + ".jpg"

def downloadimage(url):
    return urllib.urlopen(url).read()


def returnimage():
    generatedurl = randomurl()
    imagefile = downloadimage(generatedurl)
    if('d835884373f4d6c8f24742ceabe74946' == hashlib.md5(imagefile).hexdigest()):
        return returnimage()
    else:
        return generatedurl

