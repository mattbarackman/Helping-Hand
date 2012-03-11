import os
import datetime
import json
import urllib2
import logging
from math import log, exp, fabs
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import taskqueue
from models import *

        
class MainPage(webapp.RequestHandler):

    def get(self):
        user = users.get_current_user()
        #if                           
        template_values = {'user': users.get_current_user(),
                           'logout_url': users.create_logout_url("/"),
                           'login_url': users.create_login_url(self.request.uri)}
        
        self.response.out.write(template.render('static/index.html', template_values))                                                                   
        #else:
        #    self.redirect(users.create_login_url(self.request.uri))
            
class SignUp(webapp.RequestHandler):

    def get(self):
        user = users.get_current_user()                           
        
        template_values = {'user': users.get_current_user(),
                           'logout_url': users.create_logout_url("/"),
                           'login_url': users.create_login_url(self.request.uri)}

        self.response.out.write(template.render('static/signup.html', template_values))                                                                   
        #else:
        #    self.redirect(users.create_login_url(self.request.uri))
    
    def post(self):
        self.get
        
        self.redirect('/')