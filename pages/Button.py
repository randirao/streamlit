import streamlit as st
if 'key' not in st.session_state:
    st.session_state.key = 'NULL'

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Hi")
else:
    st.write("Bi")