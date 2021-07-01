from ssl import Options
import justpy as jp

import pandas
from datetime import datetime
from pandas.core import series
from pytz import utc
import matplotlib.pyplot as plt
 
data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(["Month", "Course Name"]).mean().unstack()
 
chart_def = """
{
  chart: {
       type: 'spline'
  },
  title: {
    text: 'Average weekly rating of different courses'
  },
  legend: {
    layout: 'vertical',
    align: 'left',
    verticalAlign: 'top',
    x: 150,
    y: 100,
    floating: true,
    borderWidth: 1,
    backgroundColor:
          '#FFFFFF'
  },
  xAxis: {
    categories: [
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday'
    ],
    plotBands: [{ // visualize the weekend
      from: 4.5,
      to: 6.5,
      color: 'rgba(68, 170, 213, .2)'
    }]
  },
  yAxis: {
    title: {
      text: 'Average Rating'
    }
  },
  tooltip: {
    shared: true,
    valueSuffix: ' units'
  },
  credits: {
    enabled: false
  },
  plotOptions: {
    areaspline: {
      fillOpacity: 0.5
    }
  },
  series: [{
    name: 'John',
    data: [3, 4, 3, 5, 4, 10, 12]
  }, {
    name: 'Jane',
    data: [1, 3, 4, 3, 3, 5, 4]
  }]
}
"""
 
def app():
   wp = jp.QuasarPage() #wp=web page
   h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",classes="text-h3 text-center q-pa-md")

   hc = jp.HighCharts(a=wp,options=chart_def)
   hc.options.xAxis.categories = list(month_average_crs.index[0])
   hc.options.xAxis.categories = list(month_average_crs.index)
   # the function line for data is important !!!
   hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in list(month_average_crs.columns)]
   hc.options.series = hc_data

   return wp
 
jp.justpy(app)