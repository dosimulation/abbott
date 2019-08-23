from django.db import models
import plotly.offline as opy
import plotly.graph_objs as go
#from transportation.models import * 


class TransLogDescriptive(models.Model):
	total_persons     = models.IntegerField(default=100)
	avg_age           = models.FloatField(default=35.0)		


class PlotObject(models.Model):
    TransLog_trend =models.ImageField()
    TransLog_race = models.ImageField()
