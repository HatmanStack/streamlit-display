import streamlit
import pandas
import requests
import snowflake.connector


def get_cur():
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  data = get_party_invites()
  my_cnx.close()
  df = pandas.DataFrame(data)
  streamlit.table(df)


def get_party_invites():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from SHEETS")
    return my_cur.fetchall()

get_cur()