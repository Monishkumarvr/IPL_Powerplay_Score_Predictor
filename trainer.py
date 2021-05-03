import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_excel("PP_Data.xlsx")



RF1 = RandomForestClassifier()
RF2 = RandomForestClassifier()

X = df[["venue1", "innings", "batting_team1", "Chennai Super Kings", "Delhi Capitals", "Kolkata Knight Riders", "Mumbai Indians", "Punjab Kings",
      "Rajasthan Royals", "Royal Challengers Bangalore", "Sunrisers Hyderabad"]]
Y1 = df[["total_runs"]]
Y2 = df[["wickets"]]

RF1.fit(X, Y1.values.ravel())
RF2.fit(X, Y2.values.ravel())

joblib.dump(RF1, 'model1.joblib')
joblib.dump(RF2, 'model2.joblib')
