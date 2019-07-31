from google.appengine.ext import ndb

class Candidate(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    party = ndb.StringProperty(required = True)
    previous_job_or_pos = ndb.StringProperty(required = True)
    state_of_origin = ndb.StringProperty(required = True)
    picture = ndb.StringProperty(required = True)

    # def getCandidate(self):
    #     if(candidate_choice="donald_trump"):
    #         return donald_trump
    #     elif(candidate_choice="bill_weld"):
    #         return bill_weld
    #     elif(candidate_choice="michael_bennet"):
    #         return michael_bennet
    #     elif(candidate_choice="joe_biden"):
    #         return joe_biden
    #     elif(candidate_choice="cory_booker"):
    #         return cory_booker
    #     elif(candidate_choice="steve_bullock"):
    #         return steve_bullock
    #     elif(candidate_choice="pete_buttigieg"):
    #         return pete_buttigieg
    #     elif(candidate_choice="julian_castro"):
    #         return julian_castro
    #     elif(candidate_choice="bill_de_blasio"):
    #         return bill_de_blasio
    #     elif(candidate_choice="john_delany"):
    #         return john_delany
    #     elif(candidate_choice="tulsi_gabbard"):
    #         return tulsi_gabbard
    #     elif(candidate_choice="kirsten_gillibrand"):
    #         return kirsten_gillibrand
    #     elif(candidate_choice="kamala_harris"):
    #         return kamala_harris
    #     elif(candidate_choice="jay_inslee"):
    #         return jay_inslee
    #     elif(candidate_choice="amy_klobuchar"):
    #         return amy_klobuchar
    #     elif(candidate_choice="wayne_messam"):
    #         return wayne_messam
    #     elif(candidate_choice="seth_moulton"):
    #         return seth_moulton
    #     elif(candidate_choice="beto_orourke"):
    #         return beto_orourke
    #     elif(candidate_choice="tim_ryan"):
    #         return tim_ryan
    #     elif(candidate_choice="bernie_sanders"):
    #         return bernie_sanders
    #     elif(candidate_choice="joe_sestak"):
    #         return joe_sestak
    #     elif(candidate_choice="tom_steyer"):
    #         return tom_steyer
    #     elif(candidate_choice="elizabeth_warren"):
    #         return elizabeth_warren
    #     elif(candidate_choice="marianne_williamson"):
    #         return marianne_williamson
    #     elif(candidate_choice="andrew_yang"):
    #         return andrew_yang
    #     else
    #         return Candidate(first_name = "Name", last_name = "Name", party = "Party", previous_job_or_pos= "Position", state_of_origin = "State")

donald_trump = Candidate(first_name = "Donald", last_name = "Trump", party = "Republican", previous_job_or_pos= "President of America", state_of_origin = "New York", picture = "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg")
bill_weld = Candidate(first_name = "Bill", last_name = "Weld", party = "Republican", previous_job_or_pos= "Former Governor of Massachusetts", state_of_origin = "New York", picture="https://www.bostonherald.com/wp-content/uploads/migration/1969/12/31/3fb479ea-ec4e-11e8-906c-093cb180313d-e1548326775598.jpg?w=526")
michael_bennet = Candidate(first_name = "Michael", last_name = "Bennet", party = "Democrat", previous_job_or_pos= "United States Senator from Colorado", state_of_origin = "Colorado", picture="https://s3.amazonaws.com/ballotpedia-api/storage/uploads/thumbs/200/300/crop/best/Michael_Bennet.jpg")
joe_biden = Candidate(first_name = "Joe", last_name = "Biden", party = "Democrat", previous_job_or_pos= "Former Vice President", state_of_origin = "Delaware", picture = "https://d3i6fh83elv35t.cloudfront.net/static/2019/07/2019-07-11T183417Z_1387027311_RC152B0BE320_RTRMADP_3_USA-ELECTION-BIDEN-1024x683.jpg")
cory_booker = Candidate(first_name = "Cory", last_name = "Booker", party = "Democrat", previous_job_or_pos= "United States Senator from New Jersey", state_of_origin = "New Jersey", picture = "https://www.the74million.org/wp-content/uploads/2018/09/Cory-Booker-rally.jpg")
steve_bullock = Candidate(first_name = "Steve", last_name = "Bullock", party = "Democrat", previous_job_or_pos= "Governer of Montana", state_of_origin = "Montana", picture="https://cdn.cnn.com/cnnnext/dam/assets/190514112858-01-steve-bullock-file-2018-exlarge-169.jpg")
pete_buttigieg = Candidate(first_name = "Pete", last_name = "Buttigieg", party = "Democrat", previous_job_or_pos= "Mayor of South Bend", state_of_origin = "Indiana", picture="https://southbendin.gov/wp-content/uploads/2018/05/pete-buttigieg-mayor-south-bend-in.jpg")
julian_castro = Candidate(first_name = "Julian", last_name = "Castro", party = "Democrat", previous_job_or_pos= "Former Secretary of Housing and Urban Development", state_of_origin = "Texas", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Juli%C3%A1n_Castro%27s_Official_HUD_Portrait.jpg/220px-Juli%C3%A1n_Castro%27s_Official_HUD_Portrait.jpg")
bill_de_blasio = Candidate(first_name = "Bill", last_name = "de Blasio", party = "Democrat", previous_job_or_pos= "Mayor of New York City", state_of_origin = "New York", picture="https://pixel.nymag.com/imgs/daily/intelligencer/2019/01/17/17-bill-de-blasio.w700.h700.jpg")
john_delany = Candidate(first_name = "John", last_name = "Delany", party = "Democrat", previous_job_or_pos= "Former United States Repesentative for Maryland's 6th District", state_of_origin = "Maryland", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/John_Delaney_113th_Congress_official_photo.jpg/220px-John_Delaney_113th_Congress_official_photo.jpg")
tulsi_gabbard = Candidate(first_name = "Tulsi", last_name = "Gabbard", party = "Democrat", previous_job_or_pos = "United States Representative for Hawaii's Second District", state_of_origin = "Hawaii", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Tulsi_Gabbard%2C_official_portrait%2C_113th_Congress.jpg/220px-Tulsi_Gabbard%2C_official_portrait%2C_113th_Congress.jpg")
kirsten_gillibrand = Candidate(first_name = "Kirsten", last_name = "Gillibrand", party = "Democrat", previous_job_or_pos= "United States Senator from New York", state_of_origin = "New York", picture="https://cdn.britannica.com/s:300x300/07/181907-004-233E2AD3.jpg")
kamala_harris = Candidate(first_name = "Kamala", last_name = "Harris", party = "Democrat", previous_job_or_pos= "United States Senator from California", state_of_origin = "California", picture="https://lasentinel.net/wp-content/uploads/sites/5/2018/10/Kamala_Harris_official_photo.jpg")
john_hickenlooper = Candidate(first_name = "John", last_name = "Hickenlooper", party="Democrat", previous_job_or_pos="Former Governor of Colorado", state_of_origin="Colorado", picture="https://cdn.cnn.com/cnnnext/dam/assets/190110131551-hickenlooper-hedshot-exlarge-169.jpg")
jay_inslee = Candidate(first_name = "Jay", last_name = "Inslee", party = "Democrat", previous_job_or_pos= "Governor of Washington", state_of_origin = "Washington", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Jay_Inslee_official_portrait_%28cropped_2%29.jpg/1200px-Jay_Inslee_official_portrait_%28cropped_2%29.jpg")
amy_klobuchar= Candidate(first_name = "Amy", last_name = "Klobuchar", party = "Democrat", previous_job_or_pos= "United States Senator from Minnesota", state_of_origin = "Minnesota", picture="https://cdn.britannica.com/s:300x300/19/132819-004-940E3235.jpg")
wayne_messam = Candidate(first_name = "Wayne", last_name = "Messam", party = "Democrat", previous_job_or_pos= "Mayor of Miramar", state_of_origin = "Florida", picture="https://fivethirtyeight.com/wp-content/uploads/2019/03/MESSAM-4x3.jpg?w=575")
seth_moulton = Candidate(first_name = "Seth", last_name = "Moulton", party = "Democrat", previous_job_or_pos = "United States Representative for Massachusetts' Sixth District", state_of_origin = "Massachusetts", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Seth_Moulton.jpg/220px-Seth_Moulton.jpg")
beto_orourke = Candidate(first_name = "Beto", last_name = "O'Rourke", party = "Democrat", previous_job_or_pos= "Former United States Representative for Texas' Sixteenth District", state_of_origin = "Texas", picture="https://cdn.images.express.co.uk/img/dynamic/78/590x/Beto-O-Rourke-1159876.jpg?r=1564536163752")
tim_ryan = Candidate(first_name = "Tim", last_name = "Ryan", party = "Democrat", previous_job_or_pos= "United States Representative for Ohio's Thirteenth District", state_of_origin = "Ohio", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Rep._Tim_Ryan_Congressional_Head_Shot_2010.jpg/220px-Rep._Tim_Ryan_Congressional_Head_Shot_2010.jpg")
bernie_sanders = Candidate(first_name = "Bernie", last_name = "Sanders", party = "Democrat", previous_job_or_pos= "United States Senator from Vermont", state_of_origin = "Vermont", picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPzueftBrt70-I2HhH5XqkojrAWSpfwsdJ5tlU6548jCzWcQAC")
joe_sestak = Candidate(first_name = "Joe", last_name = "Sestak", party = "Democrat", previous_job_or_pos= "Former United States Representative for Pennsylvania's Seventh District", state_of_origin = "Pennsylvania", picture="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Rear_Admiral_Joseph_A._Sestak.jpeg/220px-Rear_Admiral_Joseph_A._Sestak.jpeg")
tom_steyer = Candidate(first_name = "Tom", last_name = "Steyer", party = "Democrat", previous_job_or_pos= "Philanthropist", state_of_origin = "California", picture ="https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1440,w_2560,x_0,y_0/dpr_1.5/c_limit,w_1044/fl_lossy,q_auto/v1527570297/180525-Grove-Tom-Steyer-intv-hero_ti5qfj")
elizabeth_warren = Candidate(first_name = "Elizabeth", last_name = "Warren", party = "Democrat", previous_job_or_pos= "United States Senate from Massachusetts", state_of_origin = "Massachusetts", picture="https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTM5Nzc3OTE4ODQxNjYwNDI3/elizabeth-warren-official-portraitjpg.jpg")
marianne_williamson = Candidate(first_name = "Marianne", last_name = "Williamson", party = "Democrat", previous_job_or_pos= "Author", state_of_origin = "California", picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLWJ7g3Db-_SpxJHzsXfOoR8ltRDjRQOckkxjjQvmDBMSO8Tsyiw")
andrew_yang = Candidate(first_name = "Andrew", last_name = "Yang", party = "Democrat", previous_job_or_pos= "Entrepreneur", state_of_origin = "New York", picture="https://assets3.thrillist.com/v1/image/2832187/size/sk-2017_04_featured_listing_mobile.jpg")

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
