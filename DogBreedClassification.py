import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import image
from IPython.display import Image, display
from streamlit_option_menu import option_menu
import streamlit as st
from tensorflow.keras.applications import imagenet_utils

st.title('Dog Image Classification App')
st.markdown('''
<style>
div.css-14xtw13.e8zbici0{
  display:none;
  visibility:none;
}
.css-1dp5vir.e8zbici1{
  background-image:linear-gradient(90deg, rgb(255, 255, 255), rgb(255, 255, 255));
}
.css-1q1n0ol.egzxvld0{
  display:none;
  visibility:none;
}
</style>
''', unsafe_allow_html=True)
selected = option_menu(
    menu_title="Main Menu",
    options=['Take Camera', 'Browse File'],
    icons=['steam', 'yin-yang'],
    menu_icon='cast',
    default_index=0,
    orientation="horizontal"
)
if selected == "Take Camera":
    image1 = st.camera_input('Take a photo')
    if image1:
        st.image(image1)
        mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()
        img = image.load_img(image1, target_size=(224, 224))
        resized_img = image.img_to_array(img)
        final_img = np.expand_dims(resized_img, axis=0)
        final_img = tf.keras.applications.mobilenet_v2.preprocess_input(final_img)
        prediction = mobile.predict(final_img)
        result = imagenet_utils.decode_predictions(prediction)
        numpy_result = np.array(result)
        label = numpy_result[0][0][1]
        accuracy = float(numpy_result[0][0][2])
        # st.write(f'Dog breed type:{label}')
        # st.write(f'Score Result:{accuracy*100}')
        st.markdown(f''' ### Dog breed type: {label}''')
        st.markdown(f''' ### Prediction score Result: {accuracy * 100}%''')

elif selected == "Browse File":
    image2 = st.file_uploader("upload file", 'jpg')
    if image2 is not None:
        st.image(image2)
        mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()
        img = image.load_img(image2, target_size=(224, 224))
        resized_img = image.img_to_array(img)
        final_img = np.expand_dims(resized_img, axis=0)
        final_img = tf.keras.applications.mobilenet_v2.preprocess_input(final_img)
        prediction = mobile.predict(final_img)
        result = imagenet_utils.decode_predictions(prediction)
        numpy_result = np.array(result)
        label = numpy_result[0][0][1]
        accuracy = float(numpy_result[0][0][2])
        # st.write(f'Dog breed type: {label}')
        # st.write(f'Score Result: {accuracy*100}')
        st.markdown(f''' ### Dog breed type: {label}''')
        st.markdown(f''' ### Prediction score Result: {accuracy * 100}%''')

    else:
        st.info("Waiting for file to be uploaded")