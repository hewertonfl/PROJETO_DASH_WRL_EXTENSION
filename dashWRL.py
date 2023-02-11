from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_extensions import DeferScript
import os

app = Dash(__name__, external_stylesheets=[
           dbc.themes.BOOTSTRAP],)

app.scripts.config.serve_locally = True


def imageRenderer(imagemOriginal, imagemSegmentada):
    return html.Div([
        html.Div([
            html.Div([html.H2('Imagem Segmentada', className='text-center border-bottom text-info'), html.Div(html.Img(
                src=f'./assets/{imagemSegmentada}', className='w-100', style={"border-radius": "50px"}))], className='w-50 d-inline-block m-0', style={"padding": "0 1.5% 0 3%"}),

            html.Div([html.H2('Imagem Original', className='text-center border-bottom text-info'), html.Div(html.Img(src=f'./assets/{imagemOriginal}', className='w-100', style={
                     "border-radius": "50px"}))], className='w-50 d-inline-block m-0 esse', style={"padding": "0 3% 0 1.5%"}),
        ], className='w-100 d-inline-block', style={"margin-top": "3%"}
        )
    ], style={'height': '33.33%'}, className='rowImages')


def btnDownload():
    return dbc.Button(
        html.Span("Download", style={
                  'letter-spacing': '0.3rem', 'font-weight': 'bold'}),
        style={'position': 'fixed', 'top': '50%',
               'right': '-10px', 'transform': 'rotate(90deg)'},
        className='btn-primary p-3 bordered',
        id='js',
        n_clicks=0
    )


app.layout = html.Div(
    id='output',
    children=[btnDownload(),
              html.Button("Load more", id='load-new-content',
                          n_clicks=0, hidden=True),
              html.P(id='placeholder'),
              html.Script(src='./assets/js/jspdf.js')
              ], className="m-0 p-0",


)

# app.clientside_callback(
#     """
#     //import { jsPDF } from "jspdf";
#     function gerarPDF(n_clicks) {
#         /const doc = new jsPDF()
#         //doc.fromHTML($('.esse').get(0), 15, 15, {
#         //'width': 170,
#         //});
#        // doc.save("a.pdf")

# //});
#     console.log('eu')
# }
#     """,
#     Output('placeholder', 'key'),
#     Input('js', 'n_clicks'),
#     prevent_initial_call=True
# )


@app.callback(
    Output('output', 'children'),
    Input('load-new-content', 'n_clicks'),
    State('output', 'children'))
def more_output(n_clicks, old_output):
    name = os.listdir('./assets')
    for i in range(0, len(name)-1, 2):
        if name[i] == 'js':
            pass
        else:
            old_output.append(imageRenderer(name[i], name[i+1]))
    return old_output


if __name__ == '__main__':
    # print(os.listdir('./assets'))
    app.run_server(debug=True)
