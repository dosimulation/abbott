from import_export import resources
from .models import TransLog
from .models import TransSurvey

class TransLogResource(resources.ModelResource):
    class Meta:
        model = TransLog
        fields = ('id', 'person_id', 'Date', 'pick_up_loc', 'drop_off_loc', 'Reason_firsttime', 'first_time',
        	      'age', 'sex', 'race', 'language', 'health_ins', 'MTS_reason', 'n_hlth_appt', 
        	      'hlth_appt_score', 'n_missed_appt', 'missed_appt_score', 'ER', 'n_ER_visit', 
        	      'diabetes_diag', 'pre_diab_diag', 'health_status')
        export_order = ('id', 'person_id', 'Date', 'pick_up_loc', 'drop_off_loc', 'Reason_firsttime', 'first_time',
        	      'age', 'sex', 'race', 'language', 'health_ins', 'MTS_reason', 'n_hlth_appt', 
        	      'hlth_appt_score', 'n_missed_appt', 'missed_appt_score', 'ER', 'n_ER_visit', 
        	      'diabetes_diag', 'pre_diab_diag', 'health_status')

class TransSurveyResource(resources.ModelResource):
    class Meta:
        model = TransSurvey
        fields = ('id', 'person_id', 'Date', 'Question_1', 'Question_2', 'Question_3', 'Question_4')
        export_order = ('id', 'person_id', 'Date', 'Question_1', 'Question_2', 'Question_3', 'Question_4')
