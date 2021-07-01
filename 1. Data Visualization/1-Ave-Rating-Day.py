# make webpage
import justpy as jp

# get data and organize data
import pandas 
from datetime import datetime 
from pytz import UTC
import matplotlib as plt
data  =  pandas.read_csv("reviews.csv",parse_dates=["Timestamp"])
data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()

# make graph: copy from Highchart web.
# copy after the 'container' comma, we need the contain inside: {}
# variable = """
# { 
#   chart:
# }
# """

# js use json which is familiar with python \
# justpy will convert it into python dictionary 


# Have to change the inverted from true to false,
# Else Getting an inverted format of x-axis and y-axis

chart_def ="""
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Dayly Course Ratinge'
    },
    subtitle: {
        text: 'According to ratings from students'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.02,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}  {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-weight-bold q-pa-md text-center")
    # use the js code from top, jp.HighCharts
    hc = jp.HighCharts(a=wp, options = chart_def)
    # try to print out the dictionary, type is class 'addict.addict.Dict'
    # once run it will not show directly, after click the page it show the content of the dict 
    # print(hc.options)  and can also get to more details print(hc.options.text.title)
    # print(type(hc.options))

    # change the content in the dict 1. change tile
    hc.options.title.text = "Rating by date"
 
    # change the 2. data, series is a list which made of a dictionary 
    # series[0] is the 0 element in the list, which is a dict .data is get the data from the dict 
    
    # 2.1 change data by input directly: hc.options.series[0].data = [[3,4],[5,6],[7,8]]
    
    # 2.2 change two lists into a [x,y] list use zip, but it is not a list it is a zip object 
    # x = [1,2,4]
    # y = [3,4,5]
    # hc.options.series[0].data= list(zip(x,y))

    # 2.3 change data use 
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data= list(day_average["Rating"])
    return wp

jp.justpy(app)



