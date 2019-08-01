
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import TransLog
from .models import TransSurvey

# this will create the buttons for import and export as well
@admin.register(TransLog)

class TransLogAdmin(ImportExportModelAdmin):
    pass

@admin.register(TransSurvey)
class TransSurveyAdmin(ImportExportModelAdmin):
    pass