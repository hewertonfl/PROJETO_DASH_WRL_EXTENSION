from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import os

app = Dash(__name__, external_stylesheets=[
           dbc.themes.BOOTSTRAP], external_scripts=['./assets/js/html2pdf.bundle.min.js'])

app.scripts.config.serve_locally = True


def imageRenderer(imagemOriginal, imagemSegmentada,imagemOriginal_2, imagemSegmentada_2):
    return html.Div([
        html.Div([
            html.Div([html.H2('Imagem Segmentada', className='text-center border-bottom text-info'), html.Div(html.Img(
                src=f'./assets/{imagemSegmentada}', className='w-100', style={"border-radius": "50px"}))], className='w-50 d-inline-block m-0', style={"padding": "0 1.5% 0 3%"}),

            html.Div([html.H2('Imagem Original', className='text-center border-bottom text-info'), html.Div(html.Img(src=f'./assets/{imagemOriginal}', className='w-100', style={
                     "border-radius": "50px"}))], className='w-50 d-inline-block m-0', style={"padding": "0 3% 0 1.5%"}),
        ], className='w-100 d-inline-block', style={"margin-top": "3%"}
        ),
        html.Div([
            html.Div([html.H2('Imagem Segmentada', className='text-center border-bottom text-info'), html.Div(html.Img(
                src=f'./assets/{imagemSegmentada_2}', className='w-100', style={"border-radius": "50px"}))], className='w-50 d-inline-block m-0', style={"padding": "0 1.5% 0 3%"}),

            html.Div([html.H2('Imagem Original', className='text-center border-bottom text-info'), html.Div(html.Img(src=f'./assets/{imagemOriginal_2}', className='w-100', style={
                     "border-radius": "50px"}))], className='w-50 d-inline-block m-0', style={"padding": "0 3% 0 1.5%"}),
        ], className='w-100 d-inline-block', style={"margin-top": "3%"}
        )
    ], style={'height': '50%', "overflow":"hidden"}, className='rowImages html2pdf__page-break toprint')


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
              ], className="m-0 p-0",


)

app.clientside_callback(
    """
    function gerarPDF(n_clicks) {
        var element = document.getElementById('output')
        //var button = document.getElementById('js')
        var main_container_width = element.style.width
        var opt = {
                //margin: 10,
                filename:'my-dashboard.pdf',
                image: { type: 'jpg', quality: 0.3 },
                html2canvas: { scale: 0.5},
                jsPDF: { unit: 'mm', format: 'A4', orientation: 'portrait'},
                // Set pagebreaks if you like. It didn't work out well for me.
                pagebreak: { mode: ['avoid-all'] }
            }
            // Execute the save command. 
            html2pdf().from(element).set(opt).save()
}
    """,
    Output('js', 'n_clicks'),
    Input('js', 'n_clicks'),
    prevent_initial_call=True
)


@app.callback(
    Output('output', 'children'),
    Input('load-new-content', 'n_clicks'),
    State('output', 'children'))
def more_output(n_clicks, old_output):
    name = os.listdir('./assets')
    for i in range(0, len(name)-1, 4):
        if name[i] == 'js':
            pass
        else:
            old_output.append(imageRenderer(name[i], name[i+1],name[i+2], name[i+3]))
    return old_output


if __name__ == '__main__':
    # print(os.listdir('./assets'))
    app.run_server(debug=True)
