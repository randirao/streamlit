import streamlit as st

st.title('결과')

col1, col2 = st.columns(2)

with col1:
    st.title(' ')

with col2:
    st.write(st.session_state.name)

st.write("결과 : ",st.session_state.point)