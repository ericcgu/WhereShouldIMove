import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import quandl
import config

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input', value='', type='text'),
    html.Div(children='First Zip Code'),
    html.Div(id='output-graph'),

])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    quandl.ApiConfig.api_key = config.api_key
    parameters = {
        'start_date': '2016-01-31',
        'end_date': '2018-05-31',
        'metric': 'MRPFAH', # median rent price /sq foot,
        'zipcode': input_data,
        'zipcode1': '06903'
    }

    METRIC = 'ZILLOW/Z{0}_{1}'.format(parameters["zipcode"], parameters["metric"])

    rent_price_data = quandl.get(METRIC, start_date=parameters["start_date"], end_date=parameters["end_date"])
   def get_data(self):
        quandl.ApiConfig.api_key = config.api_key
        request = 'ZILLOW/{0}{1}_{2}'.format(self.code_segment, self.code, self.metric)
        return quandl.get(METRIC, start_date=self.start_date, end_date=self.end_date)

            def __str__(self):
        data_string = self.data[:10]
        return str(data_string)

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
            {'x': rent_price_data.index, 'y': rent_price_data['Value'], 'type': 'line', 'name': input_data},
            {'x': rent_price_data.index, 'y': rent_price_data['Value']+1, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': 'Real Estate By Year'
            }
        }
    )




if __name__ == '__main__':
    app.run_server()







