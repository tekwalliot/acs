from django.shortcuts import render
from .models import SiteDetails, SiteData, homeid
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import date, datetime, timedelta
from django.db.models import Sum, Avg

import json

from django.views.decorators.csrf import csrf_exempt

from random import randint


# Create your views here.
@login_required
def home(request):

	xaxis=[]
	yaxis=[]
	count = SiteDetails.objects.count()
	# sitedtls = SiteDetails.objects.all()[randint(0, count - 1)]
	sitedtls = SiteDetails.objects.all()[randint(0, count - 1)]

	sitermsID = sitedtls.rmsId
	homeid.objects.filter(id=1).update(homeId=sitermsID)

	try:
		sitedata = SiteData.objects.filter(rmsId=sitermsID).latest('Date')
	except SiteData.DoesNotExist:
		return HttpResponse('<h2>This Customer Do Not Have Any Data</h2>')

	
#automatic date change (cuurent past 90 days)
	today_date = date.today()-timedelta(days=1)
	#print(today_date)
	past_date = sitedata.Date

	if (past_date != today_date): 
		delta_date = today_date-past_date
		delta_days =  delta_date.days
		#print(today_date+timedelta(days=delta_days))

		y=SiteData.objects.filter(rmsId=sitermsID)
		for x in y:
			x.Date = x.Date+timedelta(days=delta_days)
			x.save()

		sitedata = SiteData.objects.filter(rmsId=sitermsID).latest('Date')
			
	y = sitedata.lpd
	while y==0:
		newdate = sitedata.Date - timedelta(days=1)
		#print(newdate)
		sitedata = SiteData.objects.filter(rmsId=sitermsID) & SiteData.objects.filter(Date=newdate)
		sitedata = sitedata.latest('Date')
		y = sitedata.lpd


	sitedata_chart = SiteData.objects.filter(rmsId=sitermsID)

	for x in sitedata_chart:
		xaxis.append(str(x.Date))
		yaxis.append(x.dcenergy)


	return render(request, 'index.html', {'sitedtls': sitedtls, 'sitedata': sitedata, 'xaxis': xaxis, 'yaxis': yaxis})

@login_required
def index1(request):

	xaxis=[]
	yaxis=[]

	getid = homeid.objects.get(id=1)
	sitermsID = getid.homeId
	sitedtls = SiteDetails.objects.get(rmsId=sitermsID)



	try:
		sitedata = SiteData.objects.filter(rmsId=sitermsID).latest('Date')
	except SiteData.DoesNotExist:
		return HttpResponse('<h2>This Customer Do Not Have Any Data</h2>')

	y = sitedata.lpd
	while y==0:
		newdate = sitedata.Date - timedelta(days=1)
		#print(newdate)
		sitedata = SiteData.objects.filter(rmsId=sitermsID) & SiteData.objects.filter(Date=newdate)
		sitedata = sitedata.latest('Date')
		y = sitedata.lpd

	sitedata_chart = SiteData.objects.filter(rmsId=sitermsID)

	for x in sitedata_chart:
		xaxis.append(str(x.Date))
		yaxis.append(x.lpd)


	return render(request, 'index1.html', {'sitedtls': sitedtls, 'sitedata': sitedata, 'xaxis': xaxis, 'yaxis': yaxis})

@login_required
def search(request):
	if request.method=="POST":

		id_no=request.POST['idno']
		homeid.objects.filter(id=1).update(homeId=id_no)

		try:
			sitedtls = SiteDetails.objects.get(rmsId=id_no)
		except SiteDetails.DoesNotExist:
			return HttpResponse('<h2>Enter ID Before Hit Search Button or No Data Available for searched ID</h2>')

		try:
			sitedata = SiteData.objects.filter(rmsId=id_no).latest('Date')
		except SiteData.DoesNotExist:
			return HttpResponse('<h2>Customer/Entered ID Does Not Exists</h2>')

#automatic date change (cuurent past 90 days)
		today_date = date.today()-timedelta(days=1)
		past_date = sitedata.Date

		if (past_date != today_date): 
			delta_date = today_date-past_date
			delta_days =  delta_date.days
			#print(today_date+timedelta(days=delta_days))

			y=SiteData.objects.filter(rmsId=id_no)
			for x in y:
				x.Date = x.Date+timedelta(days=delta_days)
				x.save()

		sitedata = SiteData.objects.filter(rmsId=id_no).latest('Date')

		y = sitedata.lpd
		while y==0:
			newdate = sitedata.Date - timedelta(days=1)
			print(newdate)
			sitedata = SiteData.objects.filter(rmsId=id_no) & SiteData.objects.filter(Date=newdate)
			sitedata = sitedata.latest('Date')
			y = sitedata.lpd

		sitedata_chart = SiteData.objects.filter(rmsId=id_no)

		xaxis=[]
		yaxis=[]

		for x in sitedata_chart:
			xaxis.append(str(x.Date))
			yaxis.append(x.dcenergy)

		return render(request, 'index.html', {'sitedtls': sitedtls, 'sitedata': sitedata, 'xaxis': xaxis, 'yaxis': yaxis})
	else:
		return HttpResponse('<h2>Customer/Entered ID Does Not Exists</h2>')


