from django.contrib.auth.models import User
from django.forms import widgets
from django import forms
from mobile.models import Report
from rest_framework import serializers ,pagination
from mobile.models import models, LANGUAGE_CHOICES, STYLE_CHOICES



#the choices for TYPE_CHOICES

# Create your models here.
TYPE_CHOICES=(
('Accident','Accident'),
('TrafficJam','TrafficJam'),
('RoadStatus','RoadStatus'),

)

#class roadtrackerserializer

class MobileSerializer(serializers.ModelSerializer):
    user=serializers.RelatedField(many=False)
    #the required forms ,we reduce on reusing forms by using this meta class
    class Meta:
        model = Report
        fields = ('road_name', 'report', 'type_report', 'created_on', 'user')


    #comment all this out to reduce reusing data
    # road_name = models.TextField(max_length=1000, blank=False)
    # report= models.TextField(blank=False)
    # type_report=models.CharField(max_length=1000,choices=TYPE_CHOICES,blank=False)
    #  created_on = models.DateTimeField(auto_now_add=True)
    
    #comment this out, since its a foreign key and im testing,,, uncomment when not using
    #user = models.ForeignKey(User)


  #  def restore_object(self, attrs, instance=None):
   
        """
        Create or update a new Roadtracker instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
   #     if instance:
            # Update existing instance
    #        instance.road_name = attrs.get('road_name', instance.road_name)
     #       instance.report = attrs.get('report', instance.report)
      #      instance.type_report = attrs.get('type_report', instance.type_report)
       #     instance.created_on = attrs.get('created_on', instance.created_on)
            #comment out the user_id since im testing
            #instance.user = attrs.get('user', instance.user)
        #    return instance

        # Create new instance
        #return Roadtracker(**attrs)

class PaginatedMobileSerializer(pagination.PaginationSerializer):
    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = MobileSerializer