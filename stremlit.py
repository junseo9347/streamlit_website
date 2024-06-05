import streamlit as st
import pandas as pd
st.write("""This is a graph of the win percentage and unbeaten percentage of Totttenham Hostpurs Football Club since 1945""")


import pandas as pd

import altair as alt

df_1 = pd.read_csv("C:/Users/junse/PycharmProjects/app_dev/ai/tottenham_win_percent.csv", header=None, names=['Value'])
df_2 = pd.read_csv("C:/Users/junse/PycharmProjects/app_dev/ai/tottenham_unbeaten_percent.csv",header=None, names=['Value'])

start_year = 1945

years = range(start_year, start_year + len(df_1))

df_1['Year'] = years

chart = alt.Chart(df_1).mark_line().encode(

    x=alt.X('Year:O', title='Year'),  # Set the x-axis as ordinal to ensure no decimals

    y=alt.Y('Value', title='Value')

).properties(

    title='Tottenham Win Rate'

)

st.altair_chart(chart, use_container_width=True)



start_year = 1945

years = range(start_year, start_year + len(df_2))

df_2['Year'] = years

chart = alt.Chart(df_2).mark_line().encode(

    x=alt.X('Year:O', title='Year'),  # Set the x-axis as ordinal to ensure no decimals

    y=alt.Y('Value', title='Value')

).properties(

    title='Tottenham Unbeaten Rate'

)

st.altair_chart(chart, use_container_width=True)

teams_df = pd.read_csv('C:/Users/junse/PycharmProjects/app_dev/ai/tottenham_win_team.csv', header=None, names=['team'])
wins_df = pd.read_csv('C:/Users/junse/PycharmProjects/app_dev/ai/tottenham_win_record.csv', header=None, names=['wins'])
teams_df['wins'] = wins_df['wins']

# Create the bar chart
chart = alt.Chart(teams_df).mark_bar().encode(
    x=alt.X('team', sort=None),
    y='wins'
).properties(
    title='Tottenham Win Record'
)
st.altair_chart(chart, use_container_width=False)



