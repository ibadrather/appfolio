# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Welcome",
        page_icon="👋",
    )

    # st.write("## Welcome! 👋")

    st.sidebar.success("Select a app above.")

    st.markdown(
        """
        <h1 align="center"> Hi there 👋, I'm Ibad Rather </h1>
        <h4 align="center">I'm a Machine Learning Engineer and a Robotics Enthusiast.</h4>

<div id="header" align="center">
  <img src="https://media4.giphy.com/media/1GEATImIxEXVR79Dhk/giphy.gif" width="350"/>
</div>

<div id="header" align="center">

  <a href="https://www.linkedin.com/in/ibad-rather/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
</div>

<h5 align="center">👈 You can see some of my projects in the Sidebar.</h5>

<body> 
  I am looking for a job! If you are interested in hiring me, please contact me on LinkedIn or email me at ibad.rather.@gmail.com
</body>

    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    run()
