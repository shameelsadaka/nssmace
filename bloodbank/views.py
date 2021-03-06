from django.http import HttpResponse
from django.shortcuts import render
from bloodbank.forms import PostForm
from django.forms import ModelForm
from bloodbank.models import Donor


def results(request):

	form = PostForm()

	location_filter = request.GET.get('location','')
	bloodtype_filter = request.GET.get('blood_type','')

	output = Donor.objects.filter(location__contains=location_filter,blood_type__contains=bloodtype_filter);

	return render(request, 'results.html', {'form':form,'output': output})
