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
import webapp2
import jinja2
import os
import models
import hmac
import util

secret = 'vadflksjdfsd'

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_cookie(self, name, value):
        val = self.make_secure_val(value)
        return self.response.headers.add_header("Set-Cookie", "%s=%s" % (name, val))

    def make_secure_val(self, val):
        return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

    def check_secure_val(self, secure_val):
        val = secure_val.split('|')[0]
        if secure_val == self.make_secure_val(val):
            return val

class MainHandler(Handler):
    def get(self):
        if(self.request.cookies.get('user') and self.check_secure_val(self.request.cookies.get('user'))):
            user = models.User.get_by_id(int(self.request.cookies.get('user').split('|')[0]))
        else:
            user = None
        art = "Enter your own art here!"
        createdArt = models.AsciiArt.all().order('-posted')
        self.render('base.html', art = art, createdArt = createdArt, user = user)

    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')

        if title and art:
            a = models.AsciiArt(title = title, art = art)
            a.put()
            self.redirect("/")
        else:
            error = "You need both title and art"
            self.render('base.html', error = error, title = title, art = art)


class registerHandler(Handler):

    def get(self):
        self.render('register.html')

    def post(self):
        username = self.request.get("username")
        password = self.request.get('password')
        verify = self.request.get('verify_password')

        if(password != verify):
            self.render('register.html', username = username, error = "Passwords don't match")
        elif(not password or not verify or not username):
            self.render('register.html', username = username, error = "Missing Required Field")
        else:
            user = models.User.register(username, password)
            user.put()
            self.set_cookie("user", str(user.key().id()))
            self.redirect('/')

class loginHandler(Handler):

    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        if(not username or not password):
            self.render('login.html', username = username, error = "Missing Username or Password")
        else:
            u = models.User.by_name(username)
            if(not u):
                self.render('login.html', username = username, error = "Invalid Username")
            elif(not util.valid_pw(username, password, u.pw_hash)):
                self.render('login.html', username = username, error = "Invalid Password")
            else:
                self.set_cookie('user', str(u.key().id()))
                self.redirect('/')

class logout(Handler):
    def get(self):
        self.set_cookie('user', str(""))
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', loginHandler),
    ('/register', registerHandler),
    ('/logout', logout)
], debug=True)
