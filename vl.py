import pandas as pd
import streamlit as st
import datetime

st.set_page_config(
     page_title="VL LAUNCH",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="expanded"
 )


from PIL import Image

col1,col2,col3=st.columns([4,5,3])
with col2:
     st.title('''VL LAUNCH''')
with col1:
    pass
with  col3:
     i=Image.open('roc.jpg')
     st.set_option('deprecation.showPyplotGlobalUse', False)                          #image projection
     st.image(i,use_column_width=None)

search = st.sidebar.radio("HOME",('home','about'))