@login_required
def genreports(request):
	table_data = SiteDetails.objects.all()
	return render(request, 'reports.html', {'table_data': table_data})

@login_required
def openId(request, rmsid):

	sitedtls = SiteDetails.objects.get(rmsId=rmsid)
	try:
		sitedata = SiteData.objects.filter(rmsId=rmsid).latest('Date')
	except SiteData.DoesNotExist:
		return HttpResponse('<h2>This Customer Do Not Have Any Data</h2>')

	#automatic date change (cuurent past 90 days)
	today_date = date.today()-timedelta(days=1)
	past_date = sitedata.Date

	if (past_date != today_date): 
		delta_date = today_date-past_date
		delta_days =  delta_date.days
		#print(today_date+timedelta(days=delta_days))

		y=SiteData.objects.filter(rmsId=rmsid)
		for x in y:
			x.Date = x.Date+timedelta(days=delta_days)
			x.save()

		sitedata = SiteData.objects.filter(rmsId=rmsid).latest('Date')

	y = sitedata.lpd
	while y==0:
		newdate = sitedata.Date - timedelta(days=1)
		print(newdate)
		sitedata = SiteData.objects.filter(rmsId=rmsid) & SiteData.objects.filter(Date=newdate)
		sitedata = sitedata.latest('Date')
		y = sitedata.lpd
		
	sitedata_chart = SiteData.objects.filter(rmsId=rmsid)
	homeid.objects.filter(id=1).update(homeId=rmsid)

	xaxis=[]
	yaxis=[]

	for x in sitedata_chart:
		xaxis.append(str(x.Date))
		yaxis.append(x.dcenergy)
	return render(request, 'index.html', {'sitedtls': sitedtls, 'sitedata': sitedata, 'xaxis': xaxis, 'yaxis': yaxis})

@login_required
def datarep(request):
	try:
		getid = homeid.objects.get(id=1)
		rmsid = getid.homeId
		table_data = SiteData.objects.filter(rmsId=rmsid)
		sitedtls = SiteDetails.objects.get(rmsId=rmsid)
		nDays = SiteData.objects.filter(rmsId=rmsid).count()
		tEnergy = SiteData.objects.filter(rmsId=rmsid).aggregate(Sum('dcenergy')).get('dcenergy__sum')
		tHrs = SiteData.objects.filter(rmsId=rmsid).aggregate(Sum('prthrs')).get('prthrs__sum')
		tLpd = SiteData.objects.filter(rmsId=rmsid).aggregate(Sum('lpd')).get('lpd__sum')

	except SiteData.DoesNotExist:
			return HttpResponse('<h2>No Data Available With This Paricular ID</h2>')
	return render(request, 'datareport.html', {'table_data': table_data, 'sitedtls': sitedtls, 'nDays': nDays, 'tEnergy': tEnergy, 'tHrs': tHrs, 'tLpd': tLpd})

@login_required
def datarep1(request):
	if request.method=="POST":

		id_no=request.POST['idno']
		homeid.objects.filter(id=1).update(homeId=id_no)

		try:
			sitedtls = SiteDetails.objects.get(rmsId=id_no)
		except SiteDetails.DoesNotExist:
			return HttpResponse('<h2>Enter ID Before Hit Search Button</h2>')

		try:
			table_data = SiteData.objects.filter(rmsId=id_no).latest('Date')
		except SiteData.DoesNotExist:
			return HttpResponse('<h2>Customer/Entered ID Does Not Exists</h2>')

		#automatic date change (cuurent past 90 days)
		today_date = date.today()-timedelta(days=1)
		past_date = table_data.Date

		if (past_date != today_date): 
			delta_date = today_date-past_date
			delta_days =  delta_date.days
			#print(today_date+timedelta(days=delta_days))

			y=SiteData.objects.filter(rmsId=id_no)
			for x in y:
				x.Date = x.Date+timedelta(days=delta_days)
				x.save()

		table_data = SiteData.objects.filter(rmsId=id_no)

		nDays = SiteData.objects.filter(rmsId=id_no).count()
		tEnergy = SiteData.objects.filter(rmsId=id_no).aggregate(Sum('dcenergy')).get('dcenergy__sum')
		tHrs = SiteData.objects.filter(rmsId=id_no).aggregate(Sum('prthrs')).get('prthrs__sum')
		tLpd = SiteData.objects.filter(rmsId=id_no).aggregate(Sum('lpd')).get('lpd__sum')


		return render(request, 'datareport.html', {'table_data': table_data, 'sitedtls': sitedtls, 'nDays': nDays, 'tEnergy': tEnergy, 'tHrs': tHrs, 'tLpd': tLpd})
	else:
		return HttpResponse('<h2>Customer/Entered ID Does Not Exists</h2>')



