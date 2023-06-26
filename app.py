import streamlit as st
import pandas
import requests



st.markdown("<h1 style='text-align: center; color: steelblue;'>Invite Results</h1>", unsafe_allow_html=True)

def get_cur():
  conn = st.experimental_connection('snowflake', type='sql')
  data = conn.query("select * from SHEETS", ttl=600)
  df = pandas.DataFrame(data)
  time_stamp = df.iloc[:,0]
  altered_time = [i.split(' ')[0] for i in time_stamp]
  df.iloc[:,0] = altered_time
  st.table(df)


get_cur()
