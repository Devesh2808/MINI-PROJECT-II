def accuracy_of_model(trained_model, data, predictors, outcome):predictions = trained_model.predict(data[predictors])
accuracy = metrics.accuracy_score(predictions,data[outcome])
print('Accuracy : %s' % '{0:.3%}'.format(accuracy))
import pandas as pd
import numpy as np
import pickle
from sklearn import metrics
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import plot_confusion_matrix
data = pd.read_csv('./IPL Matches Dataset 2021.csv')
columns = ['team1', 'team2', 'venue','toss_winner','city','toss_decision','winner']
data = data[columns]
data.replace(['Mumbai Indians','Kolkata Knight Riders','Royal ChallengersBangalore','Deccan Chargers','Chennai Super Kings','Rajasthan Royals','Delhi Daredevils',"Delhi Capitals",'GujaratLions','Punjab Kings','Sunrisers Hyderabad','Rising Pune Supergiants',"Rising PuneSupergiant",'Kochi Tuskers Kerala','Pune Warriors'],['MI','KKR','RCB','DC','CSK','RR','DD','DD','GL','KXIP','SRH','RPS','RPS','KTK','PW'],inplace=True)
encode = {'team1':{'MI':1,'KKR':2,'RCB':3,'DC':4,'CSK':5,'RR':6,'DD':7,'GL':8,'KXIP':9,'SRH':10,'RPS':11,'KTK':12,'PW':13},'team2':{'MI':1,'KKR':2,'RCB':3,'DC':4,'CSK':5,'RR':6,'DD':7,'GL':8,'KXIP':9,'SRH':10,'RPS':11,'KTK':12,'PW':13},'toss_winner':{'MI':1,'KKR':2,'RCB':3,'DC':4,'CSK':5,'RR':6,'DD':7,'GL':8,'KXIP':9,'SRH':10,'RPS':11,'KTK':12,'PW':13},'winner':{'MI':1,'KKR':2,'RCB':3,'DC':4,'CSK':5,'RR':6,'DD':7,'GL':8,'KXIP':9,'SRH':10,'RPS':11,'KTK':12,'PW':13,'Draw':14},'city':{'Hyderabad':0,'Pune':1,'Rajkot':2,'Indore':3,'Bangalore':4,'Mumbai':5,'Kolkata':6,'Delhi':7,'Chandigarh':8,'Kanpur':9,'Jaipur':10,'Chennai':11,'Cape Town':12,'Port Elizabeth':13,'Durban':14,'Centurion':15,'EastLondon':16,'Johannesburg':17,'Kimberley':18,'Bloemfontein':19,'Ahmedabad':20,'Cuttack':21,'Nagpur':22,'Dharamsala':23,'Kochi':24,'Visakhapatnam':25,'Raipur':26,'Ranchi':27,'AbuDhabi':28,'Sharjah':29,'Dubai':30,'Mohali':31,'Bengaluru':32},'venue':{'Rajiv Gandhi International Stadium, Uppal':0,'MaharashtraCricket Association Stadium':1,'Saurashtra Cricket AssociationStadium':2,'Holkar Cricket Stadium':3,'M ChinnaswamyStadium':4,'Wankhede Stadium, Mumbai':5,'Eden Gardens':6,'Feroz ShahKotla':7,'Punjab Cricket Association IS Bindra Stadium, Mohali':8,'GreenPark':9,'Punjab Cricket Association Stadium, Mohali':10,'Sawai MansinghStadium':11,'MA Chidambaram Stadium, Chepauk, Chennai':12,'Dr DYPatil Sports Academy':13,'Newlands':14,'St GeorgesPark':15,'Kingsmead':16,'SuperSport Park':17,'Buffalo Park':18,'NewWanderers Stadium':19,'De Beers Diamond Oval':20,'OUTsuranceOval':21,'Brabourne Stadium':22,'Narendra Modi Stadium,Ahmedabad':23,'Barabati Stadium':24,'Vidarbha Cricket AssociationStadium, Jamtha':25,'Himachal Pradesh Cricket AssociationStadium':26,'Nehru Stadium':27,'Dr. Y.S. Rajasekhara Reddy ACA-VDCACricket Stadium':28,'Subrata Roy Sahara Stadium':29,'Shaheed VeerNarayan Singh International Stadium':30,'JSCA International StadiumComplex':31,'Sheikh Zayed Stadium':32,'Sharjah CricketStadium':33,'Dubai International Cricket Stadium':34,'M. A. ChidambaramStadium':35,'Feroz Shah Kotla Ground':36,'M. ChinnaswamyStadium':37,'Rajiv Gandhi Intl. Cricket Stadium':38,'IS BindraStadium':39,'ACA-VDCA Stadium':40},'toss_decision':{'field':0,'bat':1}}
data.replace(encode, inplace=True)
for i in range(len(data)):
    if data['winner'][i]==data['team1'][i]:
        data['winner'][i]=0
    else:
        data['winner'][i]=1
svm_rbf = pickle.load(open('matches_svm_rbf.pkl', 'rb'))
svm_linear = pickle.load(open('matches_svm_linear.pkl', 'rb'))
nb = pickle.load(open('matches_nb.pkl', 'rb'))
knn = pickle.load(open('matches_knn.pkl', 'rb'))
# #SVM Linear
outcome_var=["winner"]
predictor_var = ['team1', 'team2', 'venue','toss_winner','city','toss_decision']
print("\nSVM Linear")
accuracy_of_model(svm_linear , data , predictor_var, outcome_var)
print("\nSVM RBF")
accuracy_of_model(svm_rbf , data , predictor_var, outcome_var)
print("\nNaive Bayes")
accuracy_of_model(nb , data , predictor_var, outcome_var)
print("\nKNN")
accuracy_of_model(knn , data , predictor_var, outcome_var)