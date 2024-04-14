import pandas as pd
import streamlit as st
import plotly.express as px 
import matplotlib.pyplot as plt 






img = plt.imread('./my_img.jpg')
h, w = img.shape[:2]
img = img[:int(0.6*h), :int(0.8*w), :]





standard = {'Samyama':90,
            'Surya Shakthi':48,
            'Kapala Bhathi': 500}
caption = {'Samyama': 'Samyama is a state where you become fully aware that you are not the body, you are not the mind you are not the world around.',
           'Surya Shakthi': 'The basis of all spiritual sadhana  which is physical in nature is to get us in sync with the cycles of nature',
           'Kapala Bhathi': 'Crank up the voltage' }




st.set_page_config(page_title="Habit Tracker", page_icon=":100:", layout="wide")

st.title("Habit Tracker")
st.header('Consistency is the key.')
is_img_shown =False

df = pd.read_csv('tracker.csv')
for column in df.columns:
    st.header(caption[column])
    col1, col2 = st.columns(2, gap='Large')
    df[column + ' total'] = df[column].cumsum()
    with col1:
        st.subheader(column, divider='rainbow')
        fig = px.line(df, x = df.index, y=column, labels={
            'index': 'Time (ticking away)',
            column: 'Intensity'
        })
        st.plotly_chart(fig,use_container_width=False)
    with col2:
        st.subheader(column + ' total', divider='rainbow')

        fig = px.line(df, x = df.index, y=column + ' total', labels={
            'index': 'Time (ticking away)',
            column: 'Intensity'
            })
        st.plotly_chart(fig, use_container_width=False)
    if not is_img_shown:
        st.image(img,use_column_width=False)
        is_img_shown = True


st.header('Last 3 days:')


st.write(df.tail(3))


