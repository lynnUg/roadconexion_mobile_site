from django.contrib.auth.models import User
from django import forms

from django.db import models
# Create your models here.
TYPE_CHOICES=(
('Accident','Accident'),
('TrafficJam','TrafficJam'),
('RoadStatus','RoadStatus'),

)


class Report(models.Model):
    road_name = models.TextField(max_length=1000, blank=False)
    report= models.TextField(blank=False)
    type_report=models.CharField(max_length=1000,choices=TYPE_CHOICES,blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.road_name
class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['type_report', 'road_name', 'report']
        #exclude = ["user"]