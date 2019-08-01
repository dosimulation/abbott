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
              }
    return render(request, 'transportation.html', context)