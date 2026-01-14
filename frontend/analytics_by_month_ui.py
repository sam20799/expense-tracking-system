import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = 'https://expense-tracking-system-5fin.onrender.com'

def monthly_analytics():
    response = requests.get(f'{API_URL}/monthlyAnalytics')
    response = response.json()
    # st.write(response)

    df = pd.DataFrame({
        'month': [record['month_name'] for record in response],
        'total': [record['total'] for record in response]
    })
    st.header("Expense Breakdown By Month")
    st.bar_chart(df,x='month',y='total',use_container_width=True)
    st.write(df)
