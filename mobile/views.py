from django.template import RequestContext
from django.shortcuts import render_to_response
from mobile.models import Report,ReportForm 
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required 


#for the RESTful API
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from mobile.models import Report
from mobile.serializers import MobileSerializer
from django.http import Http404
from rest_framework.views import APIView
#from rest_framework import status
#
"mixins and generics for simpler classes"
#from rest_framework import mixins
#from rest_framework import generics
#END OF RESTFUL API

@login_required
def submit_report(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    object_list=Report.objects.all().order_by('-created_on')
    print "here1"
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        p=request.POST
        print p
        Report_form = ReportForm(request.POST)
        # If the two forms are valid...
        if Report_form.is_valid():
            print "here3"
            # Save the user's form data to the database.
            the_report=Report(road_name=p['road_name'],report=p['report'],type_report=p['type_report'],user=request.user)
            the_report.save()
            return render_to_response(
            'posts.html',
            {'object_list':object_list},
            context)

        else:
            print "here",ReportForm.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        Report_form = ReportForm()

    # Render the template depending on the context.
    return render_to_response(
            'report.html',
            {'form':Report_form},
            context)

def search(request):
	context = RequestContext(request)
	object_list=Report.objects.all()
	if request.method == 'POST':

		 starts_with=request.POST['road_name']
		 object_list=Report.objects.filter(road_name__icontains=starts_with).order_by('-created_on')
		 return render_to_response(
            'posts.html',
            {'object_list':object_list},
            context)
	return render_to_response(
            'posts.html',
            {'object_list':object_list},
            context)
def follow(request):
	context = RequestContext(request)
	object_list=Report.objects.all().order_by('-created_on')
	return render_to_response(
            'posts.html',
            {'object_list':object_list},
            context)
@login_required
def report(request):
	context = RequestContext(request)
	Report_form = ReportForm()
	return render_to_response(
            'report.html',
            {'form':Report_form},
            context)
def reports_sorted(request,report_type):
    context = RequestContext(request)
    object_list=Report.objects.filter(type_report=report_type).order_by('-created_on')
    return render_to_response(
            'posts.html',
            {'object_list':object_list},
            context)
@login_required
def profile(request):
    print "email", request.user.username
    object_list=Report.objects.filter(user=request.user).order_by('-created_on')
    return render_to_response("profile.html",{'object_list':object_list},context_instance=RequestContext(request))
@login_required
def delete(request,pk):
    report = Report.objects.filter(pk=int(pk))
    report.delete()
    object_list=Report.objects.filter(user=request.user).order_by('-created_on')
    return render_to_response("profile.html",{'object_list':object_list},context_instance=RequestContext(request))


#we dont need this class anymore
#class JSONResponse(HttpResponse):
 #   """
  #  An HttpResponse that renders its content into JSON.
   # """
    #def __init__(self, data, **kwargs):
     #   content = JSONRenderer().render(data)
      #  kwargs['content_type'] = 'application/json'
       # super(JSONResponse, self).__init__(content, **kwargs)


#@csrf_exempt
#@api_view(['GET', 'POST'])
#def report_list(request, format=None):

#we comment this class out, since we have simplified it below using generics
class ReportList(APIView):
    """
    List all code reports, or create a new report.
    """
    
    def get(self, request, format=None):
        report = Report.objects.all()
        serializer = MobileSerializer(report, many=True)
        #return Response(serializer.data)
        return Response({'reports': serializer.data})

    def post(self, request, format=None):
        serializer = MobileSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#simpler
#class ReportList(generics.ListCreateAPIView):
#    queryset = Report.objects.all()
#    serializer_class = MobileSerializer



#@csrf_exempt
#@api_view(['GET', 'PUT', 'DELETE'])
#def report_detail(request, pk, format=None):

#we comment this class out, since we have simplified it below using generics
class ReportDetail(APIView):
          
    """
    Retrieve, update or delete a report.
    """
  

    def get_object(self, pk):
        try:
            return Report.objects.get(pk=pk)
        except Report.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = MobileSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = MobileSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#simpler
#class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Report.objects.all()
#    serializer_class = MobileSerializer


 
