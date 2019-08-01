from django.db import models

class TransLog(models.Model):
	person_id         = models.CharField(max_length=100)
	Date              = models.DateTimeField()
	pick_up_loc       = models.CharField(max_length=200)
	drop_off_loc      = models.CharField(max_length=200)
	Reason_firsttime  = models.CharField(max_length=200)
	first_time        = models.IntegerField(default=0)
	age               = models.IntegerField(default=25)
	sex               = models.CharField(max_length=20)
	race              = models.CharField(max_length=30)
	language          = models.CharField(max_length=50)
	health_ins        = models.CharField(max_length=50)
	MTS_reason        = models.CharField(max_length=50)	
	n_hlth_appt       = models.IntegerField(default=5)	
	hlth_appt_score	  = models.IntegerField(default=3)	
	n_missed_appt	  = models.IntegerField(default=3)
	missed_appt_score = models.IntegerField(default=3)
	ER                = models.CharField(max_length=10)	
	n_ER_visit        = models.IntegerField(default=3)	
	diabetes_diag     = models.CharField(max_length=10)		
	pre_diab_diag     = models.CharField(max_length=10)			
	health_status     = models.CharField(max_length=20)		


	def __str__(self):
		return self.person_id

class TransSurvey(models.Model):
	person_id = models.CharField(max_length=100)
	Date = models.DateTimeField()
	Question_1 = models.CharField(max_length=200)
	Question_2 = models.CharField(max_length=200)
	Question_3 = models.CharField(max_length=200)
	Question_4 = models.CharField(max_length=200)
	
	def __str__(self):
		return self.person_id


