"""
Version 1.0.0
Data Processer
Purpose: Process chart data to the database to save time when viewing charts
NOTES:

08/22/2019 - Added a new application named process. Process script cut-pasted to this application. 
dashboard/URLS has been edited to include path('process.urls')

A question, do I want to really have a view for process? I assume not.


#SAVE TO DATABASE (with SQL) Are we using lite, or postgresql?
is chart1_data.to_sql() useful?
Saving the charts is another option but causes bloat

"""
from internal.models import *
from transportation.models import *
import pandas as pd
import pdb

pdb.set_trace()

#prototype for processor
def process_raw_data(request):
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
    #sort before cumsum()
    chart1_data['nPersons_cum'] = chart1_data['nPersons'].cumsum()
    chart1_data['nPersonsDiab_cum'] = chart1_data['nPersonsDiab'].cumsum()
    
    #chart data to database
    chart1_data.to_sql('chartData', con, if_exists='replace')

    #Unsure about my return. Left unchanged from views.py script.
    return (request, 'transportation.html', context)


