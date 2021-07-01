from ssl import Options
import justpy as jp

import pandas
from datetime import datetime
from pandas.core import series
from pytz import utc
 
data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(["Month", "Course Name"])["Rating"].count().unstack()


chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    // Make sure connected countries have similar colors
    
    title: {
        floating: true,
        align: 'left',
        text: 'Rating numbers according to courses'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Source: Udemy scrore system'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Rated by Students'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Rated by Students'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [{
        name: "Finland",
        data: [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7, 7, 6, 12, 7, 9, 5, 5
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""
 
def app():
   wp = jp.QuasarPage() #wp=web page
   h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",classes="text-h3 text-center q-pa-md")

   hc = jp.HighCharts(a=wp,options=chart_def)
   hc.options.xAxis.categories = list(month_average_crs.index[0])
   # the function line for data is important !!!
   hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in list(month_average_crs.columns)]
   hc.options.series = hc_data

   return wp
 
jp.justpy(app)