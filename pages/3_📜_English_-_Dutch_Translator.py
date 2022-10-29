import streamlit as st
import requests

st.set_page_config(
    page_title="Simple Translator", layout="wide", initial_sidebar_state="expanded"
)


st.title("Language Translator :balloon:")
st.markdown(
    """
    This is a simple language translator app that uses the [Hugging Face Transformers](https://huggingface.co/transformers/) library to translate text from English to Dutch.
    """
)

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

base_url = "http://127.0.0.1:8000"
api_url = base_url + "/translate_en_nl"
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
