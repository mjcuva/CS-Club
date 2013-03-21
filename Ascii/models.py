from google.appengine.ext import db

import util

class AsciiArt(db.Model):
    art = db.TextProperty(required = True)
    posted = db.DateTimeProperty(auto_now_add = True)
    title = db.StringProperty(required = True)

class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)

    @classmethod
    def register(cls, name, password):
        pw_hash = util.make_pw_hash(name, password)
        return User(username = name, pw_hash = pw_hash)

    @classmethod
    def by_name(cls, name):
        u = User.all().filter("username =", name).get()
        return u