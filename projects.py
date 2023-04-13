import streamlit as st

def app():
    st.header("My Projects :computer:")

    # Deep Learning Related Projects section
    # Deep Learning Related Projects
    st.header("Deep Learning Related Projects")

    # Person captioning in images
    st.subheader("Person captioning in images")
    st.write("- Developed a model for generating captions describing people in images.")
    st.write("- Tech Stack: Python, PyTorch, OpenCV, NumPy, Pandas, SciPy.")

    # Content based Image Retrieval (like reverse google image search)
    st.subheader("Content based Image Retrieval")
    st.write("- Developed a system for retrieving similar images based on their content.")
    st.write("- Tech Stack: Python, OpenCV, NumPy, SciPy, Matplotlib.")

    # Multivariate time-series analysis for forecasting.
    st.subheader("Multivariate time-series analysis for forecasting")
    st.write("- Developed a model for forecasting multivariate time-series data.")
    st.write("- Tech Stack: Python, TensorFlow, Scikit-Learn, NumPy, Pandas, Matplotlib.")

    # Multivariate time-series analysis for classification
    st.subheader("Multivariate time-series analysis for classification")
    st.write("- Developed a model for classifying multivariate time-series data.")
    st.write("- Tech Stack: Python, TensorFlow, Scikit-Learn, NumPy, Pandas, Matplotlib.")

    # CNNs for classification
    st.subheader("CNNs for classification")
    st.write("- Developed a model for classifying images using convolutional neural networks (CNNs).")
    st.write("- Tech Stack: Python, TensorFlow, Keras, OpenCV, NumPy.")

    # Character Level RNN for Lyrics Generation
    st.subheader("Character Level RNN for Lyrics Generation")
    st.write("- Developed a model for generating lyrics using character-level recurrent neural networks (RNNs).")
    st.write("- Tech Stack: Python, TensorFlow, Keras, NumPy, Pandas.")

    # Object Recognition on Raspberry Pi
    st.subheader("Object Recognition on Raspberry Pi")
    st.write("- Developed a system for object recognition using Raspberry Pi and camera module.")
    st.write("- Tech Stack: Python, OpenCV, NumPy, Raspberry Pi.")

    st.subheader("Project 2: Autonomous Navigation with ROS and Gazebo")
    st.write("Designed an autonomous navigation system using ROS and Gazebo simulation for a wheeled robot. This project involved developing and tuning controllers for the robot to achieve optimal navigation in a simulated environment. Implemented object detection using YOLOv3 to detect and avoid obstacles in the robot's path.")
    st.markdown("**Tech Stack**: Python, ROS, Gazebo, OpenCV, TensorFlow/Keras, NumPy, Pandas, SciPy")

    st.subheader("Project 3: Data Pipeline for Image Segmentation")
    st.write("Developed a data pipeline for image segmentation using PyTorch Lightning and NVIDIA DALI. This project involved creating a custom dataset and data loader, performing data augmentation and normalization, training a DeepLabV3+ model, and visualizing the segmentation output.")
    st.markdown("**Tech Stack**: Python, PyTorch, PyTorch Lightning, NVIDIA DALI, NumPy, Pandas, OpenCV")

