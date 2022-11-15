import os
from datetime import date, datetime, timedelta

from django.contrib.sessions.models import Session
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import (TblCasedetails, TblCases, TblCasesummary, TblCompany,
                     TblDocuments, TblPriority, TblUser)


# Create your views here.
def login(request):
    
    return render(request,'webpages/login.html')
def login_check(request):
    error_message=""
    username=request.POST.get('username')
    password=request.POST.get('password')
    is_user=TblUser.objects.filter(username=username).exists()
    print("Is user====",is_user)

    if is_user:
        user_details=TblUser.objects.filter(username=username).get()
        userpassword=user_details.password
        print("Userpassword===",userpassword)
        if(userpassword==password):
            print("User exists=====")
            print("User details=====",user_details.userid)
            request.session['UserID']=user_details.userid
            request.session['UserName']=user_details.username
            request.session['Email']=user_details.designationid
            request.session['CompanyID']=user_details.companyid
            request.session['Name']=user_details.name
            request.session['MemberType']=user_details.membertype
            return redirect('dashboard/')
            
        else:
            error_message="Incorrect Password"
            return render(request,'webpages/login.html',{'login_error':error_message})
    else:
        error_message="User not exists"
        return render(request,'webpages/login.html',{'login_error':error_message})
        
def dashboard(request):
    if 'UserID' in request.session:
        userid=request.session.get('UserID')
        membertype=request.session.get('MemberType')
        if membertype=="ADMIN":
            approvalpending=TblCases.objects.filter(status="Management Approval Pending").count()
            return render(request,'webpages/admindashboard.html',{'pending':approvalpending})
        else:
            pending=TblCases.objects.filter(status="Pending",assignedto=userid).count()
            completed=TblCases.objects.filter(status="Completed",assignedto=userid).count()
            reopen=TblCases.objects.filter(status="ReOpen",assignedto=userid).count()
            total=TblCases.objects.filter(assignedto=userid).count()
            return render(request,'webpages/dashboard.html',{'pending':pending,'completed':completed,'reopen':reopen,'total':total})
    else:
        return render(request,'webpages/login.html')
def view_tasks(request):
    if 'UserID' in request.session:
        fromdate=request.GET.get('from')
        todate=request.GET.get('to')
        status=request.GET.get('status')
        print("Status=====",status)
        userid=request.session.get('UserID')
        membertype=request.session.get('MemberType')
        priority=TblPriority.objects.all()
        employees=TblUser.objects.exclude(userid=userid).filter(membertype__in=["SUPER USER","ADMIN","ASSIGNEE"])
        print("From date To date=====",fromdate,todate,userid)
        if(status!=None):
                print("Status not none")
                if(membertype=="SUPER USER"):
                    cases=TblCases.objects.filter(status=status)
                else:
                    cases=TblCases.objects.filter(status=status,assignedto=userid)
                
        if(((fromdate!=None and todate!=None) ) and status==None ):
            print("From")
            if(membertype=="SUPER USER" ):
                    cases=TblCases.objects.filter(modified__gte=fromdate,modified__lt=todate)
            else:
                    cases=TblCases.objects.filter(modified__gte=fromdate,modified__lt=todate,assignedto=userid)
            
        if(fromdate==None and todate==None and status==None):
            if(membertype=="SUPER USER" ):
                cases=TblCases.objects.all() 
            else:
                cases=TblCases.objects.filter(assignedto=userid) 
        return render(request,'webpages/tasklist.html',{'cases':cases,'priority':priority,'employees':employees})
        # print("Cases====",list(cases))
        # return JsonResponse(cases,safe=False)
    else:
        return redirect('/login')

def detailed_page(request):
    if 'UserID' in request.session:
        case=request.GET.get('Case')
        print("Case details===="+case) 
        casedetails=TblCasedetails.objects.filter(caseid=case)
        docdetails=TblDocuments.objects.filter(caseid=case)
        activities=[]
        for details in casedetails:
            print("Case detail Id====",details.casedetailid)
            activity=TblCasesummary.objects.filter(casedetailid=details.casedetailid).order_by('-modified')
            print("Activity======",activity)
            activities.append(activity)
        print("Activities====",activities)
        return render(request,'webpages/details.html',{"details":casedetails,"docs":docdetails,"activities":activities})
    else:
        return redirect('/login')

