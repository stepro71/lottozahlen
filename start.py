import streamlit as st
import math
import random
with st.echo():
    st.title("Lottozahlen Generator")
    x = st.slider('Anzahl der Zahlen',max_value=100)
    y = st.slider('Wieviele Zahlen kann man setzen?',max_value=100)
    st.write( 'Anzahl der Möglichkeiten', comb(x,y))
    z = st.slider('Wieviele Tips?',max_value=20)


    st.header("Erzeugte Tips")
#list2 = [list1.pop(list1.index(min(list1))) for i in range(len(list1))]
    for i in range (0,z):
        list1 = sorted(random.sample(range(1,x), y))
        list2 = ' '.join(map(str, list1)) 
        st.write("" , list2)