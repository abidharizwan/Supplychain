from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import *


# Create your views here.

###ADMIN###

def loginadmin(request):
    return render(request, 'login.html')
def loginpost(request): #create post method to take data
    username=request.POST['textfield'] #create a variable name called username then create it's post method
    password=request.POST['textfield2']
    log=Login.objects.filter(username=username,password=password) #create object called log, filter is a method to filter records based on certain criteria.
    if log.exists(): #is a conditional statement that checks whether there are any records in the queryset log.
        log1=Login.objects.get(username=username,password=password)  #retrieving a single record from the Login table where the username and password match specific values.
        request.session['lid']=log1.id #assigns the value of the id field of the log1 object to a session variable named 'lid'.
        if log1.type=='admin':
            return HttpResponse('''<script>alert('welcome');window.location='/myapp/adminhome/'</script>''') #returns an HTTP response containing JavaScript code that displays an alert message and redirects the user's browser to another URL.
        if log1.type=='manufacture':
            return HttpResponse('''<script>alert('welcome');window.location='/myapp/manufacturehome/'</script>''') #returns an HTTP response containing JavaScript code that displays an alert message and redirects the user's browser to another URL.
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/myapp/loginadmin/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');window.location='/myapp/loginadmin/'</script>''')

def changepasswordadmin(request):
    return render(request,'admin/changepassword.html')
def changepasswordadminpost(request):
    Oldpassword=request.POST['textfield']
    Newpassword=request.POST['textfield2']
    Confirmpassword=request.POST['textfield3']
    log=Login.objects.filter(password=Oldpassword)  #take old password
    if log.exists(): #check oldpassword and enteringpassword are same or not
        log1=Login.objects.get(password=Oldpassword,id=request.session['lid']) # retrieving a single record from the Login model/table where both the password matches a specific value (Oldpassword) and the id matches a value stored in the session variable 'lid'.
        if Newpassword==Confirmpassword:
            log1 = Login.objects.filter(password=Oldpassword, id=request.session['lid']).update(password=Confirmpassword)


            return HttpResponse('''<script>alert('login successfull');window.location='/myapp/loginadmin/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/myapp/changepasswordadmin/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');window.location='/myapp/changepasswordadmin/'</script>''')



def viewsupplieradmin(request):
    obj=Supplier.objects.filter(status='pending') #pending values are stored in obj
    return render(request,'admin/verifysupplier.html',{'data':obj})

def viewsupplieradminpost(request):
    search=request.POST['textfield']
    obj = Supplier.objects.filter(status='pending',companyname__icontains=search)  # pending values are stored in obj
    return render(request, 'admin/verifysupplier.html', {'data': obj})


def supplierapprove(request,id):
    obj=Supplier.objects.filter(LOGIN=id).update(status='approved')
    obj1=Login.objects.filter(id=id).update(type='supplier')
    return HttpResponse('''<script>alert('successfully approved');window.location='/myapp/viewsupplieradmin/'</script>''')

def supplierreject(request,id):
    obj=Supplier.objects.filter(LOGIN=id).update(status='reject')
    obj1=Login.objects.filter(id=id).update(type='pending')
    return HttpResponse('''<script>alert('successfully reject');window.location='/myapp/viewsupplieradmin/'</script>''')

def approvesupplieradmin(request):
    obj = Supplier.objects.filter(status='approved')
    return render(request,'admin/approvesupplier.html', {'data':obj})


def approvesupplieradminpost(request):
    search=request.POST['textfield']
    obj = Supplier.objects.filter(status='approved',companyname__icontains=search)
    return render(request, 'admin/approvesupplier.html', {'data': obj})


def rejectsupplieradmin(request):
    obj = Supplier.objects.filter(status='reject')
    return render(request,'admin/rejectsupplier.html', {'data':obj})

def rejectsupplieradminpost(request):
    search=request.POST['textfield']
    obj = Supplier.objects.filter(status='reject',companyname__icontains=search)
    return render(request, 'admin/rejectsupplier.html', {'data': obj})


def viewmanufactureadmin(request):
    obj=Manufacture.objects.filter(status='pending')
    return render(request,'admin/verifymanufacture.html',{'data':obj})

def viewmanufactureadminpost(request):
    search = request.POST['textfield']
    obj = Manufacture.objects.filter(status='pending', name__icontains=search)  # pending values are stored in obj, name__icontains=search this tells that in what name we want to search the data
    return render(request, 'admin/verifymanufacture.html', {'data': obj})

