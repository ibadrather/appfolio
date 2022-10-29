import streamlit as st
import os.path as osp
import pandas as pd
import altair as alt

#st.title("Bank Note Classification 💵")
# Set page tab display
st.set_page_config(
    page_title="Bank Note Classification 💵",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
# Bank Note Classification 💵
##### Data Set Information:

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

##### Attribute Information:

1. Variance of Wavelet Transformed image (continuous)
2. Skewness of Wavelet Transformed image (continuous)
3. Curtosis of Wavelet Transformed image (continuous)
4. Entropy of image (continuous)

##### Output:
1 - Fake Note

0 - Genuine Note
"""
)

st.markdown("---")

st.markdown("""
### Training the model
I have trained the model using a simple MLP in PyTorch. You can find the code [here](https://github.com/ibadrather/deep_projects/tree/main/FastAPI_Deployment/2_deploy_dl_app).

Then I converted the trained model to ONNX format and used it in this app. You can find the code [here](https://github.com/ibadrather/deep_projects/tree/main/FastAPI_Deployment/2_deploy_dl_app).

""")

st.markdown("---")


st.markdown(""" 
### Enter the values for the features. 👇
Let s see if the model can predict if the note is fake or not correctly.
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    variance = st.number_input("Variance")
with col2:
    skewness = st.number_input("Skewness")
with col3:
    curtosis = st.number_input("Curtosis")
with col4:
    entropy = st.number_input("Entroy")

bank_note_test_data_dir = osp.join(
    "pages", "pages_utils", "bank_note", "BankNote_Authentication_test.csv"
)

st.markdown("""
###### Test data for model testing:
I have provided some test data for you to test the model. You can use the test data to test the model.
The model has not seen this data before. 
""")
bank_note_test_df = pd.read_csv(bank_note_test_data_dir)
bank_note_test_df.columns = ["Variance", "Skewness", "Curtosis", "Entropy", "Class"]
st.dataframe(bank_note_test_df)

# chart = alt.Chart(bank_note_test_df).mark_area(opacity=0.3).encode()
# st.altair_chart(chart, use_container_width=True)
