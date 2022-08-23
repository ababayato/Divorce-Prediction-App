import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px


def run_eda_app():
				st.subheader("Exploratory Data Analysis")

				submenu = st.sidebar.selectbox("Submenu", ["Descriptive","Plots"])



				df = pd.read_csv("divorce_data-1.csv")
				freq = pd.read_csv("perc_of_answers.csv")
    
				if submenu == "Descriptive":
								st.dataframe(df)
    
								with st.expander("Summary"):
												st.dataframe(df.describe())
            
								with st.expander("Data Types"):
												st.dataframe(df.dtypes)
            
								with st.expander("Divorce Distribution"):
												st.dataframe(df["Divorce"].value_counts())
            
				elif submenu == "Plots":
								st.subheader("Visualization Plots")

								with st.expander("Plots based on Divorce"):
												fig = plt.figure()
												sns.countplot(df['Divorce'])
												st.pyplot(fig)

												divorce_df = df['Divorce'].value_counts()
												divorce_df = divorce_df.reset_index()
												divorce_df.columns = ["Divorce","Count"]
												#st.dataframe(divorce_df)

								with st.expander("Plots based Positive and Negative Answers"):
												fig = plt.figure(figsize=(4,4))
												plt.pie(freq['0'], autopct='%1.1f%%',labels=['Negative','Positive'])
												st.pyplot(fig)
												