def manufactureapprove(request,id):
    obj=Manufacture.objects.filter(LOGIN=id).update(status='approved')
    obj1=Login.objects.filter(id=id).update(type='manufacture')
    return HttpResponse('''<script>alert('successfully approved');window.location='/myapp/viewmanufactureadmin/'</script>''')

def manufacturereject(request,id):
    obj=Manufacture.objects.filter(LOGIN=id).update(status='reject')
    obj1=Login.objects.filter(id=id).update(type='pending')
    return HttpResponse('''<script>alert('successfully reject');window.location='/myapp/viewmanufactureadmin/'</script>''')


def approvemanufactureadmin(request):
    obj = Manufacture.objects.filter(status='approved')
    return render(request,'admin/approvemanufacture.html', {'data':obj})

def approvemanufactureadminpost(request):
    search=request.POST['textfield']
    obj = Manufacture.objects.filter(status='approved',name__icontains=search)
    return render(request, 'admin/approvemanufacture.html', {'data': obj})


def rejectmanufactureadmin(request):
    obj = Manufacture.objects.filter(status='reject')
    return render(request,'admin/rejectmanufacture.html', {'data':obj})
def viewselleradmin(request):
    obj=Seller.objects.filter(status='pending')
    return render(request,'admin/verifysellers.html',{'data':obj})

def viewselleradminpost(request):
    search = request.POST['textfield']
    obj = Seller.objects.filter(status='pending', companyname__icontains=search)
    return render(request, 'admin/verifysellers.html', {'data': obj})

def sellersapprove(request,id):
    obj=Seller.objects.filter(LOGIN=id).update(status='approved')
    obj1=Login.objects.filter(id=id).update(type='seller')
    return HttpResponse('''<script>alert('successfully approved');window.location='/myapp/viewselleradmin/'</script>''')



def sellersreject(request,id):
    obj=Seller.objects.filter(LOGIN=id).update(status='reject')
    obj1=Login.objects.filter(id=id).update(type='pending')
    return HttpResponse('''<script>alert('successfully reject');window.location='/myapp/viewselleradmin/'</script>''')



def approveselleradmin(request):
    obj = Seller.objects.filter(status='approved')
    return render(request,'admin/approvesellers.html',{'data':obj})

def approveselleradminpost(request):
    search = request.POST['textfield']
    obj = Seller.objects.filter(status='approved',companyname__icontains=search)
    return render(request, 'admin/approvesellers.html', {'data': obj})


def rejectselleradmin(request):
    obj = Seller.objects.filter(status='reject')
    return render(request,'admin/rejectsellers.html',{'data':obj})

def rejectselleradminpost(request):
    search = request.POST['textfield']
    obj = Seller.objects.filter(status='reject',companyname__icontains=search)
    return render(request, 'admin/rejectsellers.html', {'data': obj})


def viewcomplaintadmin(request):
    obj=Complaint.objects.all()
    return render(request,'admin/usercomplaint&viewreply.html', {'data':obj})

def viewcomplaintadminpost(request):
    searchfrom = request.POST['textfield']
    searchto = request.POST['textfield2']
    obj = Complaint.objects.filter(date__range=[searchfrom,searchto])
    return render(request, 'admin/usercomplaint&viewreply.html', {'data': obj})

def sendreply(request,id):
    # obj = Complaint.objects.all()
    return render(request, 'admin/sendreply.html', {'id':id})

def sendreplypost(request):
    cid = request.POST['cid']
    reply = request.POST['textfield']
    obj = Complaint.objects.get(id=cid)
    obj.reply=reply
    obj.status='replied'
    obj.save()
    return HttpResponse('''<script>alert('replied');window.location='/myapp/viewcomplaintadmin/'</script>''')

def viewfeedback(request):
    obj = Feedback.objects.all()
    return render(request, 'admin/viewfeedback.html', {'data': obj})

def viewfeedbackpost(request):
    searchfrom = request.POST['textfield']
    searchto = request.POST['textfield2']
    obj = Feedback.objects.filter(date__range=[searchfrom, searchto])
    return render(request, 'admin/viewfeedback.html', {'data': obj})


def viewuser(request):
    obj= User.objects.all()
    return render(request, 'admin/viewusers.html' ,{'data':obj})

def viewuserpost(request):
    search = request.POST['textfield']
    obj = User.objects.filter(username=search)
    return render(request, 'admin/viewusers.html', {'data': obj})

