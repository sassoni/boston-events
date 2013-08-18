#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import logging
import feedparser
import jinja2
import datetime

now = datetime.datetime.now()

def test_class():
    e = feedparser.parse('http://events.mit.edu/rss/index.html')
#    print e.feed.date
#    print e['feed']['title']
	
    return e.entries
# print e.feed.date_parsed
# print e.feed.updated_parsed

#print e.entries[0].title

 #   for entry in e.entries:
 #       logging.debug(entry.title)
		

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])
		
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hlala!')
        logging.debug("debug test")
        eventslist = test_class()
		
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
