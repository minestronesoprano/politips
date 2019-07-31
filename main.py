# main.py
# the import section
import webapp2
import jinja2
import os
from classes import Candidate

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)


# the handler section

class MainPage(webapp2.RequestHandler):
	def get(self):  # for a get request
		welcome_template = the_jinja_env.get_template('templates/home-Politips.html')
		self.response.write(welcome_template.render())  # the response

class PersonHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		person_template = the_jinja_env.get_template('templates/profile.html')
		cand = getCandidate()
		profile_data = {
		"first_name" = cand.first_name,
		"last_name" = cand.last_name,
		"party" = cand.party,
		"previous_job_or_pos"= cand.previous_job_or_pos,
		"state_of_origin" = cand.state_of_origin)
		}
		self.response.write(person_template.render(profile_data))  # the response

class RegHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		register_template = the_jinja_env.get_template('templates/register.html')
		self.response.write(register_template.render())  # the response

class PollingHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		poll_template = the_jinja_env.get_template('templates/pollingplace.html')
		self.response.write(poll_template.render())  # the response

class EntryHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		entry_template = the_jinja_env.get_template('templates/entry.html')
		self.response.write(entry_template.render())  # the response

class EntryDone(webapp2.RequestHandler):
	def post(self):
		results_template = the_jinja_env.get_template('templates/results.html')

		first_name = self.request.get("first_name")
		meme_first_line = self.request.get('last_name')
		meme_second_line = self.request.get('party')
		

		self.response.write(results_template.render(meme_data))

	def get(self):
		return self.post()
#class Statefinder(webapp2.RequestHandler):
	#def post(self):


# the app configuration section
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/candidate', PersonHandler),
	('/register',RegHandler),
	('/pollingplace',PollingHandler),
	('/entry',EntryHandler)
], debug=True)
