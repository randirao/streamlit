import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
key_dict = json.loads(st.secrets["textkey"])

cred = credentials.Certificate(key_dict)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://streamlit-493fd-default-rtdb.firebaseio.com/'
})
    
if 'name' not in st.session_state:
    st.session_state.name = "NULL"

a = 0

col1, col2 = st.columns(2)

with col1:
    st.header(':blue[_summer_] vacation')
    
with col2:
    st.session_state.name = st.text_input("학번 / 이름")
    if st.button("등록", type="primary"):
        ref2=db.reference()
        ref2.update({'user':st.session_state.name })


st.markdown("**To Do List**")

agree_reading = st.checkbox("Reading books")
if agree_reading:
    a += 1

agree_studying = st.checkbox("Studying")
if agree_studying:
    a += 1

agree_workout = st.checkbox("Working out")
if agree_workout:
    a += 1

if a == 3:
    st.text('Good!')




