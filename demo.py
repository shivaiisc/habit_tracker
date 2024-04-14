import matplotlib.pyplot as plt 
import streamlit as st
import pandas as pd 


st.set_page_config(page_title='habit tracker')
st.title('Habit')
df = pd.read_csv('tracker.csv')

for column in df.columns:
    fig, ax = plt.subplots(1, 1, figsize=(3,2))
    ax.set_facecolor('black')
    ax.set_title(column)
    ax.plot(df[column])
    st.pyplot(fig)
    print(column)
