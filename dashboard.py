import config
import quandl

quandl.ApiConfig.api_key = config.api_key

parameters = {
    'start_date': '2016-01-31',
    'end_date': '2018-05-31',
    'metric': 'MRPFAH', # median rent price /sq foot,
    'zipcode': '11375',
    'zipcode1': '06903'
}

METRIC = 'ZILLOW/Z{0}_{1}'.format(parameters["zipcode"], parameters["metric"])

try:
    test = quandl.get(METRIC, start_date=parameters["start_date"], end_date=parameters["end_date"])
    print(test)
except:
    print("No Data")