@login_required
def ac5hprep(request):
	try:
		table_data = SiteDetails.objects.filter(capacity='5HP AC')
	except SiteDetails.DoesNotExist:
			return HttpResponse('<h2>No Data Available With This Paricular Project</h2>')
	return render(request, 'reports.html', {'table_data': table_data})

@login_required
def ac3hprep(request):
	try:
		table_data = SiteDetails.objects.filter(capacity='3HP AC')
	except SiteDetails.DoesNotExist:
			return HttpResponse('<h2>No Data Available With This Paricular Project</h2>')
	return render(request, 'reports.html', {'table_data': table_data})

# def logoutpage(request):
#     logout(request)
#     return redirect('genrep')

# def dayR(request):
# 	table_data = dd.objects.all()
# 	return render(request, 'dayR.html', {'table_data': table_data})

# def monthR(request):
# 	table_data = md.objects.all()
# 	return render(request, 'monthR.html', {'table_data': table_data})

# def openId(request, System_RID_No):
# 	xaxis=[]
# 	yaxis=[]
# 	chart_data = dd.objects.filter(System_RID_No=System_RID_No).order_by('Date')[:10]

# 	for x in chart_data:
# 		xaxis.append(str(x.Date))
# 		yaxis.append(x.Inverter_Output_KWH)

# 	id_no = System_RID_No

# 	t_GPower = dd.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Gross_KWH')).get('Gross_KWH__sum')
# 	t_InvPower = dd.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Inverter_Output_KWH')).get('Inverter_Output_KWH__sum')
# 	t_PumpPower = dd.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Pump_Consumption_KWH')).get('Pump_Consumption_KWH__sum')
# 	t_PumpLtrs = dd.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Water_Discharge_Lts')).get('Water_Discharge_Lts__sum')
# 	return render(request, 'index.html', {'xaxis': xaxis, 'yaxis': yaxis, 'id_no':id_no, 't_GPower': t_GPower, 't_InvPower': t_InvPower, 't_PumpPower': t_PumpPower, 't_PumpLtrs': t_PumpLtrs})

# @csrf_exempt
# def GetInvDaysData(request):
#     ddata=json.loads(request.body)
#     # start_date=datetime.strptime(request.GET["start"],"%Y-%m-%d")
#     #end_date=datetime.strptime(request.GET["end"],"%Y-%m-%d")+timedelta(days=1)
#     # d = datetime.strptime(request.POST['TestDate'],"%Y-%m-%d").date()
#     d = datetime.strptime(ddata["TestDate"],"%Y-%m-%d").date()
#     p = ddata['ProjectName']
#     c=datetime.now().date()
#     #print(d)
                
#     if d<c :
#         data = list(dd.objects.filter(Date__startswith=d, Project=p).values('Project','System_RID_No','Date','RunTime_Hrs','Water_Discharge_Lts','Pump_Consumption_KWH','Inverter_Input_KWH','Inverter_Output_KWH','Total_KWH_Generation','Gross_KWH'))
#         return JsonResponse({'Day Wise Data': data})
#     else:
#         return HttpResponse('<h1>Inavalid Date Request<h1>')
#     #else:
#         #return HttpResponse('Error!')

# @csrf_exempt
# def GetInvMonthData(request):
#     ddata=json.loads(request.body)
#     d = datetime.strptime(ddata["TestDate"],"%Y-%m-%d").date()
#     p = ddata['ProjectName']

#     data = list(md.objects.filter(Date__startswith=d, Project=p).values('Project','System_RID_No','Date','RunTime_Hrs','Water_Discharge_Lts','Pump_Consumption_KWH','Inverter_Input_KWH','Inverter_Output_KWH','Total_KWH_Generation','Gross_KWH'))
#     return JsonResponse({'Month Wise Data': data})
# def search(request):
# 	if request.method=="POST":

# 		id_no=request.POST['idno']

# 		xaxis=[]
# 		yaxis=[]
# 		chart_data = dd.objects.filter(System_RID_No=id_no).order_by('Date')[:10]

# 		for x in chart_data:
# 			xaxis.append(str(x.Date))
# 			yaxis.append(x.Inverter_Output_KWH)

# 		t_GPower = dd.objects.filter(System_RID_No=id_no).aggregate(Sum('Gross_KWH')).get('Gross_KWH__sum')
# 		t_InvPower = dd.objects.filter(System_RID_No=id_no).aggregate(Sum('Inverter_Output_KWH')).get('Inverter_Output_KWH__sum')
# 		t_PumpPower = dd.objects.filter(System_RID_No=id_no).aggregate(Sum('Pump_Consumption_KWH')).get('Pump_Consumption_KWH__sum')
# 		t_PumpLtrs = dd.objects.filter(System_RID_No=id_no).aggregate(Sum('Water_Discharge_Lts')).get('Water_Discharge_Lts__sum')
# 		return render(request, 'index.html', {'xaxis': xaxis, 'yaxis': yaxis, 'id_no':id_no, 't_GPower': t_GPower, 't_InvPower': t_InvPower, 't_PumpPower': t_PumpPower, 't_PumpLtrs': t_PumpLtrs})
# 	else:
# 		return render(request, 'index.html')
