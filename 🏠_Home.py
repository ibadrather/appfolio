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
import os.path as osp
from streamlit.logger import get_logger
import streamlit.components.v1 as components

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Welcome",
        page_icon="👋",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # st.write("## Welcome! 👋")

    st.sidebar.success("Select a app above.")

    st.markdown(
        """
        <h1 align="center"> Hi there 👋, I'm Ibad Rather </h1>
        <h4 align="center">I'm an Engineer</h4>

<div id="header" align="center">
  <img src="https://media4.giphy.com/media/1GEATImIxEXVR79Dhk/giphy.gif" width="350"/>
</div>

<div id="header" align="left">

  <a href="https://www.linkedin.com/in/ibad-rather/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>

  <a href="https://github.com/ibadrather/">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>

  <a href="mailto:ibad.rather.ir@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>

###### Rudolf-Breitscheid-Str 27 Jena
###### 07747 Germany
###### +49-15906472860
</div>


<body> 

  I am looking for a job! If you are interested in hiring me, please contact me on LinkedIn or email me at ibad.rather.@gmail.com

  This web-app is in continious development. All the features may not work perfectly. If you find any bugs, please report them on the [GitHub repo](https://github.com/ibadrather/appfolio).
</body>

<h5 align="left">👈 You can see some of my projects in the Sidebar.</h5>


    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <h3 style="color:blue">Skills</h3>
    <body>
    <ul>
    <li> Python, C++, MATLAB, Linux </li>
    <li> PyTorch, Scikit-Learn, TensorFlow/Keras, Pytorch-Lightning </li>
    <li> Pandas, Numpy, SciPy, SymPy </li>
    <li> OpenCV, ROS, Gazebo </li>
    <li> FastAPI, Streamlit </li>
    <li> Git, Docker </li>
    <li> Leadership, Teaching </li>
    </ul>
    </body>

    <h3 style="color:blue">Experience</h3>
    <h4> Carl Zeiss AG, Jena Germany — Student Researcher </h4>
    <h6> October 2021 - PRESENT </h6>
    <ul>
    <li> Stabilized a video from an oscillating camera using Inertial Measurement Unit sensor data. </li> 
    <li> Evaluated various Neural Network architectures like Transformer, CNN, ResNet and LSTM for the use case. </li> 
    <li> Deployed models on edge hardware </li>  
    <li> Simulated the scenario using AirSim and Unreal Engine. </li> 
    </ul>
    <strong>Tech Stack</strong>: PyTorch, Pandas, NumPy, SciPy, OpenCV, Azure DevOps, ONNX, AirSim and Unreal Engine

    <h3 style="color:blue">Education</h3>
    <h4> Universität Siegen,  Germany — MS Mechatronics </h4>
    <h6> October  2019 - November 2022 </h6>
    Specialized in Deep Learning and Robotics.
    Studied software, mechanical, control, electrical and electronics engineering.

    <h4> Jamia Millia Islamia, India — B.Tech Mechanical Engineering </h4>
    <h6> August 2014 - August 2018 </h6>
    Specialized in Production Engineering and Machine Design.

    <h3 style="color:blue">Projects</h3>
    <h5> Master Project: Follow Me function in an Autonomous Delivery Robot </h5>
    Simulated a husky robot in a custom-built Gazebo world and performed SLAM. 
    
    Analyzed various SLAM algorithms.
    Made robot capable of autonomous navigation.
    
    <strong>Tech Stack</strong>: ROS, Gazebo, C++, CMAKE, Git
    """,
        unsafe_allow_html=True,
    )
    # with open(osp.join("pages", "ibad_cv.html")) as f:
    #   cv = f.read()

    # components.html(cv)


if __name__ == "__main__":
    run()
