import urllib2
import numpy.testing as npt



url_instance= urllib2.urlopen('https://twitter.com/search?q=%23pyboot&mode=realtime')
content = url_instance.read()
url_instance.close()

def scrape_usernames_quick_and_dirty(content):
    "extract @ usernames from content of a twitter search page" 
    # you can do this more elegantly with regular expressions (import re), but
    # we don't have time to go over them, and as Jamie Zawinski once said:
    #
    #    Some people, when confronted with a problem, think: "I know, I'll use
    #    regular expressions." Now they have two problems.
    #
    # Also, we should note that there are better ways of parsing out html
    # pages in Python. Have a look at 
    at_marker = '<s>@</s><b>'
    end_marker = '</b>'
    start = 0
    usernames = []
    while True:
        # find the first index of an @ marker
        hit = content.find(at_marker, start) 
        if hit == -1:
            # we hit the end and nothing was found, break out of the while
            # loop, and return what we have
            break;
        hit += len(at_marker) 
        end = content.find(end_marker, hit) 
        if hit != end:
            # twitter has some @ signs with no usernames on that page
            username = content[hit:end]
            usernames.append(username)
        start = end
    return usernames

def scrape_usernames_beautiful(content):
    try:
        import BeautifulSoup
    except ImportError:
        raise("Sorry, you'll need to install BeautifulSoup to use this" ) 
    soup = BeautifulSoup.BeautifulSoup(content)

    all_bs = [x.findParent().findNextSibling('b') for x in soup.findAll('s', text='@')]

    usernames = []
    for b in all_bs:
        if len(b.contents) > 0:
            # twitter has some @ signs with no usernames on that page
            usernames.append(b.contents[0])

    return usernames

def test_scrapers():
    "Verify that our two ways of getting usernames yields the same results" 
    url_instance= urllib2.urlopen('https://twitter.com/search?q=%23pyboot&mode=realtime')
    content = url_instance.read()
    url_instance.close()

    names_quick = scrape_usernames_quick_and_dirty(content) 
    names_beautiful = scrape_usernames_beautiful(content) 

    npt.assert_array_equal(names_quick, names_beautiful) 

