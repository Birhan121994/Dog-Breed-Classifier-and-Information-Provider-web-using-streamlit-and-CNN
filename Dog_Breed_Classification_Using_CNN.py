# Importing the most important liberaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.metrics import structural_similarity
import wikipedia
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st
from tensorflow.keras.applications import imagenet_utils
from IPython.display import Image
import streamlit.components.v1 as com
import sqlite3



st.sidebar.header('Dog Breed Classifier web app')
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Browse File', 'Take Camera'],
        icons=['steam', 'yin-yang'],
        menu_icon='cast',
        default_index=0,
        orientation="vertical"
    )

if selected == "Browse File":

    file_uploader = st.file_uploader("Upload an image file",'.jpg')

    if file_uploader is not None:
        loaded_model = tf.keras.models.load_model('C:/Users/GL/PycharmProjects/VirtualAssistant/DBC.h5')
        img1 = image.load_img(file_uploader, target_size=(224, 224))
        img2 = image.load_img(file_uploader)

        test_image = image.img_to_array(img1)
        test_image = np.expand_dims(test_image, axis=0)
        images = np.vstack([test_image])
        val = loaded_model.predict(images)

        st.write('---')
        col1, col2 = st.columns(2)
        with col1:
            st.image(img2)
            st.write('---')
            array = np.array(val)
            if array[0][0]==1:
                with st.expander('Size'):
                    st.markdown('''#### 30 to 32 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][1] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][2] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][3] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][4] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][5] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][6] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][7] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][8] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
            elif array[0][9] == 1:
                with st.expander('Size'):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown("Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown("The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown("The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown("The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
        with col2:
            array = np.array(val)

            if array[0][0] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }
                    
                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    
                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    
                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>
                
                <div class="info_div">
                    <h3 class="Dog_name">Scottish Deerhound</h3>
                    <p class="Description">
                        The Scottish Deerhound, or simply the Deerhound, is a large breed of sighthound,
                         once bred to hunt the red deer by coursing. In outward appearance, the Scottish Deerhound 
                         is similar to the Greyhound, but larger and more heavily boned with a rough-coat.
                    </p>
                    
                    <h4 class="tx1">Life Expectancy: 8-11 years.</h4>
                    <h4 class="tx2">Temperament: Dignified, Docile, Friendly, Gentle</h4>
                    <h4 class="tx3">Hypoallergenic: No</h4>
                    <h4 class="tx4">Origin: Scotland</h4>
                    <h4 class="tx5">Weight: Male: 39–50 kg, Female: 34–43 kg</h4>
                    <h4 class="tx6">Colors: Brindle, Fawn, Red Fawn, Blue, Grey, Yellow</h4>
                    <h4 class="tx7">The Kennel Club: standard</h4>
                </div>
                """, width=450, height=400)
                st.write('---')
                query1 = "Scottish Deerhound"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1','Related Dog image 2','Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[5])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])


            elif array[0][1] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Maltese Dog</h3>
                    <p class="Description">
                    Maltese dog refers both to an ancient variety of dwarf canine from Italy and generally associated also with the island of Malta, and to a modern breed of dog in the toy group. 
                    The contemporary variety is genetically related to the Bichon, Bolognese, and Havanese breeds.
                    </p>

                    <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                    <h4 class="tx2">Temperament: Playful, Docile, Easygoing, Intelligent, Lively,</h4>
                    <h4 class="tx3">Hypoallergenic: Yes</h4>
                    <h4 class="tx4">Origin: Italy, Mediterranean Basin</h4>
                    <h4 class="tx5">Weight: Male: 21–25 cm, Female: 20–23 cm</h4>
                    <h4 class="tx6">Colors: Male: 3–4 kg, Female: 3–4 kg</h4>
                    <h4 class="tx7">The Kennel Club: White</h4>
                </div>
                """, width=450, height=400)
                st.write('---')
                query1 = "Maltese dog"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[1])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])

            elif array[0][2] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Afghan Hound</h3>
                    <p class="Description">
                    The Afghan Hound is a hound that is distinguished by its thick, fine, silky coat and its tail with a ring curl at the end. The breed is selectively bred for its unique features in the cold mountains of Afghanistan. Its local name is Tāžī Spay or Sag-e Tāzī
                    </p>

                    <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                    <h4 class="tx2">Temperament: Dignified, Aloof, Independent, Clownish, Happy,</h4>
                    <h4 class="tx3">Hypoallergenic: Yes</h4>
                    <h4 class="tx4">Origin: Afghanistan</h4>
                    <h4 class="tx5">Height: Male: 68–74 cm, Female: 60–69 cm</h4>
                    <h4 class="tx6">Colors: Black, Cream, Red</h4>
                    <h4 class="tx7">The Kennel Club: White</h4>
                </div>
                """, width=450, height=400)
                st.write('---')
                query1 = "Afghan hound dog"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[1])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])
            elif array[0][3] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Entlebucher</h3>
                    <p class="Description">
                    The Entlebucher Sennenhund or Entlebucher Mountain Dog is a medium-sized herding dog, it is the smallest of the four regional breeds that constitute the Sennenhund dog type. The name Sennenhund refers to people called Senn, herders in the Swiss Alps. Entlebuch is a region in the canton of Lucerne in Switzerland.
                    </p>

                    <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                    <h4 class="tx2">Temperament: Dignified, Aloof, Independent, Clownish, Happy,</h4>
                    <h4 class="tx3">Hypoallergenic: Yes</h4>
                    <h4 class="tx4">Origin: Afghanistan</h4>
                    <h4 class="tx5">Height: Male: 68–74 cm, Female: 60–69 cm</h4>
                    <h4 class="tx6">Colors: Black, Cream, Red</h4>
                    <h4 class="tx7">The Kennel Club: White</h4>
                </div>
                """, width=450, height=420)
                st.write('---')
                query1 = "Entlebucher dog"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[1])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])

            elif array[0][4] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Bernese Mountain Dog</h3>
                    <p class="Description">
                    The Bernese Mountain Dog is a large dog breed, one of the four breeds of Sennenhund-type dogs from Bern, Switzerland and the Swiss Alps. These dogs have roots in the Roman mastiffs. The name Sennenhund is derived from the German Senne and Hund, as they accompanied the alpine herders and dairymen called Senn.
                    </p>

                    <h4 class="tx1">Life expectancy: 6 – 8 years</h4>
                    <h4 class="tx2">Temperament: Intelligent, Affectionate, Loyal, Faithful</h4>
                    <h4 class="tx3">Hypoallergenic: Yes</h4>
                    <h4 class="tx4">Origin: Afghanistan</h4>
                    <h4 class="tx5">Height: Male: 64–70 cm, Female: 58–66 cm</h4>
                    <h4 class="tx6">Male: 38–50 kg, Female: 36–48 kg</h4>
                    <h4 class="tx7">Switzerland</h4>
                </div>
                """, width=450, height=400)
                st.write('---')
                query1 = "Bernese mountain dog breed"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[1])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])
            elif array[0][5] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Shih Tzu</h3>
                    <p class="Description">
                    The Shih Tzu is a toy dog breed originating from Tibet and was bred from the Pekingese and the Lhasa Apso. Shih Tzus are known for their short snouts and large round eyes, as well as their long coat, floppy ears, and short and stout posture.
                    </p>

                    <h4 class="tx1">Life expectancy: 10 – 16 years</h4>
                    <h4 class="tx2">Temperament: Playful, Clever, Friendly, Intelligent, Lively, Outgoing,</h4>
                    <h4 class="tx3">Hypoallergenic: Yes</h4>
                    <h4 class="tx4">Origin: China, Tibet</h4>
                    <h4 class="tx5">Height: 20 – 28 cm (Female, Adult, At the withers), 20 – 28 cm (Male, Adult, At the withers)</h4>
                    <h4 class="tx6">Mass: 4 – 7.2 kg (Female, Adult), 4 – 7.2 kg (Male, Adult)</h4>
                </div>
                """, width=450, height=400)
                st.write('---')
                query1 = "Shih Tzu dog breed"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[1])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])
                st.markdown('shih-tzu')

            elif array[0][6] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;
                        padding-bottom:20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Pyrenean Mountain Dog</h3>
                    <p class="Description">
                    The Pyrenean Mountain Dog is a breed of livestock guardian dog from France, where it is commonly called the Patou. The breed comes from the French side of the Pyrenees Mountains that separate France and Spain.
                    </p>

                    <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                    <h4 class="tx2">Temperament: Dignified, Aloof, Independent, Clownish, Happy,</h4>
                    <h4 class="tx3">Hypoallergenic: Yes</h4>
                    <h4 class="tx4">Origin: Afghanistan</h4>
                    <h4 class="tx5">Height: Male: 68–74 cm, Female: 60–69 cm</h4>
                </div>
                """, width=450, height=380)
                st.write('---')
                query1 = "Pyrenean Mountain Dog"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[1])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])
            elif array[0][7] == 1:
                com.html("""
                 <style>
                     .info_div{
                         box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                         border-radius:8px;
                         background-color:#fc4949;
                         color:white;
                         margin-top:-20px;    
                     }
                     .Dog_name{
                     font-size:22px;
                     font-family:calibri;
                     padding-top: 20px;
                     padding-left: 20px;
                     font-weight:600;
                     }
                     .Description{
                     font-family:calibri;
                     font-size:17px;
                     text-align:justify;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-5px;
                     }

                     .text1{
                     display:flex;
                     flex-direction:horizontal;
                     }
                     .tx1{
                     font-family: calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top: -5px;
                     }
                     .tx2{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx3{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx4{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }

                     .tx5{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx6{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }

                     .tx7{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     padding-bottom:20px;
                     }

                 </style>

                 <div class="info_div">
                     <h3 class="Dog_name">Pomeranian</h3>
                     <p class="Description">
                       The Pomeranian is a breed of dog of the Spitz type that is named for the Pomerania region in north-west Poland and north-east Germany in Central Europe. Classed as a toy dog breed because of its small size, the Pomeranian is descended from larger Spitz-type dogs, specifically the German Spitz.
                     </p>

                     <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                     <h4 class="tx2">Temperament: Playful, Docile, Easygoing, Intelligent, Lively,</h4>
                     <h4 class="tx3">Hypoallergenic: Yes</h4>
                     <h4 class="tx4">Origin: Italy, Mediterranean Basin</h4>
                     <h4 class="tx5">Weight: Male: 21–25 cm, Female: 20–23 cm</h4>
                     <h4 class="tx6">Colors: Male: 3–4 kg, Female: 3–4 kg</h4>
                     <h4 class="tx7">The Kennel Club: White</h4>
                 </div>
                 """, width=450, height=400)
                st.write('---')
                query1 = "Pomeranian dog breed"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[3])
                with tab2:
                    st.image(list_img_urls[4])
                with tab3:
                    st.image(list_img_urls[5])

            elif array[0][8] == 1:
                com.html("""
                 <style>
                     .info_div{
                         box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                         border-radius:8px;
                         background-color:#fc4949;
                         color:white;
                         margin-top:-20px;    
                     }
                     .Dog_name{
                     font-size:22px;
                     font-family:calibri;
                     padding-top: 20px;
                     padding-left: 20px;
                     font-weight:600;
                     }
                     .Description{
                     font-family:calibri;
                     font-size:17px;
                     text-align:justify;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-5px;
                     }

                     .text1{
                     display:flex;
                     flex-direction:horizontal;
                     }
                     .tx1{
                     font-family: calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top: -5px;
                     }
                     .tx2{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx3{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx4{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }

                     .tx5{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx6{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }

                     .tx7{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     padding-bottom:20px;
                     }

                 </style>

                 <div class="info_div">
                     <h3 class="Dog_name">Basenji</h3>
                     <p class="Description">
                        The Basenji is a breed of hunting dog. It was bred from stock that originated in central Africa. The Fédération Cynologique Internationale places the breed in the Spitz and primitive types. 
                        The Basenji produces an unusual yodel-like sound, due to its unusually shaped larynx.
                     </p>

                     <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                     <h4 class="tx2">Temperament: Playful, Docile, Easygoing, Intelligent, Lively,</h4>
                     <h4 class="tx3">Hypoallergenic: Yes</h4>
                     <h4 class="tx4">Origin: Italy, Mediterranean Basin</h4>
                     <h4 class="tx5">Weight: Male: 21–25 cm, Female: 20–23 cm</h4>
                     <h4 class="tx6">Colors: Male: 3–4 kg, Female: 3–4 kg</h4>
                     <h4 class="tx7">The Kennel Club: White</h4>
                 </div>
                 """, width=450, height=400)
                st.write('---')
                query1 = "Basenji dog breed"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[3])
                with tab2:
                    st.image(list_img_urls[4])
                with tab3:
                    st.image(list_img_urls[5])
            elif array[0][9] == 1:
                com.html("""
                 <style>
                     .info_div{
                         box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                         border-radius:8px;
                         background-color:#fc4949;
                         color:white;
                         margin-top:-20px;    
                     }
                     .Dog_name{
                     font-size:22px;
                     font-family:calibri;
                     padding-top: 20px;
                     padding-left: 20px;
                     font-weight:600;
                     }
                     .Description{
                     font-family:calibri;
                     font-size:17px;
                     text-align:justify;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-5px;
                     }

                     .text1{
                     display:flex;
                     flex-direction:horizontal;
                     }
                     .tx1{
                     font-family: calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top: -5px;
                     }
                     .tx2{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx3{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx4{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }

                     .tx5{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }
                     .tx6{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     }

                     .tx7{
                     font-family:calibri;
                     margin-left:20px;
                     margin-right:20px;
                     margin-top:-15px;
                     padding-bottom:20px;
                     }

                 </style>

                 <div class="info_div">
                     <h3 class="Dog_name">Samoyed</h3>
                     <p class="Description">
                        The Samoyed is a breed of medium-sized herding dogs with thick, white, double-layer coats. They are a spitz-type dog which takes its name from the Samoyedic peoples of Siberia. Descending from the Nenets Herding Laika, 
                        they are a domesticated animal that assists in herding, hunting, protection and sled-pulling.
                     </p>

                     <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                     <h4 class="tx2">Temperament: Playful, Docile, Easygoing, Intelligent, Lively,</h4>
                     <h4 class="tx3">Hypoallergenic: Yes</h4>
                     <h4 class="tx4">Origin: Italy, Mediterranean Basin</h4>
                     <h4 class="tx5">Weight: Male: 21–25 cm, Female: 20–23 cm</h4>
                     <h4 class="tx6">Colors: Male: 3–4 kg, Female: 3–4 kg</h4>
                     <h4 class="tx7">The Kennel Club: White</h4>
                 </div>
                 """, width=450, height=400)
                st.write('---')
                query1 = "Samoyed dog breed"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[3])
                with tab2:
                    st.image(list_img_urls[4])
                with tab3:
                    st.image(list_img_urls[5])
        st.write('---')
elif selected == "Take Camera":
    camera_input = st.camera_input("Take a photo")
    if camera_input is not None:
        loaded_model = tf.keras.models.load_model('C:/Users/GL/PycharmProjects/VirtualAssistant/DBC.h5')
        img1 = image.load_img(camera_input, target_size=(224, 224))
        img2 = image.load_img(camera_input)
        test_image = image.img_to_array(img1)
        test_image = np.expand_dims(test_image, axis=0)
        images = np.vstack([test_image])
        val = loaded_model.predict(images)
        coll1, coll2 = st.columns(2)
        with coll1:
            st.image(img2)
            array = np.array(val)
            if array[0][0]==1:
                with st.expander("Size"):
                    st.markdown('''#### 15 to 20 inches tall ''')
                    st.markdown(
                        "Depending on gender, the Irish wolfhound ranges in height from 30 to 36 inches tall, while the Scottish deerhound only measures 30 to 32 inches tall. While both of these dogs look extraordinarily similar to one another, there are some key differences in their sizes.")
                with st.expander('Shadding'):
                    st.markdown(
                        "The deerhound coat does not shed, but it needs weekly brushing or combing, and the dead hairs need to be pulled out by hand twice a year. The beard tends to drip water after drinking, and it should be washed frequently.")
                with st.expander("Purpose"):
                    st.markdown(
                        "The crisply coated Scottish Deerhound, 'Royal Dog of Scotland,' is a majestically large coursing hound struck from the ancient Greyhound template. Among the tallest of dog breeds, the Deerhound was bred to stalk the giant wild red deer.")
                with st.expander("Health"):
                    st.markdown(
                        "The Scottish Deerhound breed, which has an average lifespan of 7 to 9 years, is susceptible to major health issues such as cardiomyopathy, gastric torsion, and osteosarcoma. Hypothyroidism, neck pain, atopy, and cystinuria may also plague this dog.Oct 6, 2009")
        with coll2:
            array = np.array(val)
            if array[0][0] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Scottish Deerhound</h3>
                    <p class="Description">
                        The Scottish Deerhound, or simply the Deerhound, is a large breed of sighthound,
                         once bred to hunt the red deer by coursing. In outward appearance, the Scottish Deerhound 
                         is similar to the Greyhound, but larger and more heavily boned with a rough-coat.
                    </p>

                    <h4 class="tx1">Life Expectancy: 8-11 years.</h4>
                    <h4 class="tx2">Temperament: Dignified, Docile, Friendly, Gentle</h4>
                    <h4 class="tx3">Hypoallergenic: No</h4>
                    <h4 class="tx4">Origin: Scotland</h4>
                    <h4 class="tx5">Weight: Male: 39–50 kg, Female: 34–43 kg</h4>
                    <h4 class="tx6">Colors: Brindle, Fawn, Red Fawn, Blue, Grey, Yellow</h4>
                    <h4 class="tx7">The Kennel Club: standard</h4>
                </div>
                """, width=450, height=400)
                st.write('---')
                query1 = "Scottish Deerhound"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[5])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])
            elif array[0][2] == 1:
                com.html("""
                <style>
                    .info_div{
                        box-shadow:2px 2px 10px rgba(0,0,0,0.25);
                        border-radius:8px;
                        background-color:#fc4949;
                        color:white;
                        margin-top:-20px;    
                    }
                    .Dog_name{
                    font-size:22px;
                    font-family:calibri;
                    padding-top: 20px;
                    padding-left: 20px;
                    font-weight:600;
                    }
                    .Description{
                    font-family:calibri;
                    font-size:17px;
                    text-align:justify;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-5px;
                    }

                    .text1{
                    display:flex;
                    flex-direction:horizontal;
                    }
                    .tx1{
                    font-family: calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top: -5px;
                    }
                    .tx2{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx3{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx4{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx5{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }
                    .tx6{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    }

                    .tx7{
                    font-family:calibri;
                    margin-left:20px;
                    margin-right:20px;
                    margin-top:-15px;
                    padding-bottom:20px;
                    }

                </style>

                <div class="info_div">
                    <h3 class="Dog_name">Afghan Hound</h3>
                    <p class="Description">
                    The Afghan Hound is a hound that is distinguished by its thick, fine, silky coat and its tail with a ring curl at the end. The breed is selectively bred for its unique features in the cold mountains of Afghanistan. Its local name is Tāžī Spay or Sag-e Tāzī
                    </p>

                    <h4 class="tx1">Life Expectancy: 12 – 15 years</h4>
                    <h4 class="tx2">Temperament: Dignified, Aloof, Independent, Clownish, Happy,</h4>
                    <h4 class="tx3">Hypoallergenic: Yes</h4>
                    <h4 class="tx4">Origin: Afghanistan</h4>
                    <h4 class="tx5">Height: Male: 68–74 cm, Female: 60–69 cm</h4>
                    <h4 class="tx6">Colors: Black, Cream, Red</h4>
                    <h4 class="tx7">The Kennel Club: White</h4>
                </div>
                """, width=450, height=400)
                st.write('---')
                query1 = "Afghan hound dog"
                wp_page = wikipedia.page(query1)
                list_img_urls = wp_page.images

                tab1, tab2, tab3 = st.tabs(['Related Dog image 1', 'Related Dog image 2', 'Related Dog images 3'])
                with tab1:
                    st.image(list_img_urls[1])
                with tab2:
                    st.image(list_img_urls[2])
                with tab3:
                    st.image(list_img_urls[3])
