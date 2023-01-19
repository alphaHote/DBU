import dash
from dash import html, dcc, callback, Input, Output, State
import plotly.express as px
import pandas as pd
import base64

#####################################
#page des personnels
#####################################

dash.register_page(__name__,path='/0')
new_layout={
    "font_color":"rgba(253,119,2,255)",
    'paper_bgcolor':'rgba(0,35,71,255)'  ,
    'plot_bgcolor':'rgba(0,35,71,255)',
    'boxmode' : 'group',
    'barmode' : 'group'
}

fig_retraite=px.line(x=[2022,2023,2024,2025],y=[2,4,10,9])
fig_retraite.update_layout(new_layout)

df = pd.read_csv(".\\data\\csv\\data.csv")
def generate_table(dataframe, max_rows=30):
    return html.Table(
        className="tableau",
        children=[
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

layout=html.Div(
    children=[
        # html.H4(children='US Agriculture Exports (2011)'),
        html.H1(className="title",children=["disponibilité des personnels"]),
        dcc.Graph(className='Graph',figure=fig_retraite),
        html.H1(className="title",children=["tableau des effectifs"]),
        html.Div(className="divTableau",children=[generate_table(df)]),
        html.H1(className="title",children=["recherche des personnel"]),

    ]
)