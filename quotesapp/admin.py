from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Quotes

class QuotesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("topic", "quotation","by")

admin.site.register(Quotes, QuotesAdmin)