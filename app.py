import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image

# importing the smaller apps
from eda_app import run_eda_app
from ml_app import run_ml_app

html_temp = """
		<div style="background-color:#008080;padding:5px;border-radius:5px">
		<h1 style="color:white;text-align:center;">Divorce Predict</h1>
		<h4 style="color:white;text-align:center;">Team Kubernetes </h4>
		</div>
		"""
img = Image.open("banner-7.jpg")
st.image(img)

def main():
	#st.title("Main App")
	stc.html(html_temp)

	menu = ["Home", "EDA", "ML", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":
		st.header("")
		#st.subheader("Home")
		st.write("""
			### Will your marriage be in order, or will you get divorced and seperated
			This application takes in input from users and tells the likelihood of Divorce
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App
			""")
	elif choice=="EDA":
		run_eda_app()
	elif choice == "ML":
		run_ml_app()
	else:
		st.subheader("What is it about?")
		st.text("""
        Will your marriage be in order, or will you get divorced and separated? Find out the answer
        from Machine Learning! The machine learning embedded in this application can
        determine the likelihood of divorce with very high accuracy. A dataset based on Gottman pair 
        therapy was used to build the logistic model. The dataset is publicly available. For more information about
        this dataset, see the source: Yöntem, M , Adem, K , İlhan, T , Kılıçarslan, S. (2019). DIVORCE PREDICTION
        USING CORRELATION BASED FEATURE SELECTION AND ARTIFICIAL NEURAL NETWORKS. Nevşehir Hacı Bektaş Veli 
        University SBE Dergisi, 9 (1), 259-273.
          """)

main()