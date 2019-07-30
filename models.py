from google.appengine.ext import ndb

class Candidate(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
    party = ndb.StringProperty(required=True)
	state = ndb.StringProperty(required=False)
	position = ndb.StringProperty(required=False)
