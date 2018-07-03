import quandl
import config
import datetime 
from dateutil.relativedelta import relativedelta

class Zillow:
   
    def __init__(self, code, code_segment, metric, time_span):
        self.code = code
        self.code_segment = code_segment
        self.metric = metric
        self.time_span = time_span
        self.end_date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.start_date = (datetime.datetime.now() - relativedelta(years=self.time_span)).strftime('%Y-%m-%d')
        self.data = self.getData() 
    
    def __str__(self):
        data_string = self.data[:25]
        return str(data_string)

    def getData(self):
        quandl.ApiConfig.api_key = config.api_key
        request = 'ZILLOW/{0}{1}_{2}'.format(self.code_segment, self.code, self.metric)
        return quandl.get(request, start_date=self.start_date, end_date=self.end_date)

if __name__ == "__main__":
    pass
