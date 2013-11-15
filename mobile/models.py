from django.contrib.auth.models import User 
# Create your models here.
TYPE_CHOICES=(
('Accident','Accident'),
('Traffic_Jam','Traffic_Jam'),
('Repair','Repair'),
('Status','Status'),

)
class Report(models.Model):
    road_name = models.CharField(max_length=128, unique=True)
    report= models.TextField(blank=False)
    type_report=models.CharField(max_length=200,choices=TYPE_CHOICES,blank=False)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.road_name