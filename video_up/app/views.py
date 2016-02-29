# -*- coding: utf-8 -*-
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from pymongo import MongoClient
from  django  import  forms
from app.models import *
import datetime
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import json

algdict={'1':u"打架识别","2":u"入侵检测"}

def upload(request):
    if request.method == 'POST':
        video_name=request.FILES.get('file').name
        typ=video_name.split('.')[1]
        if not (typ=='mp4'):
		return  HttpResponse(json.dumps({'confirm':"N"}), content_type='application/json')
        client = MongoClient('localhost',10001)
        col=client.video_up.videos        
        file_obj=request.FILES.get('file')
        if file_obj:
        	video_url='static/videos/'+video_name
        	videos = open(video_url,'w+')
        	for chunk in request.FILES['file'].chunks():
        	        videos.write(chunk)
        	videos.close()
        	results={'confirm':"Y",'results':'01'}
        	post={"name":video_name,
        	"url":video_url,
        	"resukts":"re"}
        	col.save(post)
            	client.close()      
    		return HttpResponse(json.dumps(results), content_type='application/json')

def logView(request):
	check=datetime.datetime.now()-datetime.timedelta(seconds=1)
	#record=log.objects(name="test001").order_by("-datetime").first()
	record=log.objects(time__gte=a)
	results={}
	for k in record:
		results[k.cid]=k.result
	if record:
		results["update"]="Y"	
		return HttpResponse(json.dumps(results), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'update':"N"}), content_type='application/json')

def index1(request):
	try:
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('/login')
	configs=config.objects().order_by("cid")
	return render_to_response("index1.html",{'a':1,'configs':configs})

def index2(request):
	try:
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('/login')
	page_size=20
	after_range_num = 3
	before_range_num = 3 
	record=log.objects().order_by("-time")
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
 		page = 1  
	paginator = Paginator(record,page_size)
	try:
		records = paginator.page(page)
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		records = paginator.page(1)
	if page >= after_range_num:
		
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
		
	else:
		
		page_range = paginator.page_range[0:int(page)+before_range_num]		
	return render_to_response("index2.html",{'a':2,"records":records,"page_range":page_range})

def index3(request):
	try:
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('/login')
	configs=config.objects().order_by("cid")
	fightConfig=algConfig.objects(aid=1).first().config
	if request.method=="POST":
		if request.POST.get('fighting-confidence', ''):
			conlist=request.POST.get('fighting-confidence', '')
			algConfig.objects(aid=1).update_one(config={"Confidence":conlist})  
			fightConfig={"confidence":conlist}
		
	return render_to_response("index3.html",{"a":3,'configs':configs,'fightConfig':fightConfig})

def addconf(request):		
	if request.method=="POST":
		newconf=request.POST
		print newconf
		configs=config.objects().order_by("cid")
		flag=0
		for index in range(len(configs)):
			if index+1!=configs[index].cid:
				cid=index+1
				flag=1
				break
		if not flag:
			cid = len(configs)+1
		conflist=newconf.getlist("algorithm[]" )
		algname=[]
		for k in conflist:
			algname.append(algdict.get(k))
		insert=config(name=newconf.get("cameraName"),cid=cid,algorithm=conflist,address=newconf.get("cameraAddress"), prefix=newconf.get("addressPrefix"),suffix=newconf.get("addressSuffix"),algname=algname)
		insert.save()
		results={"cid":cid}	
		return HttpResponse(json.dumps(results), content_type='application/json')	
	return HttpResponseRedirect('http://127.0.0.1:8000/index3/')

def delconf(request):
	if request.method=="POST":
		newconf=request.POST
		print newconf
		delnum=newconf.get("cameraId")
		delconfig=config.objects(cid=delnum)
		if delconfig:
			delconfig.delete()
		results={"cid":delnum}	
		return HttpResponse(json.dumps(results), content_type='application/json')
	return  HttpResponseRedirect('http://127.0.0.1:8000/index3/')

def reconf(request):
	if request.method=="POST":
		newconf=request.POST
		print newconf
		renum=request.POST.get("cameraId")
		conflist=newconf.getlist("algorithm[]" )
		algname=[]
		for k in conflist:
			algname.append(algdict.get(k))
		config.objects(cid=renum).update_one(name=newconf.get("cameraName"),algorithm=conflist,address=newconf.get("cameraAddress"), prefix=newconf.get("addressPrefix"),suffix=newconf.get("addressSuffix"),algname=algname)  
		results={"cid":renum}	
		return HttpResponse(json.dumps(results), content_type='application/json')
	return  HttpResponseRedirect('http://127.0.0.1:8000/index3/')

def login(request):
	if request.method == 'POST':
		uid = request.POST.get('username', '')
		passwd = request.POST.get('userpassword', '')
		if uid=="admin" and passwd=="123456":
			response = HttpResponseRedirect('/index1')
			response.set_cookie("me_uid",uid,max_age=72000)
			return response
		else:
			return  render_to_response("login.html",{'wrong':1})
	else :
		return  render_to_response("login.html",{"wrong":0})
# Create your views here.
