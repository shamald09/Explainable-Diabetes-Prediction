import time

import streamlit as st


def app(input_data):
    def stream_data():
        text = f"""
Your inputs:\n
`Pregnancies`: {float(input_data.iloc[0]['Pregnancies'])}\n
`Glucose`: {float(input_data.iloc[0]['Pregnancies'])}\n
`Insulin`: {float(input_data.iloc[0]['Pregnancies'])}\n
`BMI`: {float(input_data.iloc[0]['Pregnancies'])}\n
`Age`: {float(input_data.iloc[0]['Pregnancies'])}
                """
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)

    st.markdown("### Input Streaming")
    st.markdown("#### See your inputs in real-time below!")
    for word in stream_data():
        st.write(word)
