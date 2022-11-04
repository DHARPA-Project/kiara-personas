from dash import Dash, html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from visualizations_jinja.kiara_features import create_viz
from texts import *


external_stylesheets = [dbc.themes.FLATLY]

app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=False, suppress_callback_exceptions=True, assets_ignore='.*.js')

viz = html.Div(children=[
        create_viz(600),
        ])

app.layout = html.Div([
    dbc.NavbarSimple(brand='Kiara users'),
    html.Br(),
	html.Div(children=[
    dbc.Row([
        
        dbc.Col(dbc.Card(html.Div(children=[
            html.Br(),
            viz,
        ])), width=6),

        dbc.Col(html.Div(children=[
            dbc.Input(placeholder="Kiara", id='clicked-feat', readonly=True, size="sm",style={"width": "50%","display":"inline","margin-right":"1em","background-color":"white"}),
            html.Br(),
            html.Br(),
            html.Div(id='feat-content')
        ])
        , width=6)])
        
    ], style={"margin":"2%"}),
    dbc.Button(id='button-test', n_clicks=0,color="light"),
    dcc.Store(id="clicked-page", data=[]),
])

app.clientside_callback(
    """
    function(clicks,value) {
        if (clicks>0) {
            clicked = document.getElementById('clicked-feat').value
            return clicked
        }
    }
    """,
    Output("clicked-page", "data"),
    [Input('button-test', 'n_clicks')],
)

@callback(
    Output('feat-content','children'),
    Input("clicked-page", "data"))
def display_content(value):
    content = texts_keys[value] or None
    
    return content

if __name__ == '__main__':
	app.run_server(debug=True)