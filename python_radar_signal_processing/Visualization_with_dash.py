from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='radar-plot'),
    html.Button('Update Plot', id='update-button', n_clicks=0)
])

@app.callback(
    Output('radar-plot', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_plot(n_clicks):
    angles = np.linspace(0, 2 * np.pi, 100)
    radii = np.abs(np.sin(angles))

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=radii, theta=angles, mode='lines'))
    fig.update_layout(title='Radar Data Visualization')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
