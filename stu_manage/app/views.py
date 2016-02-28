# -*- coding: utf-8 -*-
from django.shortcuts import render
from app.forms import UploadFileForm
from django.shortcuts import render_to_response
import xlrd
from django.db import connection,transaction
from django.http import HttpResponse,HttpResponseRedirect
from app.models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import csv
import Image
from app.UserAuth import UserAuth
from app.dict import *
import MySQLdb
from django.db.models import Q
import datetime 

def handle_upload_file(name):
	try:
		data=xlrd.open_workbook('/home/stu_manage/static/upload/excel/%s'%name)
	except Exception:
		return 1
	table = data.sheet_by_index(0)
	if not table.row_values(0)[0]==u'学号':
		return 1
	sql='update information set '
	error_list=[]
	l=[]
	for i in range(1,table.ncols):
		topic=table.row_values(0)[i]
		str1=stu_dict.get(topic)
		if str1:
			l.append(str1+"= %s")
		else:
			error_list.append(i)
	sql=sql+','.join(l)+"  where stu_id = %s"

	conn = MySQLdb.connect(user='root',passwd='weigu)(*',db='tp_stu_home',charset='utf8')
	cursor = conn.cursor()
	condition=[]
	for k in range(1,table.nrows):
		list_con=table.row_values(k)
               	for j in error_list:
                       list_con[j]='wu_nei_rong'
                for j in error_list:
                       list_con.remove('wu_nei_rong')
		list1=list_con[1:]
		list1.append(list_con[0])
		condition.append(list1)
	cursor.executemany(sql,condition)
	cursor.close()
	conn.commit()
	conn.close()
	return 0
	
def upload(request):
	try:
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	auth= UserAuth(uid).is_auth()	
	if not auth:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	if request.method == "POST":
		form = UploadFileForm(request.POST,request.FILES)
		name= datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")+request.FILES['files'].name.encode('utf8')	
		typ=request.FILES['files'].name.split('.')[1]
		if not (typ=='xls' or typ=='xlsx'):
			return  HttpResponse("<h1>上传失败 只能上传excel文件</h1></br><a href='upload'>返回重新上传</a>")
		if form.is_valid():
			files = open('/home/stu_manage/static/upload/excel/%s'%name,'w+')
			for chunk in request.FILES['files'].chunks():
				files.write(chunk)
			files.close()
			up_suc=handle_upload_file(name)
			if up_suc :
				q=u"上传失败，请以学号为第一列！"
			else:
				q=u"上传成功！"
			form = UploadFileForm()
			return render_to_response('upload.html', {'form': form,'q':q})
	else :
		form = UploadFileForm()
	return render_to_response('upload.html', {'form': form})


	
def entrance(request):
	l=[1,2,3,4,65,69]
	try:	
		password = request.COOKIES['me_key']
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	if not User.objects.get(uid=uid).password==password:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	auth = UserAuth(uid).is_auth()
	mem = UserAuth(uid).is_member()
	if auth:
		return HttpResponseRedirect('manage/')
	else:	
		if mem:
			href="http://www.me.uestc.edu.cn:8888/app/information"
			return HttpResponseRedirect(href)
	response="<h1 style='text-align:center;' >抱歉，本网站暂时只对本科生开放/h1>"
	return HttpResponse(response)

def manage(request):
	try:
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	auth=UserAuth(uid).is_auth()
	if not auth:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	label=[]
	stuid=request.GET.get('stuid','')
	page_size=14
	after_range_num = 3
	before_range_num = 3 
	if  stuid:
		student=Information.objects.filter(Q( stu_id__contains = stuid ) | Q( name__contains = stuid ))	
	else:
		student= Information.objects.all()
 	for i in student:
		q="http://www.me.uestc.edu.cn:8888/app/information/?uid=" +str(i.uid)
		i.set_url(q) 
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
 		page = 1  
	paginator = Paginator(student,page_size)
	try:
		students = paginator.page(page)
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		students = paginator.page(1)
	if page >= after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]
	if request.POST.getlist('choose',''):
		condition=request.POST.get('condition','2')
		row=request.POST.getlist('choose')
		first_row=[]
		for i in row:
			first_row.append(name_dict.get(i).encode('utf8'))	
		response = HttpResponse(content_type='text/csv')  
		response['Content-Disposition'] = 'attachment; filename=stu_list.csv'  
		writer = csv.writer(response) 
		writer.writerow(first_row)
		cursor = connection.cursor()
		sql='select '+','.join(row)+" from information where stu_id like '%s%%'  or name like '%%%s%%' "
		q=cursor.execute(sql%(condition,condition))
		for i in cursor.fetchmany(q):
			l=[]
			for k in i:
				if not k:
					k=u'无'
				l.append(k.encode('utf8'))
			writer.writerow(l)
		return response 
	return	render_to_response('manage.html', {'students': students,"page_range":page_range,"auth":auth,"stuid":stuid})

def information(request):
	try:
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	auth=UserAuth(uid).is_auth()
	if request.GET.get('uid', ''):
		if auth:
			uid = request.GET.get('uid')
	cursor = connection.cursor()
	l=cursor.execute("select portrait from portrait where uid = '%s'"%uid)
	img=''
	if l:
		img=cursor.fetchmany(1)[0][0]
	stu=Information.objects.get(uid=uid)
	return render_to_response('information.html', {'auth':auth,'img':img,'stu':stu})


def submit(request):
	try:
		uid=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	stu=Information.objects.get(uid=uid)
	if request.method == 'POST':
		file_obj = request.FILES.get('file')
		if file_obj:
			try:
				image = Image.open(file_obj)
			except IOError:
				return HttpResponse("<h1>上传失败，只能上传图片哦</h1>")
			image = image.resize((120,144),Image.ANTIALIAS)
			fname= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S-")+str(uid)+'.jpg'
			image_name = "/static/upload/portrait/"+fname
			image.save(open('/home/stu_manage/static/upload/portrait/'+fname,'w+'), format="JPEG")
			cursor = connection.cursor()
			cursor.execute("update portrait set portrait ='%s' where uid = %s "% (image_name,uid))
		l=[]
		values=[]
		sql='update information set '
		for key in request.POST:
			if key=='file':
				continue
			if not request.POST.get(key)=='':
				l.append(key+" = '%s'"%request.POST.get(key))
		if l:	
			sql=sql+','.join(l)+"  where uid = '%s'"%uid
			cursor = connection.cursor()
			cursor.execute(sql)
		return HttpResponseRedirect('information/')
	return render_to_response('submit.html',{'stu':stu,})

def record(request):
	try:
		uid1=request.COOKIES['me_uid']
	except KeyError:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	auth=UserAuth(uid1).is_auth()
	if not auth:
		return HttpResponseRedirect('http://www.me.uestc.edu.cn/stu/index.php/Login/')
	uid = request.GET.get('uid', '')
	stu=Information.objects.get(uid=uid)
	if request.method == 'POST':	
		l=[]	
		sql='update information set '
		for key in request.POST:
			if not request.POST.get(key)=='':
				l.append(key+" = '%s'"%request.POST.get(key))
		if l:
			sql=sql+','.join(l)+"  where uid = '%s'"%uid
			cursor = connection.cursor()
			cursor.execute(sql)
			return HttpResponseRedirect('http://www.me.uestc.edu.cn:8888/app/information/?uid=%s'%uid)
	return render_to_response('record.html',{'stu':stu})
