import streamlit as st

st.title('결과')

col1, col2 = st.columns(2)

with col1:
    st.title(' ')

with col2:
    if st.session_state.name == 'NULL':
        st.switch_page("Main.py")
    st.write(st.session_state.name)
    
st.write("결과 : ",st.session_state.point)