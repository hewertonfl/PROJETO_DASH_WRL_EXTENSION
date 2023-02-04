# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def imageRenderer():
    return html.Div([
        html.Div([
            html.Div([html.H2('Texto',className='text-center'),html.Div(html.Img(src='./assets/teste.jpg',className='w-100 shadow'))],className='w-50 d-inline-block m-0',style={"padding":"0 1.5% 0 3%"}),
            html.Div([html.H2('Texto',className='text-center'),html.Div(html.Img(src='./assets/teste.jpg',className='w-100 shadow'))],className='w-50 d-inline-block m-0',style={"padding":"0 3% 0 1.5%"}),
    ],className='w-100 d-inline-block', style={"margin-bottom":"calc(3% - 38.391px)"}
)
])


app.layout = html.Div(children=[
    imageRenderer(),
    imageRenderer(),
    imageRenderer(),
    imageRenderer(),
    imageRenderer(),
])

if __name__ == '__main__':
    print(os.listdir('./assets'))
    app.run_server(debug=True)