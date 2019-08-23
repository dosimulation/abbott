
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import TransLogDescriptive
from .models import PlotObject

# this will create the buttons for import and export as well
admin.site.register(TransLogDescriptive)
admin.site.register(PlotObject)


