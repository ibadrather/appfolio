# Import Streamlit
import streamlit as st

def app():
    # Create a title with emoji
    st.title("Ibad Rather")
    st.subheader("Developer, Engineer and Researcher :robot_face:")

    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)

    # Skills and Tools in columns with emojis
    st.header("Skills & Tools :hammer_and_wrench:")

    # Create a two-column layout for Skills and Tools
    col1, col2 = st.columns(2)

    # Display Skills in the first column
    with col1:
        st.subheader("Skills :rocket:")
        skills = [
            "Deep Learning, Computer Vision, ML/DL Pipelines, ETL/ELT",
            "Data Engineering, Data & Feature Engineering, Data Validation",
            "Data Collection, Data Preprocessing, Data & Concept Drift",
            "Image Segmentation, Image Classification, Object & Change Detection",
            "Image Processing, Video Stabilization, Image Retrieval",
            "Web Deployment, Backend, Software Development, Agile Development",
            "Signal Processing, Robotics",
            "Research & Development",
        ]

        for skill in skills:
            st.write(f"- {skill}")


    # Display Tools in the second column
    with col2:
        st.subheader("Tools :wrench:")
        tools = [
            "Python, C++, MATLAB, Linux",
            "Git, Docker, FastAPI, REST",
            "PyTorch, TensorFlow/Keras, Scikit-Learn",
            "MLflow, TFDV, TFX, Optuna, Airflow",
            "Numpy, Pandas, OpenCV, SciPy",
            "ROS, Gazebo, CMAKE",
            "Heroku, AWS, Streamlit",
        ]
        for tool in tools:
            st.write(f"- {tool}")

    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)

    ## Work Experience
    st.header("Work Experience :briefcase:")

    # Freelancer - Machine Learning Engineer
    st.subheader("Machine Learning Engineer, Freelancer")
    st.write("December 2022 - Present")
    st.markdown("- Developed a comprehensive remote sensing library that includes classical image segmentation, deep image segmentation, scene classification, and change detection, making it easier for researchers and practitioners to detect changes in rural areas.")
    st.markdown("- Developed a human activity recognition system for indoor localization for a university.")
    st.markdown("- Achieved state-of-the-art performance in medical image segmentation.")
    st.markdown("**Tech Stack**: Python, PyTorch, Scikit-Learn, Pandas, NumPy, Matplotlib")

    # Carl Zeiss AG - Student Researcher
    st.subheader("Carl Zeiss AG, Jena Germany — Student Researcher")
    st.write("October 2021 - November 2022")
    st.markdown("- Developed digital video stabilization algorithm using an Inertial Measurement Unit (IMU) to compensate for oscillating camera motion with high precision requirements of 0.1 mm.")
    st.markdown("- Conducted extensive evaluation and comparison of deep learning architectures and classical algorithms for both pose-estimation and motion prediction using IMU sensor data, achieving high accuracy and performance with a variety of neural networks (including Transformers, CNNs, and RNNs).")
    st.markdown("- Investigated and evaluated various simulation platforms (Epic Games Unreal Engine, Microsoft AirSim, Nvidia Omniverse) for camera and sensor simulation to create realistic and accurate simulation environments.")
    st.markdown("**Tech Stack**: Python, PyTorch, OpenCV, NumPy, Pandas, SciPy, ONNX, PyThea, AirSim, Unreal Engine, SymPy")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Mechatronics
    st.subheader("Universität Siegen, Germany — M.Sc. Mechatronics")
    st.write("October 2019 - November 2022")
    st.markdown("Developed expertise in the areas of Deep Learning and Robotics. Possess a background in software, mechanical, control, electrical, and electronics engineering.")

    # Mechanical Engineering
    st.subheader("Jamia Millia Islamia, India — B.Tech. Mechanical Engineering")
    st.write("August 2014 - August 2018")
    st.markdown("Specialized in Production Engineering and Machine Design.")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Awards section
    st.header("Awards :trophy:")
    st.subheader("Hackathon Winner: HackaTUM 2022")
    st.write("Won the Optiver track in which we had to develop a trading bot on a simulated stock market.")

    st.markdown("<hr>", unsafe_allow_html=True)


    # Certificates section
    st.header("Certificates :scroll:")
    certificates = [
        "Machine Learning",
        "Data Engineer Project",
        "Convolutional Neural Networks (CNNs) - TensorFlow",
        "Data Analysis with Python",
        "Robotics Software Engineer Nanodegree (Udacity)",
    ]

    for certificate in certificates:
        st.write(f"- {certificate}")

    st.markdown("<hr>", unsafe_allow_html=True)


    # Create a two-column layout for Languages and Location
    col1, col2 = st.columns(2)

    # Display Languages in the first column
    with col1:
        st.subheader("Languages :speaking_head_in_silhouette:")
        languages = [
            "English (C1)",
            "Urdu (Native)",
            "Hindi (Native)",
            "German (A1)"
        ]

        for language in languages:
            st.markdown(f"- {language}")

    # Display Location in the second column
    with col2:
        st.subheader("Location :round_pushpin:")
        location = "Germany"
        st.markdown(location)

        # Optionally, display the country flag emoji
        st.markdown(":de:", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Contact Information section
    st.header("Contact Information :mailbox:")

    # Create a two-column layout for the address and other contact details
    col1, col2 = st.columns(2)

    # Display the address in the first column
    with col1:
        st.subheader("Address :house:")
        address = [
            "Rudolf-Breitscheid-Str 27",
            "Jena, 07747, Germany"
        ]

        for line in address:
            st.markdown(line)

    # Display the phone number and email in the second column
    with col2:
        st.subheader("Phone :telephone_receiver:")
        phone = "+49-15906472860"
        st.markdown(phone)

        st.subheader("Email :envelope:")
        email = "ibad.rather.ir@gmail.com"
        st.markdown(email)

    # Display a fun background color
    st.markdown(
        """
        <style>
        body {
            background-color: #5fe6f5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
