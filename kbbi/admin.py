from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
from django.contrib.auth.models import Group

# Register your models here.

class KBBIDataAdmin(admin.ModelAdmin):

	list_display = 'katakunci', 'arti_kata'
	search_fields = 'katakunci',

	def arti_kata(self, obj):
		return mark_safe(obj.artikata)
	arti_kata.allow_tags = True

admin.site.register(KBBIData, KBBIDataAdmin)
admin.site.unregister(Group)
