from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class KBBIData(models.Model):
	_id = models.AutoField(primary_key=True, default=1)
	katakunci = models.TextField()
	artikata = models.TextField()


	def __str__(self):
		return self.katakunci

	class Meta:
		db_table = 'datakata'
		verbose_name_plural = 'Data KBBI'
		app_label = 'kbbi'
		ordering = 'katakunci', 


	def escape_artikata(self):
		esc1 =  self.artikata.replace("&lt;", "<").replace("&gt;",">")
		esc2 = esc1.replace(";" , ";</br>")
		esc3 = esc2.replace("<b>1</b>", "</br><b>1</b>")
		return esc3
	escape_artikata.allow_tags = True