def status_update(request):
    if 'UserID' in request.session:
        caseid=request.GET.get('id')
        status=request.GET.get('status')
        description=request.GET.get('description')
        
        case=TblCases.objects.get(caseid=caseid)
        case.status=status
        
        if(description!=""):
            case.description=description
        case.save()
        modified=datetime.now()
        registerdetail=TblCasedetails(caseid=case.caseid,topic=case.topic,description=case.description,regdate=case.regdate,modified=modified,iscompleted=0,completiondate=None,expcompletion=None,status=status,userid=case.assignedto,priority=case.priority,casetype=case.casetype)
        registerdetail.save()
        print("Case====",case)
        return JsonResponse({"message":"success"})
    else:
        return redirect('/login')
def detail_status_update(request):
    if 'UserID' in request.session:
        caseid=request.GET.get('id')
        status=request.GET.get('status')
        description=request.GET.get('description')
        
        case=TblCasedetails.objects.get(casedetailid=caseid)
        case.status=status
        
        # if(description!=""):
        #     case.description=description
        case.save()
        modified=datetime.now()
        desctime=modified.strftime("%d/%m/%Y %H:%M:%S")
        summaryname=request.session.get('Name')
        summarydesc=summaryname+" on "+desctime+":"+description
        summarydetail=TblCasesummary(casedetailid=caseid,description=summarydesc,regdate=modified,modified=modified)
        summarydetail.save()
        print("Case====",case)
        return JsonResponse({"message":"success"})
    else:
        return redirect('/login')
def reassign_task(request):
    if 'UserID' in request.session:
        caseid=request.GET.get('id')
        status=request.GET.get('status')
        description=request.GET.get('description')
        priority=request.GET.get('priority')
        assignto=request.GET.get('assignto')
        print("Deatails====",caseid,status,description,assignto)
        reassign=TblUser()
        priorityTbl=TblPriority()
        reassign.userid=assignto
        priorityTbl.id=priority
        print("Deatails====",caseid,status,description,priority)
        case=TblCases.objects.get(caseid=caseid)

        case.status=status
        case.assignedto=reassign
        if(description!=""):
            case.description=description
        case.priority=priorityTbl
        case.save()
        modified=datetime.now()
        registerdetail=TblCasedetails(caseid=case.caseid,topic=case.topic,description=case.description,regdate=case.regdate,modified=modified,iscompleted=0,completiondate=None,expcompletion=None,status=status,userid=case.assignedto,priority=case.priority,casetype=case.casetype)
        registerdetail.save()
        print("Case====",case)
        return JsonResponse({"message":"success"})
    else:
        return redirect('/login')
def view_document(request):
    if 'UserID' in request.session:
        docid=request.GET.get('id')
        imagedetail=TblDocuments.objects.filter(id=docid)
        contenttype=""
        imagetype=""
        imagename=""
        imagedata=""
        for detail in imagedetail:
            print("Image detail=====",detail.doctype)
            contenttype=detail.doctype
            imagetype=detail.doctype
            imagename=detail.documentname
            imagedata=detail.documentdata
        if(imagetype=="application/vnd.ms-word"):
                contenttype = ".doc"
        if(imagetype=="application/vnd.ms-word"):
            contenttype = ".docx"
        if(imagetype=="application/vnd.ms-excel"):
            contenttype = ".xls"
        if(imagetype=="application/vnd.ms-excel"):
            contenttype = ".xlsx"
        if(imagetype=="image/jpg"):
            contenttype =".jpg" 
        if(imagetype=="image/jpg"):
            contenttype = ".JPG"
        if(imagetype=="image/jpg"):
            contenttype = ".JPEG"
        if(imagetype=="image/jpg"):
            contenttype = ".jpeg"
        if(imagetype=="image/png"):
            contenttype = ".png"
        if(imagetype=="image/png"):
            contenttype =".PNG" 
            
        if(imagetype=="image/gif"):
            contenttype =".gif" 
                    
        if(imagetype=="image/gif"):
            contenttype =".GIF" 
        if(imagetype=="image/bmp"):
            contenttype = ".bmp"
        if(imagetype=="image/bmp"):
            contenttype = ".BMP"
        if(imagetype== "application/pdf"):
            contenttype = ".pdf"
        if(imagetype=="application/pdf"):
            contenttype = ".PDF"
        print("Content type====",contenttype)
        
        imagename=imagename
        files = os.listdir("static\\uploads\\")
        for f in files:
            os.remove("static\\uploads\\" + f)
        
        file_path="static\\uploads"+"\\"+imagename
        print("Image name=====",imagename)
        # with open('binary_file') as file: 
        #     data = file.read() 
        res = ''.join(format(x, '02x') for x in imagedata)
        result=str(res)
        data = bytes.fromhex(result) 
        with open(file_path, 'wb') as file: 
            file.write(data)
        # with open(file_path, 'r',errors='ignore') as file: 
        #     file_data=file.read()
        img = open(file_path, 'rb')
        response = FileResponse(img,as_attachment=False)
        response['Content-Disposition'] = 'inline; filename='+imagename
        return response
        # return render(request,"webpages/docs.html",{"imagepath":imagename})
    else:
        return redirect('/login')
