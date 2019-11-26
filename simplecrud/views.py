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
	#read all data from database
	data = describe.objects.all()
	return render(request, 'read.html', {'readalldata':data})

#create new data into database
def createdata(request):
	#when user create new data
	if request.method == 'POST':
		#process : 
		#1. initialize form to save new data into database
		if insertdata.is_valid():			
			#2. save data into database and return to read.html
			return redirect('readdata')
		else:
			#3. when data can't save into database
			return redirect('createdata')
		#end process
	else:
		#load view for create data
		return render(request, 'create.html', {'create':insertdata})

#update data that choose by user
def updatedata(request, id):
	if request.method == 'POST':
		#process : 
		# find id to set id and prepare update data into database
		if updateData.is_valid():			
			#update data into database and return to read.html
			return redirect('readdata')
		else:
			#return into update.html
			return render(request, 'update.html', {'updatedata':showpage, 'getdata':getdata})
		#end process
	else:
		#find id to get data from database
		#load view for edit data
		return render(request, 'update.html', {'updatedata':showpage, 'getdata':getdata})
	
#delete data that choose by user
def deletedata(request, id):
	#find id from database
	if request.method == 'POST':
		#delete data and return into read.html
		return redirect('readdata')
	
	#load view for delete data
	return render(request, 'delete.html', {'deletedata':deletedata})
