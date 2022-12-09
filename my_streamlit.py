# -*- coding: utf-8 -*-
"""my_streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16wi9B-kY8awS0mRxN-aYhXxb1CWksWxU
"""

import skimage
from skimage.color import rgb2gray
from skimage import img_as_ubyte
import imutils
from skimage import io, filters, feature
import cv2
import streamlit as st
import numpy as np


 
# vars
DEMO_IMAGE = 'demo.jpg' # a demo image for the segmentation page, if none is uploaded
favicon = 'favicon.png'
# main page
st.set_page_config(page_title='Otsu Segmentaion - Yovel Rodoy', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')
st.title('Otsu Segmentaion - By Yovel Rodoy')

# side bar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] . div:first-child{
        width: 350px
    }
    
    [data-testid="stSidebar"][aria-expanded="false"] . div:first-child{
        width: 350px
        margin-left: -350px
    }    
    </style>
    
    """,
    unsafe_allow_html=True,


)

st.sidebar.title('Segmentation Sidebar')
st.sidebar.subheader('Site Pages')

# using st.cache so streamlit runs the following function only once, and stores in chache (until changed)
@st.cache()

# take an image, and return a resized that fits our page
def image_resize(image, width=None, height=None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = width/float(w)
        dim = (int(w*r),height)
    
    else:
        r = width/float(w)
        dim = (width, int(h*r))
        
    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)
    
    return resized

# add dropdown to select pages on left
app_mode = st.sidebar.selectbox('David',
                                  ['Moshe', 'Segment an Image'])

# Run image
if app_mode == 'Segment an Image':
    
    st.sidebar.markdown('---') # adds a devider (a line)
    
    # side bar
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] . div:first-child{
            width: 350px
        }

        [data-testid="stSidebar"][aria-expanded="false"] . div:first-child{
            width: 350px
            margin-left: -350px
        }    
        </style>

        """,
        unsafe_allow_html=True,


    )

# choosing a sigma value (either with +- or with a slider)
sigma_value = st.sidebar.number_input('Insert Sigma value', value=1, min_value = 1) # asks for input from the user
st.sidebar.markdown('---') # adds a devider (a line)
    
# read an image from the user
img_file_buffer = st.sidebar.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
# assign the uplodaed image from the buffer, by reading it in
if img_file_buffer is not None:
  image = io.imread(img_file_buffer)
else: # if no image was uploaded, then segment the demo image
  demo_image = DEMO_IMAGE
  image = io.imread(demo_image)

# display on the sidebar the uploaded image
st.sidebar.text('Original Image')
st.sidebar.image(image)

# call the function to segment the image


# Display the result on the right (main frame)
st.subheader('Output Image')

