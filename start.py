import streamlit as st
from scipy.special import comb
import random

with st.echo():

    #import streamlit as st
    #from scipy.special import comb
    #import random
    #uncomment first three lines

    st.title("Lottozahlen Generator")
    x = st.slider('Anzahl der Zahlen',max_value=100)
    y = st.slider('Wieviele Zahlen kann man setzen?',max_value=100)
    st.write( 'Anzahl der Möglichkeiten', comb(x,y))
    z = st.slider('Wieviele Tips?',max_value=20)
    st.header("Erzeugte Tips")
    for i in range (0,z):
        list1 = sorted(random.sample(range(1,x), y))
        list2 = ' '.join(map(str, list1)) 
        st.write("" , list2)
