# -*- coding: utf-8 -*-

import logging
import cgi
import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

class InfiniteGadgetHandler(webapp.RequestHandler):
  def get(self, encoded_wave_id):
    wave_id = encoded_wave_id.replace('%21', '!').replace('%2B', '+')
    wave_server = 'http://wave.google.com/'
    if wave_id.find('wavesandbox') < 0:
      wave_server = wave_server + 'a/wavesandbox.com/'
    else:
      wave_server = wave_server + 'wave/'
    path = os.path.join(os.path.dirname(__file__), 'infinite_gadget.xml')
    self.response.out.write(template.render(path, {
      'wave_id': wave_id,
      'wave_server': wave_server
    }))

def main():
  application = webapp.WSGIApplication([(r'/infinite_gadget/(.*)', InfiniteGadgetHandler),
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
