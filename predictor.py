import streamlit as st
import pandas as pd
import joblib

def predictRuns(v, bat_team, bow_team, inn):

    #runs = 0
    #wickets = 0
    t1, t2, t3, t4, t5, t6, t7, t8 = 0, 0, 0, 0, 0, 0, 0, 0
    ven = int(v)
    b_team = int(bat_team)
    inng = int(inn)

    if int(bow_team) == 0:
        t1 = 1
        t2, t3, t4, t5, t6, t7, t8 = 0, 0, 0, 0, 0, 0, 0
    elif int(bow_team) == 3:
        t4 = 1
        t1, t2, t3, t5, t6, t7, t8 = 0, 0, 0, 0, 0, 0, 0
    elif int(bow_team) == 1:
        t2 = 1
        t1, t3, t4, t5, t6, t7, t8 = 0, 0, 0, 0, 0, 0, 0
    elif int(bow_team) == 2:
        t3 = 1
        t1, t2, t4, t5, t6, t7, t8 = 0, 0, 0, 0, 0, 0, 0
    elif int(bow_team) == 4:
        t5 = 1
        t2, t3, t4, t1, t6, t7, t8 = 0, 0, 0, 0, 0, 0, 0
    elif int(bow_team) == 5:
        t6 =1
        t2, t3, t4, t5, t1, t7, t8 = 0, 0, 0, 0, 0, 0, 0
    elif int(bow_team) == 6:
        t7 = 1
        t2, t3, t4, t5, t6, t1, t8 = 0, 0, 0, 0, 0, 0, 0
    elif int(bow_team) == 7:
        t8 = 1
        t2, t3, t4, t5, t6, t7, t1 = 0, 0, 0, 0, 0, 0, 0
    
    
    
    
    x1 = {0:ven, 1:inng, 2:b_team, 3:t1, 4:t2, 5:t3,
      6:t4, 7:t5, 8:t6, 9:t7, 10:t8}
    x1 = pd.DataFrame(x1, index = [0,])


    model1 = joblib.load('model1.joblib')
    #model2 = joblib.load('model2.joblib')
    runs = model1.predict (x1)
    #wickets = model2.predict(x1)
    runs = int(runs[0])
    #wickets = int(wickets[0])
    #score = [runs, wickets]
    return runs



st.title("IPL Powerplay Score Predictor")

st.markdown("Enter\n\nMA Chidambaram Stadium = 9\n\nWankhede Stadium = 17\n\nNarendra Modi Stadium = 11\n\nArun Jaitley Stadium = 0")
venue = st.text_input("Venue")
st.markdown("Enter\n\nChennai Super Kings = 0\n\nDelhi Capitals = 1\n\nKolkata Knight Riders = 2\n\nMumbai Indians = 3\n\nPunjab Kings = 4\n\nRajasthan Royals = 5\n\nRoyal Challengers Bangalore = 6\n\nSunrisers Hyderabad = 7")
batting_team = st.text_input("Batting Team")
bowling_team = st.text_input("Bowling Team")
st.markdown("Enter\n\nFirst Innings = 0\n\nSecond Innings = 1")
innings = st.text_input("Innings")

if st.button("Predict"):
    result = predictRuns(venue, batting_team, bowling_team, innings)
    #r = result[0]
    #w = result[1]
    st.success("The PP score: "+ str(result))
