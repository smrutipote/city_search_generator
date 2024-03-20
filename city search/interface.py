import given
import streamlit
import streamlit as st

st.title('City Search Begins here')
country = st.sidebar.selectbox('Pick a city', ('Mumbai', 'Paris', 'New york', 'Mexico city', 'Tokyo',  'London'))


# def testing(country):
#     return {'city': 'Mumbai',
#             'place': 'Gate way of India,Marine drive, Taj Hotel'}


if country:
    options = given.country_call(country)
    st.header(options['city'])
    parts = options['place'].strip().split(',')
    for num in parts:
        st.write(num)


////In Terminal : streamlit run interface.py///////////
