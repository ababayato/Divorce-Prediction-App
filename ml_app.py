import streamlit as st 
import os
import joblib
import numpy as np

attrib_info = """
#### Attribute Information:
    - Q3 (When we need it, we can take our discussions with my spouse from the beginning and correct it.)
    - Q6 (We don't have time at home as partners.)
    - Q15 (Our dreams with my spouse are similar and harmonious.)
    - Q17 (We share the same views about being happy in our life with my spouse.)
    - Q20 (My spouse and I have similar values in trust.)
    - Q26 (I know my spouse's basic anxities)
    - Q31 (I feel aggresive when I argue with my spouse.)
    - Q40 (We're just starting a discussion before I know what's going on)
    - Q41 (When I talk to my spouse about something, my calm suddenly breaks.)
    - Q44 (Sometimes I think it's good for me to leave home for a while.)
    - Divorce 0. No Divorce, 1. Divorce.
     All responses were collected on a 5 point scale (0=Never, 1=Seldom, 2=Averagely, 3=Frequently, 4=Always)
"""

label_dict = {"Never":0,"Seldom":1,"Averagely":2,"Frequently":3,"Always":4}
target_label_map = {"No Divorce":0,"Divorce":1}

['Q3', 'Q6', 'Q15', 'Q17', 'Q20', 'Q26', 'Q31', 'Q40', 'Q41', 'Q44', 'Divorce']

def get_fvalue(val):
      feature_dict = {"Never":0,"Seldom":1,"Averagely":2,"Frequently":3,"Always":4}
      for key,value in feature_dict.items():
              if val == key:
                      return value 

def get_value(val,my_dict):
      for key,value in my_dict.items():
              if val == key:
                      return value 

# Load ML Models
@st.cache
def load_model(model_file):
        loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
        return loaded_model


def run_ml_app():
        st.subheader("Machine Learning Section")
        loaded_model = load_model("divorce_mod.pkl")
      
        with st.expander("Attributes Info"):
                st.markdown(attrib_info,unsafe_allow_html=True)

        #layout
        col1,col2 = st.columns(2)

        with col1: 
                Q3 = st.selectbox('When we need it, we can take our discussions with my spouse from the beginning and correct it.', ("Never","Seldom","Averagely","Frequently","Always"))
                Q6 = st.selectbox("We don't have time at home as partners.", ("Never","Seldom","Averagely","Frequently","Always"))
                Q15 = st.selectbox('Our dreams with my spouse are similar and harmonious.', ("Never","Seldom","Averagely","Frequently","Always"))
                Q17 = st.selectbox("We share the same views about being happy in our life with my spouse.", ("Never","Seldom","Averagely","Frequently","Always"))
                Q20 = st.selectbox('My spouse and I have similar values in trust.', ("Never","Seldom","Averagely","Frequently","Always"))
                
        with col2:
                Q26 = st.selectbox("I know my spouse's basic anxities.", ("Never","Seldom","Averagely","Frequently","Always"))
                Q31 = st.selectbox("I feel aggresive when I argue with my spouse.", ("Never","Seldom","Averagely","Frequently","Always"))
                Q40 = st.selectbox("We're just starting a discussion before I know what's going on", ("Never","Seldom","Averagely","Frequently","Always"))
                Q41 = st.selectbox('When I talk to my spouse about something, my calm suddenly breaks.', ("Never","Seldom","Averagely","Frequently","Always"))
                Q44 = st.selectbox("Sometimes I think it's good for me to leave home for a while.", ("Never","Seldom","Averagely","Frequently","Always"))
                

        with st.expander("Your Selected Options"):
                result = {'Q3':Q3,
                'Q6':Q6,
                'Q15':Q15,
                'Q17':Q17,
                'Q20':Q20,
                'Q26':Q26,
                'Q31':Q31,
                'Q40':Q40,
                'Q41':Q41,
                'Q44':Q44}
                st.write(result)
                encoded_result = []
                for i in result.values():
                        if type(i) == int:
                                encoded_result.append(i)
                        else:
                                encoded_result.append(get_fvalue(i))
    
        with st.expander("Prediction Results"):
                single_sample = np.array(encoded_result).reshape(1,-1)
                
                prediction = loaded_model.predict(single_sample)
                pred_prob = loaded_model.predict_proba(single_sample)
                st.write(prediction)
                if prediction == 1:
                        st.warning("Divorce Risk-{}".format(prediction[0]))
                        pred_probability_score = {"Negative DM":pred_prob[0][0]*100,"Positive DM":pred_prob[0][1]}
                        st.subheader("Prediction Probability Score")
                        st.write(pred_probability_score)
		            
                else:
                        st.success("Will not Divorce-{}".format(prediction[0]))
                        pred_probability_score = {"Negative DM":pred_prob[0][0]*100,"Positive DM":pred_prob[0][1]}
                        st.subheader("Prediction Probability Score")
                        st.json(pred_probability_score)