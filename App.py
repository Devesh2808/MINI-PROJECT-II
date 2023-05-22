from flask import Flask, render_template, request, url_for
import pickle
from sklearn import svm
import numpy as np

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/match")
def match():
    return render_template("match.html")


@app.route("/score")
def score():
    return render_template("score.html")


@app.route("/predict_match", methods=["POST"])
def predict_match():
    if request.method == "POST":
        team1 = int(request.form["team1"])
        team2 = int(request.form["team2"])
        venue = int(request.form["venue"])
        city = int(request.form["city"])
        toss_decision = int(request.form["toss_decision"])
        toss_winner = int(request.form["toss_winner"])


data = [[team1, team2, venue, toss_winner, city, toss_decision]]
prediction = []
svm_rbf = pickle.load(open("matches_svm_rbf.pkl", "rb"))
prediction.append(svm_rbf.predict(data)[0])
svm_linear = pickle.load(open("matches_svm_linear.pkl", "rb"))
prediction.append(svm_linear.predict(data)[0])
nb = pickle.load(open("matches_nb.pkl", "rb"))
prediction.append(nb.predict(data)[0])
knn = pickle.load(open("matches_knn.pkl", "rb"))
prediction.append(knn.predict(data)[0])
teams = [
    "Mumbai Indians",
    "Kolkata Knight Riders",
    "Royal ChallengersBangalore",
    "Deccan Chargers",
    "Chennai Super Kings",
    "RajasthanRoyals",
    "Delhi Daredevils",
    "Delhi Capitals",
    "Gujarat Lions",
    "Kings XIPunjab",
    "Sunrisers Hyderabad",
    "Rising Pune Supergiants",
    "Rising PuneSupergiant",
    "Kochi Tuskers Kerala",
    "Pune Warriors",
]
venues = [
    "Rajiv Gandhi International Stadium, Uppal",
    "MaharashtraCricket Association Stadium",
    "Saurashtra Cricket Association Stadium",
    "Holkar Cricket Stadium",
    "M Chinnaswamy Stadium",
    "Wankhede Stadium",
    "Eden Gardens",
    "Feroz Shah Kotla",
    "Punjab Cricket Association IS Bindra Stadium,Mohali",
    "Green Park",
    "Punjab Cricket Association Stadium, Mohali",
    "SawaiMansingh Stadium",
    "MA Chidambaram Stadium, Chepauk",
    "Dr DY PatilSports Academy",
    "Newlands",
    "St Georges Park",
    "Kingsmead",
    "SuperSportPark",
    "Buffalo Park",
    "New Wanderers Stadium",
    "De Beers Diamond Oval",
    "OUTsurance Oval",
    "Brabourne Stadium",
    "Sardar Patel Stadium,Motera",
    "Barabati Stadium",
    "Vidarbha Cricket Association Stadium,Jamtha",
    "Himachal Pradesh Cricket Association Stadium",
    "NehruStadium",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA CricketStadium",
    "Subrata Roy Sahara Stadium",
    "Shaheed Veer Narayan SinghInternational Stadium",
    "JSCA International Stadium Complex",
    "SheikhZayed Stadium",
    "Sharjah Cricket Stadium",
    "Dubai International CricketStadium",
    "M. A. Chidambaram Stadium",
    "Feroz Shah Kotla Ground",
    "M.Chinnaswamy Stadium",
    "Rajiv Gandhi Intl. Cricket Stadium",
    "IS BindraStadium",
    "ACA-VDCA Stadium",
]
cities = [
    "Hyderabad",
    "Pune",
    "Rajkot",
    "Indore",
    "Bangalore",
    "Mumbai",
    "Kolkata",
    "Delhi",
    "Chandigarh",
    "Kanpur",
    "Jaipur",
    "Chennai",
    "CapeTown",
    "Port Elizabeth",
    "Durban",
    "Centurion",
    "East London",
    "Johannesburg",
    "Kimberley",
    "Bloemfontein",
    "Ahmedabad",
    "Cuttack",
    "Nagpur",
    "Dharamsala",
    "Kochi",
    "Visakhapatnam",
    "Raipur",
    "Ranchi",
    "Abu Dhabi",
    "Sharjah",
    "Dubai",
    "Mohali",
    "Bengaluru",
]
toss = ["Field", "Bat"]
p = dict()
p["Home Team"] = teams[team1 - 1]
p["Away Team"] = teams[team2 - 1]
p["Venue"] = venues[venue]
p["City"] = cities[city]
p["Toss Winner"] = teams[toss_winner - 1]
p["Toss Decision"] = toss[toss_decision]
if prediction[0] == 0:
    winner = teams[team1 - 1]
else:
    winner = teams[team2 - 1]
