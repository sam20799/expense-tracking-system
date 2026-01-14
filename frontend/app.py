import streamlit as st
from add_update_ui import add_update
from analytics_by_category_ui import analytics
from analytics_by_month_ui import monthly_analytics
from datetime import datetime
st.markdown("""
    <h1 style='text-align: center; color: #008080; font-family: "Trebuchet MS", sans-serif;'>
        💰 Budget Buddy 💰
    </h1>
    <hr style="border: 2px solid #008080; width: 50%; margin-left: auto; margin-right: auto;">
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 💰 Expense Tracker")
    st.caption("Track, manage & understand your spending")

    st.divider()

    st.markdown("### 🧭 How it works")

    st.markdown("""
    **1. Add / Update Expenses**  
    📅 Pick a date  
    ✍️ Add or edit entries  
    💾 Save instantly  

    **2. View Insights**  
    📊 Category-wise breakdown  
    📈 Spending distribution  
    🔍 Spot major expenses  
    """)

    st.divider()

    st.markdown("### ✨ Features")

    st.markdown("""
    ✅ Daily expense tracking  
    ✅ Edit past records  
    ✅ Spending analysis  
    ✅ Budget awareness  
    """)

    st.divider()

    st.caption("🚀 Simple. Fast. Personal finance made easy.")

tab1,tab2,tab3  = st.tabs(['Add/Update','Analytics By Category','Analytics By Month'])

with tab1:
    add_update()
with tab2:
    analytics()
with tab3:
    monthly_analytics()





current_year = datetime.now().year
st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:13px; margin-top:30px;">
        © 2026 <b>SHUBHAM KR</b>. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)


