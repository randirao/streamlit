import streamlit as st

if 'point' not in st.session_state:
    st.session_state.point = 0

pit=0

genre = st.radio(
    "***1) 1+1=?***",
    ["창문", "2", "10"])

if genre == "2":
    st.write("정답! :grin:")
    pit+=50
else:
    st.write("오답 :sweat_smile:")

title = st.text_input("***2) 오리가 얼면?***")
if title == '언덕' :
    st.write("정답! :grin:")
    pit+=50
else :
    st.write("오답 :sweat_smile:")

st.session_state.point = pit