def adminhome(request):
    return render(request, 'admin/adminhome.html')


######## supplier ########

def signupsupplier(request):
    return render(request, 'supplier/signup.html')

def signupsupplierpost(request):
    companyname = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    website = request.POST['textfield4']
    location = request.POST['textfield5']
    industry = request.POST['textfield6']
    # status = request.POST['textfield8']
    logo = request.FILES['textfield7']
    certification = request.FILES['textfield8']
    password = request.POST['textfield9']
    confirm_password = request.POST['textfield10']

    from datetime import datetime
    date=datetime.now().strftime('%Y%m%d-%H%M%S')+'-1.jpg' #this for logo images do some changes in settings.ppy and djangoproject/urls.py then add these lines in views.py file
    fs=FileSystemStorage()
    fn=fs.save(date,logo)
    path=fs.url(date)


    from datetime import datetime #for the certificate images
    date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + '-2.jpg'  #year,month,date,hour,minute,second
    fs1 = FileSystemStorage()
    fn1 = fs1.save(date1, certification)
    path1 = fs1.url(date1)

    obj= Login() #when supplier wants to signup should go datas to login table and supplier table
    obj.username=email
    obj.password=confirm_password
    obj.type='pending'
    obj.save() #save to the db

    if password==confirm_password:
        objj= Supplier() #datas for the supplier table
        objj.companyname=companyname
        objj.email=email
        objj.LOGIN=obj
        objj.phone=phone
        objj.website=website
        objj.location=location
        objj.industry=industry
        objj.status='pending'
        objj.logo=path
        objj.certification=path1
        objj.save()
    return HttpResponse('''<script>alert('registered successfully');window.location='/myapp/loginadmin/'</script>''')


def loginsupplier(request):
    return render(request, 'login.html')


def viewprofilesupplier(request):
    obj=Supplier.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'supplier/viewprofile.html',{'data':obj})

def editsupplier(request):
    obj=Supplier.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'supplier/editsupplier.html',{'data':obj})

def editsupplierpost(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    website=request.POST['textfield4']
    location=request.POST['textfield5']
    industry=request.POST['textfield6']
    certification=request.POST['textfield8']


    obj=Supplier.objects.get(LOGIN_id=request.session['lid'])
    if 'textfield7' in request.FILES:
        logo = request.POST['textfield7']
        from datetime import datetime  # for the logo images
        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
        fs1 = FileSystemStorage()
        fn1 = fs1.save(date1, logo)
        path1 = fs1.url(date1)
        obj.logo = path1
        obj.save()

    obj.companyname=name
    obj.email=email
    obj.phone=phone
    obj.website=website
    obj.location=location
    obj.industry=industry
    obj.certification=certification
    obj.save()
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/viewprofilesupplier/'</script>''')



def addrawmaterialssupplier(request):
    return render(request,'supplier/addrawmaterials.html')

def managerawmaterialsaddsupplierpost(request):
    name=request.POST['name']
    category=request.POST['category']
    description=request.POST['description']
    origin=request.POST['origin']
    harvestorproductiondate=request.POST['harvest']
    cost=request.POST['cost']
    quantity=request.POST['quantity']
    certification=request.POST['certificate']

    obj=Rawmaterials() #add datas
    obj.name=name
    obj.category=category
    obj.description=description
    obj.origin=origin
    obj.harvestorproductiondate=harvestorproductiondate
    obj.cost=cost
    obj.quantity=quantity
    obj.certification=certification
    obj.SUPPLIER=Supplier.objects.get(LOGIN_id=request.session['lid']) #for foreign key
    obj.save()
    return HttpResponse('''<script>alert('added ');window.location='/myapp/managerawmaterialsaddsupplier/'</script>''')


def viewrawmaterialsedit(request):
    obj = Rawmaterials.objects.filter(SUPPLIER__LOGIN_id=request.session['lid'])
    return render(request,'supplier/viewrawmaterials.html',{'data':obj})

def viewrawmaterialspost(request):
    search=request.POST['textfield']
    obj = Rawmaterials.objects.filter(SUPPLIER__LOGIN_id=request.session['lid'],name__icontains=search)
    return render(request, 'supplier/viewrawmaterials.html', {'data': obj})

def editrawmaterials(request,id):
    obj=Rawmaterials.objects.get(id=id)
    return render(request, 'supplier/editrawmaterial.html', {'data':obj})

