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


def getLastName(candidate_choice):
	if(candidate_choice=="donald_trump"):
		return "Trump" #fix this line
	elif(candidate_choice=="bill_weld"):
		return "Weld"
	elif(candidate_choice=="michael_bennet"):
		return "Bennet"
	elif(candidate_choice=="joe_biden"):
		return "Biden"
	elif(candidate_choice=="cory_booker"):
		return "Booker"
	elif(candidate_choice=="steve_bullock"):
		return "Bullock"
	elif(candidate_choice=="pete_buttigieg"):
		return "Buttigieg"
	elif(candidate_choice=="julian_castro"):
		return "Castro"
	elif(candidate_choice=="bill_de_blasio"):
		return "de Blasio"
	elif(candidate_choice=="john_delany"):
		return "Delany"
	elif(candidate_choice=="tulsi_gabbard"):
		return "Gabbard"
	elif(candidate_choice=="kirsten_gillibrand"):
		return "Gillibrand"
	elif(candidate_choice=="kamala_harris"):
		return "Harris"
	elif(candidate_choice=="jay_inslee"):
		return "Inslee"
	elif(candidate_choice=="amy_klobuchar"):
		return "Klobuchar"
	elif(candidate_choice=="wayne_messam"):
		return "Messam"
	elif(candidate_choice=="seth_moulton"):
		return "Moulton"
	elif(candidate_choice=="beto_orourke"):
		return "O'Rourke"
	elif(candidate_choice=="tim_ryan"):
		return "Ryan"
	elif(candidate_choice=="bernie_sanders"):
		return "Sanders"
	elif(candidate_choice=="joe_sestak"):
		return "Sestak"
	elif(candidate_choice=="tom_steyer"):
		return "Steyer"
	elif(candidate_choice=="elizabeth_warren"):
		return "Warren"
	elif(candidate_choice=="marianne_williamson"):
		return "Williamson"
	elif(candidate_choice=="andrew_yang"):
		return "Yang"
	else:
		return "Not Found"


# the handler section

class BaseHandler(webapp2.RequestHandler):
  def handle_exception(self, exception, debug):
    # Set a custom message.
    self.response.write('An error occurred.')

    # If the exception is a HTTPException, use its error code.
    # Otherwise use a generic 500 error code.
    if isinstance(exception, webapp2.HTTPException):
      self.response.set_status(exception.code)
    else:
      self.response.set_status(500)

class MainPage(webapp2.RequestHandler):
	def get(self):  # for a get request
		welcome_template = the_jinja_env.get_template('templates/home-Politips.html')
		self.response.write(welcome_template.render())  # the response

class PersonHandler(webapp2.RequestHandler):
	def get(post):  # for a get request
		person_template = the_jinja_env.get_template('templates/profile.html')
		cand_surname = getLastName(choice)
		cand = Candidate.query().filter(Candidate.last_name==cand_surname).fetch()[0]
		profile_data = {
		"first_name" : cand.first_name,
		"last_name" : cand.last_name,
		"party" : cand.party,
		"previous_job_or_pos": cand.previous_job_or_pos,
		"state_of_origin" : cand.state_of_origin,
		"picture" :cand.picture
		}
		self.response.write(person_template.render(profile_data))  # the response

class RegHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		register_template = the_jinja_env.get_template('templates/register.html')
		self.response.write(register_template.render())  # the response

class PollingHandler(webapp2.RequestHandler):
	def post(self):  # for a get request
		poll_template = the_jinja_env.get_template('templates/pollingplace.html')
		state_data ={
			"Massachusetts" : "https://www.sec.state.ma.us/wheredoivotema/bal/myelectioninfo.aspx",
			"New Jersey" : "https://voter.njsvrs.com/PublicAccess/servlet/com.saber.publicaccess.control.PublicAccessNavigationServlet?USERPROCESS=PollingPlace",
			"whee" : "about:blank"f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
		}
		state = self.request.get("states_list")
		vars = {
		"state_url" : state_data[state]
		}
		self.response.write(poll_template.render(vars))  # the response

	def get(self):
		poll_template = the_jinja_env.get_template('templates/pollingplace.html')
		self.response.write(poll_template.render())  # the response
#class Statefinder(webapp2.RequestHandler):
	#def post(self):

class ErrorHandler(BaseHandler):
	def get(self):
		error_template = the_jinja_env.get_template('templates/404.html')
		self.response.set_status(404)
		self.response.write(error_template.render())  # the response

# the app configuration section
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/candidate', PersonHandler),
	('/register',RegHandler),
	('/pollingplace',PollingHandler),
], debug=True)
