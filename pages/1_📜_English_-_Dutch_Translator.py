import streamlit as st
import requests
from url import BASE_URL

st.set_page_config(
    page_title="Simple Translator", layout="wide", initial_sidebar_state="expanded"
)


st.title("Language Translator :balloon:")
st.markdown(
    """
    This is a simple language translator app that uses the [Hugging Face Transformers](https://huggingface.co/transformers/) library API to translate text from English to Dutch.

    The front-end is built using [Streamlit](https://streamlit.io/) and the back-end is written in FastAPI and deployed on [Heroku](https://www.heroku.com/).
    
    This app is in continious development. All the features may not work perfectly. If you find any bugs, please report them on the [GitHub repo](https://github.com/ibadrather/appfolio).

    <body>
    <h3>How to use this app?</h3>
    <ol>
    <li>Enter the text you want to translate in the text box.</li>
    <li>Click on the translate button.</li>
    <li>Wait for the translation to appear.</li>
    </ol>
    <strong>Note</strong>: It may take some time for the first translation to appear (Upto 20 seconds according to Hugging Face API), as the model is loaded into memory.
    </body>

    """, unsafe_allow_html=True,)

st.markdown("---")

st.markdown("### Enter some text in English to translate to Dutch. 👇")
input_text = st.text_area(
    "Enter text:",
    height=None,
    max_chars=500,
    key="input_text",
    help="Enter your text here",
)


# option1 = st.selectbox("Input language", ("English",))
# option2 = st.selectbox("Output language", ("Dutch",))

api_url = BASE_URL + "/translate_en_nl"

if st.button("Translate Sentence"):
    if input_text == "":
        st.warning("Please **enter text** for translation")

    else:
        with st.spinner("Loading Model and translating..."):
            ### Make request to  API untill we get a response successfully
            while True:
                try:
                    res = requests.post(api_url, json={"text": input_text})
                    # We first check if the response is valid
                    translation = res.json()[0]["translation_text"]
                    # If the response is valid, we break out of the loop
                    if res.status_code == 200:
                        break
                except:
                    pass

            st.markdown("### Translation in Dutch:")
            st.write(translation)
            st.success("Translation successful")
            st.success("Translation is **successfully** completed!")
            # st.balloons()
else:
    pass