def editrawmaterialspost(request):
    name=request.POST['name']
    category=request.POST['category']
    description=request.POST['description']
    origin=request.POST['origin']
    harvestorproductiondate=request.POST['harvestorproductiondate']
    certification=request.POST['certification']
    cost=request.POST['cost']
    quantityavailable=request.POST['quantityavailable']

    obj = Rawmaterials()  # edit datas
    obj.name = name
    obj.category = category
    obj.description = description
    obj.origin = origin
    obj.harvestorproductiondate = harvestorproductiondate
    obj.cost = cost
    obj.quantity = quantityavailable
    obj.certification = certification
    obj.SUPPLIER = Supplier.objects.get(LOGIN_id=request.session['lid'])  # for foreign key
    obj.save()
    return HttpResponse('''<script>alert('editted ');window.location='/myapp/viewrawmaterialsedit/'</script>''')

def deleterawmaterials(request,id):
    obj = Rawmaterials.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert('deleted ');window.location='/myapp/viewrawmaterialsedit/'</script>''')


def viewstock(request):
    obj=Stockrawmaterial.objects.all()
    return render(request, 'supplier/viewstock.html',{'data':obj})

def addstocksupplier(request):
    obj=Rawmaterials.objects.all()
    return render(request, 'supplier/addstock.html', {'data':obj})

def addstocksupplierpost(request):
    quantity=request.POST['textfield']
    rawmaterial=request.POST['textfield2']

    obj = Stockrawmaterial()
    obj.quantity = quantity
    obj.RAWMATERIAL_id = rawmaterial  # for foreign key
    return HttpResponse('''<script>alert('stock added ');window.location='/myapp/addstocksupplier/'</script>''')



def editstocksupplier(request,id):
    obj = Stockrawmaterial.objects.get(id=id)
    obj = Rawmaterials.objects.all()
    return render(request, 'supplier/editstock.html', {'data': obj})


def editstocksupplierpost(request):
    quantity = request.POST['textfield']
    rawmaterial = request.POST['textfield2']

    obj = Stockrawmaterial.objects.get(id=id)
    obj.RAWMATERIAL_id = rawmaterial
    obj.quantity = quantity
    # obj.Stockrawmaterial = Stockrawmaterial.objects.get(quantity=request.session['lid'])  # for foreign key
    return HttpResponse('''<script>alert('edited successfully ');window.location='/myapp/viewstock/'</script>''')

def deletestocksupplier(request,id):
    obj=Stockrawmaterial.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert('deleted successfully ');window.location='/myapp/viewstock/'</script>''')



def viewordersfrommanufacture(request):
    obj=Rawmaterialordermain.objects.all() #to view every data
    return render(request,'supplier/viewordersfrommanufacture.html', {'data':obj})

def viewordersub(request,id):
    obj=Rawmaterialoredrsub.objects.filter(RAWMATERIALORDERMAIN=id)
    return render(request, 'supplier/ordersubsupplier.html', {'data':obj})



def updateorderstatussupplier(request,id):
    obj=Rawmaterialordermain.objects.filter(pk=id).update(status='updated')
    # return render(request, 'supplier/updateorderstatus.html')
    return HttpResponse('''<script>alert('updated successfully ');window.location='/myapp/viewordersfrommanufacture/'</script>''')


def supplierhome(request):
    return render(request, 'supplier/supplierhome.html')

### manufacture ###

def signupmanufacture(request):
    return render(request, 'manufacture/signup.html')

def signupmanufacturepost(request):
    name= request.POST['textfield']
    email= request.POST['textfield2']
    phone= request.POST['textfield3']
    website= request.POST['textfield4']
    location= request.POST['textfield5']
    registrationdate= request.POST['textfield6']
    status= request.POST['textfield7']
    logo= request.FILES['textfield8']
    certification= request.FILES['textfield9']
    password= request.POST['textfield10']
    confirmpassword= request.POST['textfield11']

    from datetime import datetime
    date = datetime.now().strftime(
        '%Y%m%d-%H%M%S') + '-1.jpg'  # this for logo images do some changes in settings.ppy and djangoproject/urls.py then add these lines in views.py file
    fs = FileSystemStorage()
    fn = fs.save(date, logo)
    path = fs.url(date)

    from datetime import datetime  # for the certificate images
    date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + '-2.jpg'  # year,month,date,hour,minute,second
    fs1 = FileSystemStorage()
    fn1 = fs1.save(date1, certification)
    path1 = fs1.url(date1)


    log=Login()
    log.username=email
    log.password=confirmpassword
    log.type='manufacture'
    log.save()


    obj=Manufacture()
    obj.name=name
    obj.email=email
    obj.phone=phone
    obj.website=website
    obj.location=location
    obj.registrationdate=registrationdate
    obj.status=status
    obj.logo=path
    obj.certification=path1
    obj.LOGIN=log
    obj.status='pending'
    obj.save()
    return HttpResponse('''<script>alert(' welcome');window.location='/myapp/loginadmin/'</script>''')