def logout(request):
    try:
        UserId=request.session['UserID']
        del request.session['UserID']
    except:
        print("Exception")
   
    return redirect('login/')
def case_file_upload(request):
    if 'UserID' in request.session:
        detailid=request.POST.get('detailid')
        caseid=request.POST.get('caseid')
        print("Datas=====",detailid,caseid)
        # summary=TblCasesummary.objects.get(casedetailid=detailid)
        detail=TblCasedetails.objects.get(caseid=caseid)
        print("Detail======")
        detailid=detail.casedetailid
        print("Detailid===",detailid)
        docfile=request.FILES.get("docfile",None)
        if docfile:
            imagedata=None
            extension1 = os.path.splitext(str(docfile))[1]
            imagename=os.path.splitext(str(docfile))[0]
            print("Image name===",imagename)
            fullname=imagename+extension1
            print("Fullname==",fullname)
            contenttype=""
            file_path="static\\uploads\\"
                # file_path=os.path.join(UPLOAD_ROOT,accno)
            print("File existance======",file_path,os.path.isfile(file_path))
            if os.path.isfile(file_path):
                os.mkdir(file_path)
            fullpath=str(caseid)+extension1
            print("Full path====",fullpath)
            fullfilepath=os.path.join(file_path,fullpath)
            print("File",fullfilepath)
            with open(fullfilepath, 'wb+') as destination:
                for chunk in docfile.chunks():
                    imagedata=chunk
            
            if(extension1==".doc"):
                contenttype = "application/vnd.ms-word"
            if(extension1== ".docx"):
                contenttype = "application/vnd.ms-word"
            if(extension1==".xls"):
                contenttype = "application/vnd.ms-excel"
            if(extension1==".csv"):
                contenttype = "application/vnd.ms-excel"
            if(extension1==".xlsx"):
                contenttype = "application/vnd.ms-excel"
            if(extension1==".jpg"):
                contenttype = "image/jpg"
            if(extension1==".JPG"):
                contenttype = "image/jpg"
            if(extension1==".JPEG"):
                contenttype = "image/jpg"
            if(extension1==".jpeg"):
                contenttype = "image/jpg"
            if(extension1==".png"):
                contenttype = "image/png"
            if(extension1==".PNG"):
                contenttype = "image/png"
            if(extension1==".gif"):
                contenttype = "image/gif"
            if(extension1==".GIF"):
                contenttype = "image/gif"
            if(extension1==".bmp"):
                contenttype = "image/bmp"
            if(extension1==".BMP"):
                contenttype = "image/bmp"
            if(extension1== ".pdf"):
                contenttype = "application/pdf"
            if(extension1==".PDF"):
                contenttype = "application/pdf"
            
            print("Type odf imagedata===",type(imagedata))
            regdate =datetime.now()
            docs=TblDocuments(caseid=caseid,casedetailid=detailid,casesummaryid=0,documentdata=imagedata,documentname=fullname,doctype=contenttype,uploadeddate=regdate)
            docs.save()
    
        return JsonResponse({"message":"success"})
    else:
        return redirect('/login')

def viewall_users(request):
    users=TblUser.objects.all()
    company=TblCompany.objects.all()
    # priority=TblPriority.objects.get(id=5)
    # priority.delete()
    print("Priority=======")
    # priority.priority="risk"
    # priority.save()

    return render(request,'display.html',{'users':users,'companies':company})

