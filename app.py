import streamlit
import pandas
import requests
import snowflake.connector


streamlit.markdown("<h1 style='text-align: center; color: steelblue;'>Invite Results</h1>", unsafe_allow_html=True)

def get_cur():
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  data = get_party_invites(my_cnx)
  my_cnx.close()
  df = pandas.DataFrame(data)
  df.iloc[:,0]= df.iloc[:,0].str[:11]
  streamlit.table(df)


def get_party_invites(my_cnx):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from SHEETS")
    return my_cur.fetchall()

get_cur()