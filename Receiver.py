
from bsread import source, PULL
import threading
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import json


newStore = {}
secStore = {}

def receive_stream():
    with source(host = 'localhost',port=1500, mode = PULL) as stream:
        while True:

            message = stream.receive()

            newStore["x"] = message.data.data['CHA_1'].value
            newStore["y"] = message.data.data['CHA_2'].value

            secStore["x"] = message.data.data['CHA_3'].value
            secStore["y"] = message.data.data['CHA_4'].value


t1 = threading.Thread(target = receive_stream)
t1.start()


app = dash.Dash(__name__)

app.layout = html.Div(

    html.Div([
        html.H2('RECEIVED STREAMS'),
        html.Div(id='updating-a-graph'),
        #dcc.Graph(id = 'a-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds
            n_intervals=0)
])

)


@app.callback(Output('updating-a-graph', 'children'),
              [Input('interval-component', 'n_intervals')])


def print_stream(data):
    return dcc.Graph(figure = {'data':[newStore , secStore]})
if __name__ == '__main__':
    app.run_server(debug=True ,port=8088, host=0.0)