# def loginmanufacture(request):
#
#     return render(request, 'login.html')

def changepasswordmanufacture(request):

    return render(request, 'manufacture/changepassword.html')


def changepasswordmanufacturepost(request):
    Oldpassword=request.POST['textfield']
    Newpassword=request.POST['textfield2']
    Confirmpassword=request.POST['textfield3']
    log=Login.objects.filter(password=Oldpassword)  #take old password
    if log.exists(): #check oldpassword and enteringpassword are same or not
        log1=Login.objects.get(password=Oldpassword,id=request.session['lid']) # retrieving a single record from the Login model/table where both the password matches a specific value (Oldpassword) and the id matches a value stored in the session variable 'lid'.
        if Newpassword==Confirmpassword:
            log1 = Login.objects.filter(password=Oldpassword, id=request.session['lid']).update(password=Confirmpassword)


            return HttpResponse('''<script>alert('login successfull');window.location='/myapp/loginadmin/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/myapp/changepasswordadmin/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');window.location='/myapp/changepasswordadmin/'</script>''')



def viewprofilemanufacture(request):
    obj=Manufacture.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'manufacture/viewprofile.html', {'data':obj})

def manufactureeditprofile(request):
    obj=Manufacture.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'manufacture/manufactureedit.html', {'data':obj})

def manufactureeditpost(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    website=request.POST['textfield4']
    location=request.POST['textfield5']
    Registrationdate=request.POST['textfield6']
    status=request.POST['textfield7']

    obj=Manufacture.objects.get(LOGIN_id=request.session['lid'])
    if 'logo' in request.FILES:
        logo = request.POST['textfield8']

        from datetime import datetime
        date = datetime.now().strftime(
            '%Y%m%d-%H%M%S') + '.jpg'  # this for logo images do some changes in settings.ppy and djangoproject/urls.py then add these lines in views.py file
        fs = FileSystemStorage()
        fn = fs.save(date, logo)
        path = fs.url(date)
        obj.logo=path
        obj.save()
    if 'logo' in request.FILES:
        certification = request.FILES['textfield9']

        from datetime import datetime  # for the certificate images
        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
        fs1 = FileSystemStorage()
        fn1 = fs1.save(date1, certification)
        path1 = fs.url(date)
        obj.certification=path1
        obj.save()

    obj=Manufacture()
    obj.name=name
    obj.email=email
    obj.phone=phone
    obj.website=website
    obj.location=location
    obj.registrationdate=Registrationdate
    obj.status=status
    obj.save()
    return HttpResponse('''<script>alert('edited');window.location='/myapp/viewprofilemanufacture/'</script>''')


def viewsupplier(request):
    obj = Supplier.objects.all()
    return render(request, 'manufacture/viewsupplier.html',{'obj':obj})




def viewrawmaterialsandsendorder(request,id):
    obj=Stockrawmaterial.objects.filter(RAWMATERIAL=id)
    return render(request, 'manufacture/viewrawmaterial&sendorder.html',{'data':obj})


def viewmanufactureproduct(request):
    return render(request, 'manufacture/editdeletemanufacturingproduct.html')

def viewmanufactureproductpost(request):
    obj = Manufacture.objects.all()
    return render(request, 'manufacture/editdeletemanufacturingproduct.html', {'obj': obj})



def managemanufactureproductadd(request):
    return render(request, 'manufacture/addmanufacturingproduct.html')

def managemanufactureproductaddpost(request):
    name=request.POST['textfield']
    category=request.POST['textfield2']
    description=request.POST['textfield3']
    specification=request.POST['textfield4']
    unitofmeasurement=request.POST['textfield5']

    obj = Manufactureproducts()     #add products
    obj.productname=name
    obj.category=category
    obj.description=description
    obj.specification=specification
    obj.unitofmeasurement=unitofmeasurement
    obj.MANUFACTUREID =Manufacture.objects.get(LOGIN_id=request.session['lid']) # for foreign key
    obj.save()
    return HttpResponse('''<script>alert('product added ');window.location='/myapp/managemanufactureproductadd/'</script>''')



def managemanufactureproductedit(request):
    return render(request, 'manufacture/editmanufacturingproduct.html')

def managemanufactureproducteditpost(request):
    name=request.POST['textfield']
    category=request.POST['textfield2']
    description=request.POST['textfield3']
    specification=request.POST['textfield5']

    obj=Manufactureproducts() #edit Manufactureproducts
    obj.name=name
    obj.category=category
    obj.description=description
    obj.specification=specification
    obj.MANUFACTUREID = Manufacture.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/viewmanufactureproduct/'</script>''')

