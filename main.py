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
	if(candidate_choice=="Donald Trump"):
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
	def get(self):  # for a get request
		person_template = the_jinja_env.get_template('templates/profile.html')

		choice = self.request.get("name")
		cand_surname = getLastName(choice)
		#cand_surname= "Trump"
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

	def get(self):
		person_template = the_jinja_env.get_template('templates/profile.html')
		self.response.write(person_template.render())

class RegHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		register_template = the_jinja_env.get_template('templates/register.html')
		self.response.write(register_template.render())  # the response

class PollingHandler(webapp2.RequestHandler):
	def post(self):  # for a get request
		poll_template = the_jinja_env.get_template('templates/pollingplace.html')
		state_data ={
			"Alabama" : "https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do",
			"Alaska" : "https://myvoterinformation.alaska.gov/",
			"Arizona" : "https://voter.azsos.gov/VoterView/PollingPlaceSearch.do",
			"Arkansas" : "https://www.voterview.ar-nova.org/VoterView/RegistrantSearch.do",
			"California" : "https://www.sos.ca.gov/elections/polling-place/",
			"Colorado" : "https://www.sos.state.co.us/pubs/elections/",
			"Connecticut" : "https://portaldir.ct.gov/sots/LookUp.aspx",
			"Delaware" : "https://ivote.de.gov/voterlogin.aspx",
			"Florida" : "https://registration.elections.myflorida.com/CheckVoterStatus",
			"Georgia" : "https://www.mvp.sos.ga.gov/MVP/mvp.do",
			"Hawaii" : "https://olvr.hawaii.gov/altpollingplacesearch.aspx",
			"Idaho" : "https://apps.idahovotes.gov/YourPollingPlace/WhereDoIVote.aspx",
			"Illinois" : "https://ova.elections.il.gov/PollingPlaceLookup.aspx",
			"Indiana" : "https://indianavoters.in.gov/",
			"Iowa" : "https://sos.iowa.gov/elections/voterreg/pollingplace/search.aspx",
			"Kansas" : "https://myvoteinfo.voteks.org/VoterView/PollingPlaceSearch.do",
			"Kentucky" : "https://vrsws.sos.ky.gov/vic/",
			"Louisiana" : "https://voterportal.sos.la.gov/",
			"Maine" : "http://www.maine.gov/portal/government/edemocracy/voter_lookup.php",
			"Maryland" : "https://elections.maryland.gov/voting/where.html",
			"Massachusetts" : "https://www.sec.state.ma.us/wheredoivotema/bal/myelectioninfo.aspx",
			"Michigan" : "https://mvic.sos.state.mi.us/",
			"Minnesota" : "http://pollfinder.sos.state.mn.us/",
			"Mississippi" : "http://www.sos.ms.gov/PollingPlace/Pages/default.aspx",
			"Missouri" : "http://www.sos.mo.gov/elections/pollingplacelookup/",
			"Montana" : "https://app.mt.gov/voterinfo/",
			"Nebraska" : "https://www.votercheck.necvr.ne.gov/VoterView/PollingPlaceSearch.do",
			"Nevada" : "http://nvsos.gov/votersearch/",
			"New Hampshire" : "http://app.sos.nh.gov/Public/PollingPlaceSearch.aspx",
			"New Jersey" : "https://voter.njsvrs.com/PublicAccess/servlet/com.saber.publicaccess.control.PublicAccessNavigationServlet?USERPROCESS=PollingPlace",
			"New Mexico" : "https://voterportal.servis.sos.state.nm.us/WhereToVote.aspx?AspxAutoDetectCookieSupport=1",
			"New York" : "https://voterlookup.elections.ny.gov/",
			"North Carolina" : "https://vt.ncsbe.gov/PPLkup/",
			"North Dakota" : "https://vip.sos.nd.gov/wheretovote.aspx",
			"Ohio" : "https://www.sos.state.oh.us/elections/voters/toolkit/polling-location/",
			"Oklahoma" : "https://services.okelections.us/voterSearch.aspx",
			"Oregon" : "http://sos.oregon.gov/voting/Pages/drop-box-locator.aspx",
			"Pennsylvania" : "https://www.pavoterservices.state.pa.us/Pages/PollingPlaceInfo.aspx",
			"Rhode Island" : "https://sos.ri.gov/vic/",
			"South Carolina" : "https://info.scvotes.sc.gov/eng/voterinquiry/VoterInformationRequest.aspx?PageMode=VoterInfo",
			"South Dakota" : "https://sos.sd.gov/Elections/VIPLogin.aspx",
			"Tennessee" : "https://tnmap.tn.gov/voterlookup/",
			"Texas" : "https://teamrv-mvp.sos.texas.gov/MVP/mvp.do",
			"Utah" : "http://vote.utah.gov/vote/menu/index",
			"Vermont" : "https://mvp.sec.state.vt.us/",
			"Virginia" : "https://vote.elections.virginia.gov/VoterInformation/PollingPlaceLookup",
			"Washington" : "https://www.sos.wa.gov/elections/auditors.aspx",
			"West Virginia" : "https://services.sos.wv.gov/Elections/Voter/FindMyPollingPlace",
			"Wisconsin" : "https://myvote.wi.gov/en-US/FindMyPollingPlace",
			"Wyoming" : "http://soswy.state.wy.us/Elections/PollPlace/Default.aspx",
			"whee" : "about:blank"
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
