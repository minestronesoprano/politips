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

cands = Candidate.query().fetch()

def getCandidate(candidate_choice):
	if(candidate_choice=="donald_trump"):
		return cands(donald_trump) #fix this line 
	elif(candidate_choice=="bill_weld"):
		return bill_weld
	elif(candidate_choice=="michael_bennet"):
		return michael_bennet
	elif(candidate_choice=="joe_biden"):
		return joe_biden
	elif(candidate_choice=="cory_booker"):
		return cory_booker
	elif(candidate_choice=="steve_bullock"):
		return steve_bullock
	elif(candidate_choice=="pete_buttigieg"):
		return pete_buttigieg
	elif(candidate_choice=="julian_castro"):
		return julian_castro
	elif(candidate_choice=="bill_de_blasio"):
		return bill_de_blasio
	elif(candidate_choice=="john_delany"):
		return john_delany
	elif(candidate_choice=="tulsi_gabbard"):
		return tulsi_gabbard
	elif(candidate_choice=="kirsten_gillibrand"):
		return kirsten_gillibrand
	elif(candidate_choice=="kamala_harris"):
		return kamala_harris
	elif(candidate_choice=="jay_inslee"):
		return jay_inslee
	elif(candidate_choice=="amy_klobuchar"):
		return amy_klobuchar
	elif(candidate_choice=="wayne_messam"):
		return wayne_messam
	elif(candidate_choice=="seth_moulton"):
		return seth_moulton
	elif(candidate_choice=="beto_orourke"):
		return beto_orourke
	elif(candidate_choice=="tim_ryan"):
		return tim_ryan
	elif(candidate_choice=="bernie_sanders"):
		return bernie_sanders
	elif(candidate_choice=="joe_sestak"):
		return joe_sestak
	elif(candidate_choice=="tom_steyer"):
		return tom_steyer
	elif(candidate_choice=="elizabeth_warren"):
		return elizabeth_warren
	elif(candidate_choice=="marianne_williamson"):
		return marianne_williamson
	elif(candidate_choice=="andrew_yang"):
		return andrew_yang
	else:
		return Candidate(first_name = "Name", last_name = "Name", party = "Party", previous_job_or_pos= "Position", state_of_origin = "State")



# the handler section

class MainPage(webapp2.RequestHandler):
	def get(self):  # for a get request
		welcome_template = the_jinja_env.get_template('templates/home-Politips.html')
		self.response.write(welcome_template.render())  # the response

class PersonHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		person_template = the_jinja_env.get_template('templates/profile.html')
		cand = getCandidate("donald_trump")
		profile_data = {
		"first_name" : cand.request.get("first_name"),
		"last_name" : cand.request.get("last_name"),
		"party" : cand.request.get("party"),
		"previous_job_or_pos": cand.request.get("previous_job_or_pos"),
		"state_of_origin" : cand.request.get("state_of_origin")
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