# print(p)
return render_template("predict_match.html", prediction=p, winner=winner)


@app.route("/predict_score", methods=["POST"])
def predict_score():
    if request.method == "POST":
        temp_array = list()
    batting_team = int(request.form["team1"])
    bowling_team = int(request.form["team2"])


if batting_team == 5:
    temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif batting_team == 8:
    temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif batting_team == 10:
    temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif batting_team == 2:
    temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif batting_team == 1:
    temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif batting_team == 6:
    temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif batting_team == 3:
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif batting_team == 11:
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]
if bowling_team == 5:
    temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif bowling_team == 8:
    temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif bowling_team == 10:
    temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif bowling_team == 2:
    temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif bowling_team == 1:
    temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif bowling_team == 6:
    temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif bowling_team == 3:
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif bowling_team == 11:
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]
# Overs, Runs, Wickets, Runs_in_prev_5, Wickets_in_prev_5
overs = float(request.form["over"])
runs = int(request.form["runs"])
wickets = int(request.form["wickets"])
runs_in_last_5 = int(request.form["runs_in_last_5"])
wickets_in_last_5 = int(request.form["wickets_in_last_5"])
temp_array = temp_array + [overs, runs, wickets, runs_in_last_5, wickets_in_last_5]
# Converting into numpy array
temp_array = np.array([temp_array])
linear_regressor = pickle.load(open("score_linear.pkl", "rb"))
final_score = int(linear_regressor.predict(temp_array)[0])
teams = [
    "Mumbai Indians",
    "Kolkata Knight Riders",
    "Royal ChallengersBangalore",
    "Deccan Chargers",
    "Chennai Super Kings",
    "RajasthanRoyals",
    "Delhi Daredevils",
    "Delhi Capitals",
    "Gujarat Lions",
    "Kings XIPunjab",
    "Sunrisers Hyderabad",
    "Rising Pune Supergiants",
    "Rising PuneSupergiant",
    "Kochi Tuskers Kerala",
    "Pune Warriors",
]
venues = [
    "Rajiv Gandhi International Stadium, Uppal",
    "MaharashtraCricket Association Stadium",
    "Saurashtra Cricket Association Stadium",
    "Holkar Cricket Stadium",
    "M Chinnaswamy Stadium",
    "Wankhede Stadium",
    "Eden Gardens",
    "Feroz Shah Kotla",
    "Punjab Cricket Association IS Bindra Stadium,Mohali",
    "Green Park",
    "Punjab Cricket Association Stadium, Mohali",
    "SawaiMansingh Stadium",
    "MA Chidambaram Stadium, Chepauk",
    "Dr DY PatilSports Academy",
    "Newlands",
    "St Georges Park",
    "Kingsmead",
    "SuperSportPark",
    "Buffalo Park",
    "New Wanderers Stadium",
    "De Beers Diamond Oval",
    "OUTsurance Oval",
    "Brabourne Stadium",
    "Sardar Patel Stadium,Motera",
    "Barabati Stadium",
    "Vidarbha Cricket Association Stadium,Jamtha",
    "Himachal Pradesh Cricket Association Stadium",
    "NehruStadium",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA CricketStadium",
    "Subrata Roy Sahara Stadium",
    "Shaheed Veer Narayan SinghInternational Stadium",
    "JSCA International Stadium Complex",
    "SheikhZayed Stadium",
    "Sharjah Cricket Stadium",
    "Dubai International CricketStadium",
    "M. A. Chidambaram Stadium",
    "Feroz Shah Kotla Ground",
    "M.Chinnaswamy Stadium",
    "Rajiv Gandhi Intl. Cricket Stadium",
    "IS BindraStadium",
    "ACA-VDCA Stadium",
]
cities = [
    "Hyderabad",
    "Pune",
    "Rajkot",
    "Indore",
    "Bangalore",
    "Mumbai",
    "Kolkata",
    "Delhi",
    "Chandigarh",
    "Kanpur",
    "Jaipur",
    "Chennai",
    "CapeTown",
    "Port Elizabeth",
    "Durban",
    "Centurion",
    "East London",
    "Johannesburg",
    "Kimberley",
    "Bloemfontein",
    "Ahmedabad",
    "Cuttack",
    "Nagpur",
    "Dharamsala",
    "Kochi",
    "Visakhapatnam",
    "Raipur",
    "Ranchi",
    "Abu Dhabi",
    "Sharjah",
    "Dubai",
    "Mohali",
    "Bengaluru",
]
toss = ["Field", "Bat"]
return render_template("predict_score.html", low=final_score - 6, high=final_score + 6)
if __name__ == "__main__":
    app.run()
