import streamlit as st
import requests
from url import BASE_URL
from pages.pages_utils.language_translator.utils import get_translation_from_hf

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

    <h4>What languages are supported?</h4>
    This app supports translation from English, Dutch and German. You can translate from any of these languages to any of these languages (except Dutch-German).


    """,
    unsafe_allow_html=True,
)

st.markdown("---")

st.markdown("### Select input and output languages and enter text to translate. 👇")
option1 = st.selectbox("Input language", ("English", "Dutch", "German"))
input_text = st.text_area(
    "Enter text:",
    height=None,
    max_chars=500,
    key="input_text",
    help="Enter your text here",
)
option2 = st.selectbox("Output language", ("Dutch", "English", "German"))

api_url_translator = BASE_URL + "/translator"

if st.button("Translate Sentence"):
    if input_text == "":
        st.warning("Please **enter text** for translation")

    elif option1 == option2:
        st.warning("Please select different languages for translation")
    
    elif option1 == "Dutch" and option2 == "German":
        st.warning("Sorry, translation from Dutch to German is not available")

    else:
        with st.spinner("Loading Model and translating..."):
            if option1 == "English" and option2 == "Dutch":
                ### Make request to  API untill we get a response successfully
                translation = get_translation_from_hf(
                    input_text,
                    api_url_translator,
                    input_language="en",
                    output_language="nl",
                )

            elif option1 == "Dutch" and option2 == "English":
                translation = get_translation_from_hf(
                    input_text,
                    api_url_translator,
                    input_language="nl",
                    output_language="en",
                )

            elif option1 == "German" and option2 == "English":
                translation = get_translation_from_hf(
                    input_text,
                    api_url_translator,
                    input_language="de",
                    output_language="en",
                )
            
            elif option1 == "English" and option2 == "German":
                translation = get_translation_from_hf(
                    input_text,
                    api_url_translator,
                    input_language="en",
                    output_language="de",
                )

            elif option1 == "German" and option2 == "Dutch":
                translation = get_translation_from_hf(
                    input_text,
                    api_url_translator,
                    input_language="de",
                    output_language="nl",
                )
                
        st.text_area(
            label="Translation",
            value=translation,
            height=None,
            key="translation",
            help="Translation will appear here",
        )

        st.success("Translation successful")
else:
    pass
