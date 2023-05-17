import cv2
import numpy as np
import streamlit as st


def process_image():
    def preprocess(img):
        bytes_data = np.asarray(bytearray(img.read()), dtype=np.uint8)
        img = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
        return img

    def invert(img):
        img = preprocess(img)
        inv = cv2.bitwise_not(img)
        return inv

    def sketch(img):
        img = preprocess(img)
        _, sketch_img = cv2.pencilSketch(
            img, sigma_s=60, sigma_r=0.07, shade_factor=0.05
        )
        return sketch_img

    def gray(img):
        img = preprocess(img)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
        return gray_img

    def none(img):
        img = preprocess(img)
        return img

    def edges(img):
        img = preprocess(img)
        edge_img = cv2.Canny(img, 100, 200)
        edge_img = cv2.cvtColor(edge_img, cv2.COLOR_GRAY2RGB)
        return edge_img

    def cartoon(img):
        img = preprocess(img)
        numDownSamples = 2
        numBilateralFilters = 50
        img_color = img
        for _ in range(numDownSamples):
            img_color = cv2.pyrDown(img_color)
        for _ in range(numBilateralFilters):
            img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
        for _ in range(numDownSamples):
            img_color = cv2.pyrUp(img_color)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)
        img_edge = cv2.adaptiveThreshold(
            img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2
        )
        (x, y, z) = img_color.shape
        img_edge = cv2.resize(img_edge, (y, x))
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        return cv2.bitwise_and(img_color, img_edge)

    def sobel(img):
        img = preprocess(img)
        sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
        sobel = cv2.bitwise_or(sobel_x, sobel_y)
        return sobel

    def upsidedown(img):
        img = preprocess(img)
        upside_down = cv2.flip(img, 0)
        return upside_down

    def left_right(img):
        img = preprocess(img)
        left_right = cv2.flip(img, 1)
        return left_right

    def repeat(img):
        img = preprocess(img)
        w, h, _ = img.shape
        repeat = np.tile(img, (2, 2, 1))
        repeat = cv2.resize(repeat, (h, w))
        return repeat

    picture = st.camera_input("First, take a picture...")

    filters_to_funcs = {
        "No filter": none,
        "Grayscale": gray,
        "Edge Detection": edges,
        "Invert": invert,
        "Sketch": sketch,
        "Cartoon": cartoon,
        # "Sobel Edge": sobel,
        "Upside Down": upsidedown,
        "Left Right": left_right,
        "Repeat": repeat,
    }
    filters = st.selectbox("...and now, apply a filter!", filters_to_funcs.keys())

    if picture:
        st.image(filters_to_funcs[filters](picture), channels="BGR")


st.set_page_config(page_title="Image Processing", page_icon="📷")
st.markdown("# Basic Image Processing!")
st.sidebar.header("Let's play with images!")
st.write(
    """
    I have implemented some basic image processing filters using OpenCV.
    Take a picutre first and then apply a filter to it.
    Have fun!
    """
)

process_image()

# show_code(webcam_demo)
