from django.template import RequestContext
from django.shortcuts import render_to_response
from mobile.models import Report,ReportForm 
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required 
def submit_report(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
   
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
            {'form':ReportForm},
            context)

        else:
            print "here",ReportForm.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        the_report = ReportForm()

    # Render the template depending on the context.
    return render_to_response(
            'report.html',
            {'form':ReportForm},
            context)
def search(request):
	context = RequestContext(request)
	object_list=Report.objects.all()
	if request.method == 'POST':

		 starts_with=request.POST['road_name']
		 object_list=Report.objects.filter(road_name__startswith=starts_with)
		 return render_to_response(
            'posts.html',
            {'object_list':object_list},
            context)
	return render_to_response(
            'posts.html',
            {'object_list':object_list},
            context)