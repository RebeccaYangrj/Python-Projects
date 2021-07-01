#web
import justpy as jp

#data
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Week"] = data["Timestamp"].dt.strftime("%Y-%U")
week_average = data.groupby(["Week"]).mean()

#graph from 
fig_fmt = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Weekly Course Rating'
    },
    subtitle: {
        text: 'According to the Rating data from student'
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

# web-build


def app():
    wp = jp.QuasarPage()
    
    h1 = jp.QDiv(a=wp, text = "Analysis of course rating", classes= "text-h3 text-weight-bold q-pa-md text-center")
    h2 = jp.QDiv(a=wp, text = "Average the rating by weeks", classes= "text-h4 text-weight-bold q-pa-md text-center")
    hc = jp.HighCharts(a=wp, options = fig_fmt)
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average["Rating"])
    return wp

# initiate the web

jp.justpy(app)
