from google.appengine.ext import ndb

class Candidate(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    party = ndb.StringProperty(required = True)
    previous_job_or_pos = ndb.StringProperty(required = True)
    state_of_origin = ndb.StringProperty(required = True)

    def getCandidate(self):
        if(candidate_choice="donald_trump"):
            return donald_trump
        elif(candidate_choice="bill_weld"):
            return bill_weld
        elif(candidate_choice="michael_bennet"):
            return michael_bennet
        elif(candidate_choice="joe_biden"):
            return joe_biden
        elif(candidate_choice="cory_booker"):
            return cory_booker
        elif(candidate_choice="steve_bullock"):
            return steve_bullock
        elif(candidate_choice="pete_buttigieg"):
            return pete_buttigieg
        elif(candidate_choice="julian_castro"):
            return julian_castro
        elif(candidate_choice="bill_de_blasio"):
            return bill_de_blasio
        elif(candidate_choice="john_delany"):
            return john_delany
        elif(candidate_choice="tulsi_gabbard"):
            return tulsi_gabbard
        elif(candidate_choice="kirsten_gillibrand"):
            return kirsten_gillibrand
        elif(candidate_choice="kamala_harris"):
            return kamala_harris
        elif(candidate_choice="jay_inslee"):
            return jay_inslee
        elif(candidate_choice="amy_klobuchar"):
            return amy_klobuchar
        elif(candidate_choice="wayne_messam"):
            return wayne_messam
        elif(candidate_choice="seth_moulton"):
            return seth_moulton
        elif(candidate_choice="beto_orourke"):
            return beto_orourke
        elif(candidate_choice="tim_ryan"):
            return tim_ryan
        elif(candidate_choice="bernie_sanders"):
            return bernie_sanders
        elif(candidate_choice="joe_sestak"):
            return joe_sestak
        elif(candidate_choice="tom_steyer"):
            return tom_steyer
        elif(candidate_choice="elizabeth_warren"):
            return elizabeth_warren
        elif(candidate_choice="marianne_williamson"):
            return marianne_williamson
        elif(candidate_choice="andrew_yang"):
            return andrew_yang
        else
            return Candidate(first_name = "Name", last_name = "Name", party = "Party", previous_job_or_pos= "Position", state_of_origin = "State")


donald_trump = Candidate(first_name = "Donald", last_name = "Trump", party = "Republican", previous_job_or_pos= "President of the United States of America", state_of_origin = "New York")
bill_weld = Candidate(first_name = "Bill", last_name = "Weld", party = "Republican", previous_job_or_pos= "Former Governor of Massachusetts", state_of_origin = "New York")
michael_bennet = Candidate(first_name = "Michael", last_name = "Bennet", party = "Democrat", previous_job_or_pos= "United States Senator from Colorado", state_of_origin = "Colorado")
joe_biden = Candidate(first_name = "Joe", last_name = "Biden", party = "Democrat", previous_job_or_pos= "Former Vice President", state_of_origin = "Delaware")
cory_booker = Candidate(first_name = "Cory", last_name = "Booker", party = "Democrat", previous_job_or_pos= "United States Senator from New Jersey", state_of_origin = "New Jersey")
steve_bullock = Candidate(first_name = "Steve", last_name = "Bullock", party = "Democrat", previous_job_or_pos= "Governer of Montana", state_of_origin = "Montana")
pete_buttigieg = Candidate(first_name = "Pete", last_name = "Buttigieg", party = "Democrat", previous_job_or_pos= "Mayor of South Bend", state_of_origin = "Indiana")
julian_castro = Candidate(first_name = "Julian", last_name = "Castro", party = "Democrat", previous_job_or_pos= "Former Secretary of Housing and Urban Development", state_of_origin = "Texas")
bill_de_blasio = Candidate(first_name = "Bill", last_name = "de Blasio", party = "Democrat", previous_job_or_pos= "Mayor of New York City", state_of_origin = "New York")
john_delany = Candidate(first_name = "John", last_name = "Delany", party = "Democrat", previous_job_or_pos= "Former United States Repesentative for Maryland's 6th District", state_of_origin = "Maryland")
tulsi_gabbard = Candidate(first_name = "Tulsi", last_name = "Gabbard", party = "Democrat", previous_job_or_pos = "United States Representative for Hawaii's Second District", state_of_origin = "Maryland")
kirsten_gillibrand = Candidate(first_name = "Kirsten", last_name = "Gillibrand", party = "Democrat", previous_job_or_pos= "United States Senator from New York", state_of_origin = "New York")
kamala_harris = Candidate(first_name = "Kamala", last_name = "Harris", party = "Democrat", previous_job_or_pos= "United States Senator from California", state_of_origin = "California")
jay_inslee = Candidate(first_name = "Jay", last_name = "Inslee", party = "Democrat", previous_job_or_pos= "Governor of Washington", state_of_origin = "Washington")
amy_klobuchar= Candidate(first_name = "Amy", last_name = "Klobuchar", party = "Democrat", previous_job_or_pos= "United States Senator from Minnesota", state_of_origin = "Minnesota")
wayne_messam = Candidate(first_name = "Wayne", last_name = "Messam", party = "Democrat", previous_job_or_pos= "Mayor of Miramar", state_of_origin = "Florida")
seth_moulton = Candidate(first_name = "Seth", last_name = "Moulton", party = "Democrat", previous_job_or_pos = "United States Representative for Massachusetts' Sixth District", state_of_origin = "Massachusetts")
beto_orourke = Candidate(first_name = "Beto", last_name = "O'Rourke", party = "Democrat", previous_job_or_pos= "Former United States Representative for Texas' Sixteenth District", state_of_origin = "Texas")
tim_ryan = Candidate(first_name = "Tim", last_name = "Ryan", party = "Democrat", previous_job_or_pos= "United States Representative for Ohio's Thirteenth District", state_of_origin = "Ohio")
bernie_sanders = Candidate(first_name = "Bernie", last_name = "Sanders", party = "Democrat", previous_job_or_pos= "United States Senator from Vermont", state_of_origin = "Vermont")
joe_sestak = Candidate(first_name = "Joe", last_name = "Sestak", party = "Democrat", previous_job_or_pos= "Former United States Representative for Pennsylvania's Seventh District", state_of_origin = "Pennsylvania")
tom_steyer = Candidate(first_name = "Tom", last_name = "Steyer", party = "Democrat", previous_job_or_pos= "Philanthropist", state_of_origin = "California")
elizabeth_warren = Candidate(first_name = "Elizabeth", last_name = "Warren", party = "Democrat", previous_job_or_pos= "United States Senate from Massachusetts", state_of_origin = "Massachusetts")
marianne_williamson = Candidate(first_name = "Marianne", last_name = "Williamson", party = "Democrat", previous_job_or_pos= "Author", state_of_origin = "California")
andrew_yang = Candidate(first_name = "Andrew", last_name = "Yang", party = "Democrat", previous_job_or_pos= "Entrepreneur", state_of_origin = "New York")

donald_trump.put()
bill_weld.put()
michael_bennet.put()
joe_biden.put()
cory_booker.put()
steve_bullock.put()
pete_buttigieg.put()
julian_castro.put()
bill_de_blasio.put()
john_delany.put()
tulsi_gabbard.put()
kirsten_gillibrand.put()
kamala_harris.put()
jay_inslee.put()
amy_klobuchar.put()
wayne_messam.put()
seth_moulton.put()
beto_orourke.put()
tim_ryan.put()
bernie_sanders.put()
joe_sestak.put()
tom_steyer.put()
elizabeth_warren.put()
marianne_williamson.put()
andrew_yang.put()
