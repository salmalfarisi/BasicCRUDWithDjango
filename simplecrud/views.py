from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import FormData, DBForm, HiddenForm
from .models import describe
import datetime

#insert session message for django
from django.contrib import messages

# Create your views here.

#Read data from database
def readdata(request):
	data = describe.objects.all()
	return render(request, 'read.html', {'readalldata':data})

#create new data into database
def createdata(request):	
	if request.method == 'POST':
		insertdata = FormData(request.POST)
		if insertdata.is_valid():				
			now = datetime.datetime.now()
			savedata = describe()
			savedata.title = insertdata.cleaned_data['title']
			savedata.desc = insertdata.cleaned_data['desc']
			savedata.created_at = now
			savedata.updated_at = now
			savedata.save()
			return redirect('readdata')
		else:
			return redirect('createdata')
	else:
		insertdata = FormData()
		#view for create html
		return render(request, 'create.html', {'create':insertdata})

#update data that choose by user
def updatedata(request, id):
	if request.method == 'POST':
		getdata = describe.objects.get(id=id)
		updateData = HiddenForm(request.POST, instance=getdata)
		if updateData.is_valid():			
			now = datetime.datetime.now()
			updateData.title = updateData.cleaned_data['title']
			updateData.desc = updateData.cleaned_data['desc']
			updateData.updated_at = now
			updateData.save()
			return redirect('readdata')
		else:
			getdata = describe.objects.get(id=id)
			messages.add_message(request, messages.ERROR, 'Error While Update Data')
			updatedata = HiddenForm(instance=getdata)
			showpage = updatedata
			#view for edit data html
			return render(request, 'update.html', {'updatedata':showpage, 'getdata':getdata})
	else:
		getdata = describe.objects.get(id=id)
	
		updatedata = HiddenForm(instance=getdata)
		showpage = updatedata
		#view for edit data html
		return render(request, 'update.html', {'updatedata':showpage, 'getdata':getdata})
	
#delete data that choose by user
def deletedata(request, id):
	deletedata = describe.objects.get(id=id)
	
	if request.method == 'POST':
		deletedata.delete()
		return redirect('readdata')
	
	#view for delete html
	return render(request, 'delete.html', {'deletedata':deletedata})