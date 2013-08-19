#!/usr/bin/env python

import os
import webapp2
import logging
import feedparser
import jinja2
import datetime

# today's date
today = datetime.date.today()
now = today.strftime("%A %d %B %Y")

rss_feeds_list = ['http://www.trumba.com/calendars/cob-calendar.rss',  
                  'http://events.mit.edu/rss/index.html']

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])
	
	
def parse_feeds():
    allevents = []
    
    for feed in rss_feeds_list:
        e = feedparser.parse(feed)
        
        for entry in e.entries:
            allevents.append(entry)
    
    return allevents
    
#return e.entries
# print e.feed.date_parsed
# print e.feed.updated_parsed
#print e.entries[0].title
#print e.feed.date
#print e['feed']['title']
#for entry in e.entries:
#logging.debug(entry.title)
		


		
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hlala!')
        logging.info("debug test")
        eventslist = parse_feeds()

        #for event in eventslist:
        #    logging.info(event)
		
        template_values = {
            'events': eventslist,
            'today_date': now,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        #for entry in eventslist:
        #    self.response.out.write(entry.title)
        #    self.response.out.write('<br>')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
