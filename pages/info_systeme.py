import dash
from dash import html, dcc, callback, Input, Output, State
import plotly.express as px
import pandas as pd
import base64

#####################################
#page des informations
#####################################

# new_layout={
#     "font_family":"Courier New",
#     "font_color":"blue",
#     "title_font_family":"Times New Roman",
#     "title_font_color":"red",
#     "legend_title_font_color":"green",
    
#     'paper_bgcolor':'rgba(0,35,71,255)'  ,
#     'plot_bgcolor':'rgba(0,35,71,255)' ,
# }

new_layout={
    "font_color":"rgba(253,119,2,255)",
    'paper_bgcolor':'rgba(0,35,71,255)'  ,
    'plot_bgcolor':'rgba(0,35,71,255)',
    'boxmode' : 'group',
    'barmode' : 'group',
    
}

df = pd.read_csv("data\\csv\\data_2.csv")
fig_1 = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60,
                 color_discrete_sequence=px.colors.sequential.Plasma)

fig_1.update_layout(new_layout)
dash.register_page(__name__,path='/2')

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.update_layout(new_layout)


layout=html.Div(
    className="graphContainer",
    children=[
        #division pour 
        dcc.Graph(className="Graph",figure=fig),
         dcc.Graph(
                    id='life-exp-vs-gdp',
                    className='Graph',
                     figure=fig_1
                    )
    ]
)