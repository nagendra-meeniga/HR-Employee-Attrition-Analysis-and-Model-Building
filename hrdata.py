import streamlit as st
import pandas as pd
import pickle
st.title("Welcome to HR Data Development")
st.sidebar.header('User Input Parameters')

def user_input():
    bt = st.sidebar.selectbox('Business_Travel',('Travel_Rarely','Travel_Frequently','Non-Travel'))
    cab = st.sidebar.selectbox('CF_age_band',('Under 25','25 - 34','35 - 44','45 - 54','Over 55'))
    dp = st.radio("The department in which the employee works.",["Sales","R&D","HR"])
    ef = st.sidebar.selectbox('Education_Field',('Life Sciences','Medical','Marketing','Technical Degree',
                                                 'Other','Human Resources'))
    jr = st.sidebar.selectbox('Job_Role',('Sales Executive','Research Scientist','Laboratory Technician',
                                          'Manufacturing Director','Healthcare Representative','Manager',
                                          'Sales Representative','Research Director','Human Resources'))
    ms = st.sidebar.selectbox('Marital_Status',('Single','Married','Divorced'))
    ot = st.sidebar.selectbox('Over_Time',('Yes','No'))
    
    ttly = st.sidebar.number_input("Training_Times_Last_Year",min_value=0,max_value=30,step=1)
    
    age = st.sidebar.number_input("Age",min_value=18,max_value=60,step=1)
    
    dr = st.slider("Daily_Rate",min_value=0,max_value=2000,step=1)
    
    dfh = st.sidebar.number_input("Distance_From_Home",min_value=0,max_value=70,step=1)
    
    es = st.sidebar.selectbox('Environment_Satisfaction',(1,2,3,4,5))
    
    hr = st.slider("Hourly_Rate",min_value=0,max_value=200,step=1)
    
    ji = st.radio("Level of involvement in the job.",[1,2,3,4,5],captions=["Low Job Involvement","Moderate Job Involvement",
                                                                          "Average/Normal Job Involvement","High level Job Involvement",
                                                                          "Very High level Job Involvement"])
    jl = st.sidebar.selectbox('Job_Level',(1,2,3,4,5)) 
    js = st.sidebar.selectbox('Job_Satisfaction',(1,2,3,4,5))
    
    mi = st.slider("Monthly_Income",min_value=1000,max_value=35000,step=1)
    mr = st.slider("Monthly_Rate",min_value=1500,max_value=35000,step=1)
    
    ncw = st.sidebar.number_input("Num_Companies_Worked",min_value=0,max_value=15,step=1)
    psh = st.sidebar.number_input("Percent_Salary_Hike",min_value=8,max_value=35,step=1)
    
    rs = st.sidebar.selectbox('Relationship_Satisfaction',(1,2,3,4,5))
    sol = st.sidebar.selectbox('Stock_Option_Level',(1,2,3,4,5))
    
    twy = st.sidebar.number_input("Total_Working_Years",min_value=0,max_value=40,step=1)
    
    wlb = st.sidebar.selectbox('Work_Life_Balance',(1,2,3,4,5))
    
    yc = st.sidebar.number_input("Years_At_Company",min_value=0,max_value=40,step=1)
    ycr = st.sidebar.number_input("Years_In_Current_Role",min_value=0,max_value=40,step=1)
    yslp = st.sidebar.number_input("Years_Since_Last_Promotion",min_value=0,max_value=25,step=1)
    ywcm = st.sidebar.number_input("Years_With_Curr_Manager",min_value=0,max_value=40,step=1)
    
    
    data = {'Business_Travel' : bt,
              'CF_age_band' : cab,
              'Department' : dp,
              'Education_Field' : ef,
              'Job_Role' : jr,
              'Marital_Status' : ms,
              'Over_Time' : ot,
              'Training_Times_Last_Year' : ttly,
              'Age' : age,
              'Daily_Rate' : dr,
              'Distance_From_Home' : dfh,
              'Environment_Satisfaction' : es,
              'Hourly_Rate' : hr,
              'Job_Involvement' : ji,
              'Job_Level' : jl,
              'Job_Satisfaction' : js,
              'Monthly_Income' : mi, 
              'Monthly_Rate' : mr,
              'Num_Companies_Worked' : ncw,
              'Percent_Salary_Hike' : psh,
              'Relationship_Satisfaction' : rs,
              'Stock_Option_Level' : sol,
              'Total_Working_Years' : twy,
              'Work_Life_Balance' : wlb,
              'Years_At_Company' : yc,
              'Years_In_Current_Role' :ycr,
              'Years_Since_Last_Promotion' : yslp,
              'Years_With_Curr_Manager' : ywcm}
    
    features = pd.DataFrame(data,index=[0])
    return features

df = user_input()
st.write(df)

with open(file="HR_Data_Set_final_model.sav",mode="rb") as a1:
    model = pickle.load(a1)
    
prediction = model.predict(df)

st.subheader('Predicted Result')

st.write(prediction)
st.write(prediction[0])
