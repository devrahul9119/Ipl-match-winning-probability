import streamlit as st
import pandas as pd
import pickle
teams = ['Royal Challengers Bangalore',
         'Kings XI Punjab',
         'Mumbai Indians',
         'Kolkata Knight Riders',
         'Rajasthan Royals',
         'Chennai Super Kings',
         'Sunrisers Hyderabad',
          'Delhi Capitals']

city_names = ['Bangalore', 'Mumbai', 'Delhi', 'Indore', 'Nagpur', 'Ahmedabad',
       'Chandigarh', 'Hyderabad', 'Cuttack', 'Jaipur', 'Sharjah',
       'Kolkata', 'Pune', 'Chennai', 'Abu Dhabi', 'Dubai',
       'Visakhapatnam', 'Raipur', 'Bengaluru', 'Dharamsala', 'Ranchi']

pipe = pickle.load(open('pipe.pkl','rb'))
st.markdown("<h1 style='text-align: center;'>IPL Win Probability</h1>", unsafe_allow_html=True)

col1,col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team',sorted(teams))

if batting_team == bowling_team :
    st.error('Choose diffrent teams')

city = st.selectbox('Select city',sorted(city_names))
target = st.number_input('Target')

col1,col2,col3 = st.columns(3)
with col1 :
    score = st.number_input('Score')
with col2 :
    wickets = st.number_input('Wickets')
with col3 :
    overs = st.number_input('Overs completed ')

if st.button('Predict Probability'):
    runs_left = target - score
    wickets = 10 - wickets
    balls_left = 120 -(overs*6)
    current_run_rate = score/overs
    req_run_rate = (runs_left*6)/balls_left

    df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],
                  'current_run_rate':[current_run_rate],'req_run_rate':[req_run_rate],'total_runs_x':[target]})

    result = pipe.predict_proba(df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + ' ' + str(round(win*100))+'%')
    st.header(bowling_team + ' '+ str(round(loss*100))+'%')


