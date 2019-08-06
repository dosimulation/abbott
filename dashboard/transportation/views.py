from django.shortcuts import render, redirect
from .models import *
from django.core.files.base import ContentFile
# for plotting
import plotly.offline as opy
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import pdb
# main page
def index(request):
    return render(request, 'index.html')

# taking the translog data table, returns the total number
# of observations back to the transportation html page

# https://stackoverflow.com/questions/5631247/displaying-graphs-charts-in-django
def transportation(request):

    Nrows = TransLog.objects.count()
    df = pd.DataFrame(TransLog.objects.all().values())

    df['month'] = pd.DatetimeIndex(df['Date']).month
    
    ## aggregate the data to monthly level
    t_visit_by_month = df.groupby(['person_id', 'month']).size().reset_index(name='counts')
    d_visit_by_month = df[df['Reason_firsttime']=="Diabetes"].groupby(['person_id','month']).size().reset_index(name='counts')

    # total visits
    n_persons_by_month = t_visit_by_month.groupby(['month']).size().reset_index(name='nPersons')
    # total number of people with diabetes visits
    n_p_diab_by_month = d_visit_by_month.groupby(['month']).size().reset_index(name='nPersonsDiab')
    chart1_data = pd.merge(n_persons_by_month, n_p_diab_by_month, on ='month')
    chart1_data['nPersons_cum'] = chart1_data['nPersons'].cumsum()
    chart1_data['nPersonsDiab_cum'] = chart1_data['nPersonsDiab'].cumsum()

    
    # line chart
    trend_data = [
        go.Scatter(
            x=chart1_data['month'], # assign x as the dataframe column 'x'
            y=chart1_data['nPersons_cum'],
            name='Total Monthly Visits'
        ),
        go.Scatter(
            x=chart1_data['month'], # assign x as the dataframe column 'x'
            y=chart1_data['nPersonsDiab_cum'],
            name='Total Monthly Diabetes-Related Visits '
        )
    ]

    layout=go.Layout(title="Cumulative Trend Over Time",  yaxis={'title':'Count'},  
                     xaxis = go.layout.XAxis(
                     tickmode = 'array',
                     tickvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                     ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']), 
                     legend=go.layout.Legend(
                     x=0,
                     y=1,
                     traceorder="normal",
                     font=dict(
                     family="sans-serif",
                     size=12,
                     color="black"),
                     bgcolor="LightSteelBlue",
                     bordercolor="Black",
                     borderwidth=1),
                     margin = go.layout.Margin(
                     l = .05,
                     r = .05,
                     b = 100,
                     t = 100,
                     pad = 4), 
                     autosize=False)


    figure=go.Figure(data=trend_data,layout=layout)
    div_trend = opy.plot(figure, auto_open=False, output_type='div')

    # gender chart
    gender = df.groupby(['sex']).size().reset_index(name='count')
    fig_gender = go.Bar(x= gender['sex'], y=gender['count'], width=[.2, .2])
    data_gender=[fig_gender]

    layout=go.Layout(title="Gender", xaxis={'title':'Gender'}, yaxis={'title':'Count'}, 
                    margin = go.layout.Margin(
                        l = 50,
                        r = 50,
                        b = 100,
                        t = 100,
                        pad = 4), 
                    autosize=False)

    figure=go.Figure(data=data_gender,layout=layout)
    div_gender = opy.plot(figure, auto_open=False, output_type='div')

    # race chart
    race = df.groupby(['race']).size().reset_index(name='count')
    fig_race = go.Bar(x= race['race'], y=race['count'], width=[.2, .2])
    data_race=[fig_race]
    layout=go.Layout(title="Race/Ethnicity", xaxis={'title':'Race/Ethnicity'}, yaxis={'title':'Count'}, 
                    margin = go.layout.Margin(
                        l = 50,
                        r = 50,
                        b = 100,
                        t = 100,
                        pad = 4), 
                    autosize=False)
    
    figure=go.Figure(data=data_race,layout=layout)
    div_race = opy.plot(figure, auto_open=False, output_type='div')
    #pdb.set_trace()


    context = {
        'nobs'       : Nrows,
        'gender_plot': div_gender,
        'race_plot'  : div_race,
        'trend_plot' : div_trend,
              }
    return render(request, 'transportation.html', context)