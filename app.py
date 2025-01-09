import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]

    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    
    return " ".join(y)


tk = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))


# Custom CSS for Colors and Style
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #1f4037, #99f2c8);
        color: #ffffff;
    }
    .css-1lcbmhc {
        background-color: transparent;
    }
    input[type="text"]  {
        background-color: #ffffff;
        color: #000000;
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #cccccc;
        font-size: 16px;
    }
    .stButton > button {
        background-color: #4caf50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-size: 18px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .st-header {
        text-align: center;
        color: #ffcc00;
        font-size: 24px;
        margin-bottom: 10px;
        text-shadow: 2px 2px 5px black;
    }
    .st-title {
        font-size: 30px;
        text-shadow: 2px 2px 10px black;
    }
    .colored-card {
        background-color: #ff5722;
        color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Option Menu with Colors
selected = option_menu(
    menu_title=None,
    options=["Home", "Detect SMS Spam", "About"],
    icons=['house', 'envelope', 'info-circle'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "5px", "background-color": "#2c3e50"},
        "icon": {"color": "orange", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "color": "white",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#ff5722",
        },
        "nav-link-selected": {"background-color": "#e74c3c"},
    },
)

# Pages
if selected == "Home":
    st.title("Welcome to the SMS Spam Detection App Using NLP 🎉")
    st.write(
        """
        <div class="colored-card">
            <h2>Navigate to the 'Detect SMS Spam' tab to check if an SMS is spam or not!</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif selected == "Detect SMS Spam":
    st.title("SMS Spam Detection 🚨")

    input_sms = st.text_input("Enter the SMS")
    if st.button("Predict"):
        if input_sms.strip():
            # Preprocess and Predict
            transformed_sms = transform_text(input_sms)
            vector_input = tk.transform([transformed_sms])
            result = model.predict(vector_input)[0]
            # Display Result
            if result == 1:
                st.success("This is a SPAM message! 🚫")
            else:
                st.success("This is NOT a Spam message! ✅")
        else:
            st.warning("Please enter a valid SMS!")

elif selected == "About":
    st.title("About the SMS Spam Detection App 💡")
    st.markdown(
        """
        <div class="colored-card">
            <ul>
                <li>Collected and preprocessed SMS data from Kaggle.</li>
                <li>Trained and selected the best model with 100% precision.</li>
                <li>Conducted exploratory data analysis for insights.</li>
                <li>Utilized Natural Language Processing (NLP) techniques.</li>
                <li>Deployed the model on Streamlit for real-time spam detection.</li>
                <li>Created a user-friendly web app interface.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("<h4>✨ Made by Abhishek Hendge ✨</h4>", unsafe_allow_html=True)

