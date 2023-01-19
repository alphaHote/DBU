from dash import Dash, html, dcc
import dash
import os

app = Dash(__name__, use_pages=True)

app.layout = html.Div([

    # html.Div(
    #     [
    #         html.Div(
    #             dcc.Link(
    #                 f"{page['name']} - {page['path']}", href=page["relative_path"]
    #             )
    #         )
    #         for page in dash.page_registry.values()
    #     ]
    # ),
    #[divBarreNavigation, tableBarreNavigation, ligneBarreNavigation, colonneBarreNavigation]

    

    html.Div(
        className="navbar",
        children=[
            html.A("situation globale",href='/'),
            html.A("situation personnel",href='/0'),
            html.A("situation matériel",href='/1'),
            html.A("informations système",href='/2'),
        ]
    ),

    html.Div(
        className="main",

        children=[	dash.page_container]
    ),
  

])

if __name__ == '__main__':
    # os.system("start http://127.0.0.1:8050/")
    app.run_server(host="0.0.0.0")