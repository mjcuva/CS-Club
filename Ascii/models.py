from google.appengine.ext import db

class AsciiArt(db.Model):
    art = db.TextProperty(required = True)
    posted = db.DateTimeProperty(auto_now_add = True)
    title = db.StringProperty(required = True)