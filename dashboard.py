import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import zillow as z

app = dash.Dash()
app.css.append_css({
    'external_url': (
        'https://cdn.rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

app.layout = html.Div(children=[
    html.Div([
        html.Div([
             html.Img(src='https://cdn.geekwire.com/wp-content/uploads/2015/02/Zillow-box-logo.png', height='100', width='100')
        ], className="two columns"),

        html.Div([
             html.H1('Zillow Real Estate Research', style={'text-align': 'center'})
        ], className="eight columns"),
    ], className="row"),
    html.H4('Metrics Per Square Foot Over Last 3 Years by U.S. Zip Code', style={'text-align': 'center'}),
    html.Br(), html.Br(),
      html.Div([
        html.Div([
              html.Label('First Zip Code'),
              dcc.Input(id='zipcode1', value='', type='text', style={'text-align': 'center'}),
        ], className="four columns"),
         html.Div([
              html.Label('Second Zip Code'),
              dcc.Input(id='zipcode2', value='', type='text', style={'text-align': 'center'}),     
        ], className="four columns"),
        html.Div([
               html.Label('Metric'),
               dcc.RadioItems(
                   options=[
                   {'label': 'Rental Price (Median) Per Square Foot', 'value': 'MRPFAH'},
                   {'label': 'Sales Price (Median) Per Square Foot ', 'value': 'MSPFAH'},
                 ],
               value='metric'),
        ], className="four columns"),
    ], className="row", style={'text-align': 'center'}),






  
 
    
])



if __name__ == '__main__':
    app.run_server()







