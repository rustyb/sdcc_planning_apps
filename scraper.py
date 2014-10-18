# This is a template for a Python scraper on Morph (https://morph.io)
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

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

unique_keys = [ 'reg_ref' ]
for i in range(1,447):
    html = requests.get("http://www.sdublincoco.ie/index.aspx?pageid=144&type=apps&fromdate=01-01-2007&todate=17-10-2014&dateoptions=specific&area=Any&keywordtype=regref&term=&p=%s" % i).content
    print "Page %s" % i
    dom = lxml.html.fromstring(html)
    
    for tr in dom.cssselect("tbody tr"):
        tds = tr.cssselect("td")
        if len(tds)==7:
            data = {
                'reg_ref' : tds[0].text_content(),
                'last_action' : tds[1].text_content(),
                'closing_date' : tds[2].text_content(),
                'app_name': tds[3].text_content(),
                'location': tds[4].text_content()
            }
            #print data
            scraperwiki.sql.save(unique_keys, data)
    
"""    for entry in dom.cssselect('tbody tr'):
        pp = {
            '
        }
        post = {
            'date_recieved': entry.cssselect('dd')[2].text_content(),
            'last_action': entry.cssselect('dd')[3].text_content(),
            'application_type': entry.cssselect('dd')[4].text_content(),
            'submission_type': entry.cssselect('dd')[5].text_content(),
            'applicant': entry.cssselect('dd')[7].text_content(),
            'location': entry.cssselect('dd')[8].text_content(),
            'proposed_dev': entry.cssselect('dd')[9].text_content(),
            'decision_due': entry.cssselect('dd')[10].text_content()
        }
        print post
    
"""
    
# Saving data:
# unique_keys = [ 'id' ]
# data = { 'id':12, 'name':'violet', 'age':7 }
# scraperwiki.sql.save(unique_keys, data)
