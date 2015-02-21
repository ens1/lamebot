#!/usr/bin/python2
# Uses distrowatch.com to return a random distro or find one
# by andri
import urllib2
import string
def returndistro(text):
    i = "http://distrowatch.com/"
    # If no arguments are given, it gives you a random distro with random.php
    if len(text)==0:
        # Uses random.php to be directed to a random distro page
        site = urllib2.urlopen(i + "random.php")
        # Gets the distro name from the title
        distro = site.readlines()[1][24:-9]
        # Gets the URL from the distro page
        url = site.geturl()
        # Returns the distro name and the URL
        return("%s - %s" % (distro, url))
    else:
        # Only uses the first argument, because 2 or more won't make a difference
        # For example, ankur still returns Ankur Bangla and damn returns Damn Small
        a = text[0]
        # Uses table.php to be directed to a distro page
        site = urllib2.urlopen(i + "table.php?distribution=%s" %a)
        # Gets the distro name from the title
        distro = site.readlines()[1][24:-9]
        # Gets the URL from the 
        url = site.geturl()
        # If the distro name is empty, returns that it didn't find it
        if distro != "":
            return("%s - %s" % (distro, url))
        else:
            return("Did not find distro named %s." %a)
