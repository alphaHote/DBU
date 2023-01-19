import dash
from dash import html, dcc, callback, Input, Output, State

import plotly.express as px
import pandas as pd
import base64

#####################################
#page des matériels
#####################################

dash.register_page(__name__,path='/1')
x=["théorique","réalisé","disponible"]
y=[20,10,30]
fig=px.pie(
    labels=x,
    values=y,
    color_discrete_sequence=px.colors.sequential.Cividis_r,
    names=x
    )#,names=df["x"],values=["y"])
new_layout={
    "font_color":"rgba(253,119,2,255)",
    'paper_bgcolor':'rgba(0,35,71,255)'  ,
    'plot_bgcolor':'rgba(0,35,71,255)',
    'boxmode' : 'group',
    'barmode' : 'group'
}

fig.update_layout(new_layout)

layout=html.Div(
    children=[
        html.H1(className="title",children=["état des matériels"]),
        #division pour 
        html.Div(
            children=[
                dcc.Graph(figure=fig,className="Graph"),
            ]
        )
    ]
)