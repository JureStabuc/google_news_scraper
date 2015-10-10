# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
import urllib2
from xml.dom.minidom import parseString

def get_google_new_results( term, count ):
    results = []
    obj = parseString( urllib2.urlopen('http://news.google.com/news?q=%s&output=rss' % term).read() )

    elements = obj.getElementsByTagName('title')[2:] # To get rid of unwanted title elements in XML doc    
    links = obj.getElementsByTagName('link')[2:]
    print links
    for element in elements[:count]:
        headline =  element.childNodes[0].data
        for link in links:
            url = link.childNodes[0].data.split('=')[-1]
        newssearch = headline + ' -> ' + url
        results.append( newssearch )

    return results

items = get_google_new_results( 'apple', 2 )
for i,e in enumerate(items):
    print '%d: %s' % (i+1,e,)