def manufactureproductdelete(request,id):
    obj = Manufactureproducts.objects.get(id=id).delete
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/viewmanufactureproduct/'</script>''')


def viewsellerorderandverify(request):
    return render(request, 'manufacture/viewsellersorder&verify.html')

def viewsellerorderandverifypost(request):
    obj = Manufacture.objects.all()
    return render(request, 'manufacture/viewsellersorder&verify.html', {'obj': obj})



def manufacturehome(request):
    return render(request, 'manufacture/manufacturehome.html')


###SELLER###

def signupseller(request):
    return render(request, 'seller/signup.html')

def signupsellerpost(request):
    companyname = request.POST['textfield']
    email = request.POST['textfield2']
    address = request.POST['textfield3']
    website = request.POST['textfield4']
    location = request.POST['textfield5']
    dateofbirth = request.POST['textfield6']
    status = request.POST['textfield7']
    password = request.POST['textfield8']
    confirmpassword = request.POST['textfield9']

    log = Login()
    log.username = email
    log.password = confirmpassword
    log.type = 'seller'
    log.save()

    obj = Manufacture()
    obj.name = companyname
    obj.email = email
    obj.address = address
    obj.website = website
    obj.location = location
    obj.dateofbirth = dateofbirth
    obj.status = status
    obj.LOGIN = log
    obj.save()
    return HttpResponse('''<script>alert(' welcome');window.location='/myapp/loginadmin/'</script>''')


# def loginseller(request):
#     return render(request, 'login.html')


def viewandeditprofile(request):
    obj=Seller.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'seller/view&editprofile.html',{'data':obj})


def viewcustomerorder(request):
    return render(request,'seller/viewcustomerorder.html')

def viewcustomerorderpost(request):
    obj = Seller.objects.all()
    return render(request, 'seller/viewcustomerorder.html', {'data': obj})


def viewpayments(request):
    obj = Payment.objects.all()
    return render(request,'seller/viewpayments.html',{'data':obj})

def viewpaymentspost(request):
    searchfrom = request.POST['textfield']
    searchto = request.POST['textfield']
    obj = Payment.objects.filter(paymentdate__range=[searchfrom, searchto])
    return render(request,'seller/viewpayments.html',{'data':obj})


def updateorderstatus(request):
    return render(request, 'seller/viewcustomerorder.html')

def viewmanufacture(request):
    return render(request, 'seller/viewmanufacture.html')

def viewmanufacturepost(request):
    obj = Seller.objects.all()
    return render(request,'seller/viewmanufacture.html',{'data':obj})

def viewmanufacturingproducts(request):
    return render(request, 'seller/viewmanufacturingproducts.html')

def viewmanufacturingproductspost(request):
    obj = Seller.objects.all()
    return render(request,'seller/viewmanufacturingproducts.html',{'data':obj})

def viewpurchase(request):
    return render(request, 'seller/purchase.html')

def viewpurchasepost(request):
    obj = Seller.objects.all()
    return render(request, 'seller/purchase.html', {'data': obj})

def viewproducts(request):
    return render(request,'seller/viewmanufacturingproducts.html',{'data':obj})

def addproductstosale(request):
    return render(request,'seller/addproducttosale.html')

def addproductstosalepost(request):
    productname = request.POST['textfield']
    description = request.POST['textfield2']
    category = request.POST['textfield3']

    obj = Seller()
    obj.productname=productname
    obj.description=description
    obj.category=category
    obj.save()
    return HttpResponse('''<script>alert(' Added');window.location='/myapp/loginadmin/'</script>''')

def sellerhome(request):
    return render(request,'seller/sellerhome.html')


###CUSTOMER###







