import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = 'http://127.0.0.1:8000'

def analytics():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Start Date',datetime(2025,8,1))
    with col2:
        end_date = st.date_input('End Date', datetime(2025,8,5))

    if st.button('Get Analytics'):

        payload = {
            'start_date':start_date.strftime("%Y-%m-%d"),
            'end_date':end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f'{API_URL}/analytics',json=payload)
        response = response.json()

        df = pd.DataFrame({
            'Category':[record for record in response],
            'Total':[response[record]['total'] for record in response],
            'Percentage':[response[record]['percentage'] for record in response]

        })
        df_sorted = df.sort_values('Percentage',ascending=False)
        st.divider()
        st.header("Expense Breakdown by Category")
        st.bar_chart(df,x="Category",y='Percentage',horizontal=True,height=300,use_container_width=True)

        st.write(df_sorted)

