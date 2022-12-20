from django.contrib import admin
from .models import Medics, GroupType, Patient

class MedicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name','works_from', 'is_working')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name')
    list_editable = ('is_working',)
    list_filter = ('is_working', 'works_from')
    prepopulated_fields = {"slug": ("last_name",)}
admin.site.register(Medics, MedicsAdmin)
admin.site.register(GroupType)
admin.site.register(Patient)

# Register your models here.
