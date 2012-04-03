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
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')
        zipcode = int(self.request.get('zipcode'))
        role = self.request.get('role')
        user_info = User(username = username,
                         email = email,
                         password = password,
                         zipcode = zipcode,
                         role = role)
        user_info.put()
        
        self.redirect('/moreinfo')

class MoreInfo(webapp.RequestHandler):

    def get(self):
        user = self.request.get('user')
        template_values = {'user': user,
                           'logout_url': users.create_logout_url("/"),
                           'login_url': users.create_login_url(self.request.uri)}

        self.response.out.write(template.render('static/moreinfo.html', template_values))                                                                   
        #else:
        #    self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')
        zipcode = int(self.request.get('zipcode'))
        user_info = User(username = username,
                         email = email,
                         password = password,
                         zipcode = zipcode)
        user_info.put()
        user = db.GqlQuery("SELECT * FROM User WHERE email=%s" % email)
        
        template_values = {'user': user,
                           'logout_url': users.create_logout_url("/"),
                           'login_url': users.create_login_url(self.request.uri)}
        
        self.response.out.write(template.render('/moreinfo', template_values))