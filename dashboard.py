import pandas as pd
import streamlit as st
import plotly.express as px 
import matplotlib.pyplot as plt






st.set_page_config(page_title="Habit Tracker", page_icon="📅", layout="wide")

st.title("Habit Tracker")

df = pd.read_csv('tracker.csv')
st.write(df.tail(3))
print(df.tail(3))
for column in df.columns:
    fig, axes = plt.subplots(1, 1, figsize=(3, 2))
    axes.set_title(column)
    axes.set_facecolor('black')
    axes.plot(df[column].tolist())
    st.pyplot(fig, use_container_width=False)
