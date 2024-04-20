import datetime
import json
import smtplib

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from web3 import *

from myapp.models import *
from sam1 import settings

blockchain_address = 'HTTP://127.0.0.1:7545'
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = settings.STATIC_ROOT+'\\blocks\\build\\contracts\\supply.json'
# deployed_contract_addressa = '0x2F5fCdCdc1EA4322AEA9cf6e9B0a40560F0baD95'
deployed_contract_addressa = web3.eth.accounts[4]

# Create your views here.

###ADMIN###

def loginadmin(request):
    return render(request, 'loginindex.html')
def loginpost(request): #create post method to take data
    username=request.POST['textfield'] #create a variable name called username then create it's post method
    password=request.POST['textfield2']
    log=Login.objects.filter(username=username,password=password) #create object called log, filter is a method to filter records based on certain criteria.
    if log.exists(): #is a conditional statement that checks whether there are any records in the queryset log.
        log1=Login.objects.get(username=username,password=password)  #retrieving a single record from the Login table where the username and password match specific values.
        request.session['lid']=log1.id #assigns the value of the id field of the log1 object to a session variable named 'lid'.
        if log1.type=='admin':
            return HttpResponse('''<script>alert('welcome');window.location='/myapp/adminhome/'</script>''')#returns an HTTP response containing JavaScript code that displays an alert message and redirects the user's browser to another URL.
        if log1.type=='supplier':
            return HttpResponse('''<script>alert('welcome');window.location='/myapp/supplierhome/'</script>''')

        if log1.type=='manufacture':
            return HttpResponse('''<script>alert('welcome');window.location='/myapp/manufacturehome/'</script>''') #returns an HTTP response containing JavaScript code that displays an alert message and redirects the user's browser to another URL.
        if log1.type=='seller':
            return  HttpResponse('''<script>alert('welcome');window.location='/myapp/sellerhome/'</script>''')
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

def rejectmanufactureadminpost(request):
    search=request.POST['textfield']
    obj = Manufacture.objects.filter(status='reject',name__icontains=search)
    return render(request, 'admin/rejectmanufacture.html', {'data': obj})

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
    obj = User.objects.filter(username__icontains=search)
    return render(request, 'admin/viewusers.html', {'data': obj})

def adminhome(request):
    return render(request, 'admin/adminindex.html')


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


    obj=Supplier.objects.get(LOGIN_id=request.session['lid'])
    if 'textfield7' in request.FILES:
        logo = request.FILES['textfield7']
        from datetime import datetime  # for the logo images
        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
        fs1 = FileSystemStorage()
        fn1 = fs1.save(date1, logo)
        path1 = fs1.url(date1)
        obj.logo = path1
        obj.save()


    if 'textfield8' in request.FILES:
        certificate = request.FILES['textfield8']
        from datetime import datetime  # for the logo images
        date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
        fs2 = FileSystemStorage()
        fn2 = fs2.save(date2, certificate)
        path2 = fs2.url(date2)
        obj.certification = path2
        obj.save()

    obj.companyname=name
    obj.email=email
    obj.phone=phone
    obj.website=website
    obj.location=location
    obj.industry=industry
    obj.save()
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/viewprofilesupplier/#tab'</script>''')



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
    certification=request.FILES['certificate']


    from datetime import datetime
    date='raw_materials/'+datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fs=FileSystemStorage()
    fs.save(date,certification)
    path=fs.url(date)



    obj=Rawmaterials() #add datas
    obj.name=name
    obj.category=category
    obj.description=description
    obj.origin=origin
    obj.harvestorproductiondate=harvestorproductiondate
    obj.cost=cost
    obj.quantityavailable=quantity
    obj.certification=path
    obj.SUPPLIER=Supplier.objects.get(LOGIN_id=request.session['lid']) #for foreign key

    with open(compiled_contract_path)as file:
        contract_json = json.load(file)
        contract_abi = contract_json['abi']
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    message2 = contract.functions.addmaterials(int(blocknumber),
                                              str(name),
                                              str(category),
                                              str(description),
                                              str(request.session['lid']),
                                              str(origin),
                                              str(harvestorproductiondate),
                                              str(path),
                                              str(cost),
                                              str(quantity),
                                              str('rawmaterial')
                                              ).transact({'from': web3.eth.accounts[0]})
    return HttpResponse('''<script>alert('added ');window.location='/myapp/supplierhome/'</script>''')


def viewrawmaterialsedit(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()

    l=[]
    for i in range(blocknumber,0, -1):

       try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            c= decoded_input[1]
            # if c['typea'] == 'request':

            if int(c['suppliera']) == int(request.session['lid']):
                l.append({'ida':c['ida'],
                              'namea':c['namea'],
                              'categorya':c['categorya'],
                              'descriptiona':c['descriptiona'],
                              'suppliera':c['suppliera'],
                              'quantitya':c['quantitya'],
                              'origina':c['origina'],
                              'costa':c['costa'],
                              'productiondatea':c['productiondatea'],
                              'certificatea':c['certificatea']})
       except:
           pass
    return render(request,'supplier/viewrawmaterials.html',{'data':l})

def viewrawmaterialspost(request):
    obj = request.POST['textfield']
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l = []
    for i in range(blocknumber, 0, -1):

        try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1])
            c = decoded_input[1]
            # if c['typea'] == 'request':

            if int(c['suppliera']) == int(request.session['lid']):
                if str(obj).lower() in str(c['namea']).lower():
                    l.append({'ida': c['ida'],
                              'namea': c['namea'],
                              'categorya': c['categorya'],
                              'descriptiona': c['descriptiona'],
                              'suppliera': c['suppliera'],
                              'quantitya': c['quantitya'],
                              'origina': c['origina'],
                              'costa': c['costa'],
                              'productiondatea': c['productiondatea'],
                              'certificatea': c['certificatea']})
        except:
            pass
    return render(request, 'supplier/viewrawmaterials.html', {'data': l})

def editrawmaterials(request,id):
    obj=Rawmaterials.objects.get(id=id)
    return render(request, 'supplier/editrawmaterial.html', {'data':obj})

def editrawmaterialspost(request):
    name=request.POST['name']
    category=request.POST['category']
    description=request.POST['description']
    origin=request.POST['origin']
    harvestorproductiondate=request.POST['harvest']
    cost=request.POST['cost']
    quantityavailable=request.POST['quantity']
    id=request.POST['id']

    obj = Rawmaterials.objects.get(id=id)  # edit datas

    if 'certification' in request.FILES:
        certification = request.FILES['certification']

        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, certification)
        path = fs.url(date)

        obj.certification = path
        obj.save()

    obj.name = name
    obj.category = category
    obj.description = description
    obj.origin = origin
    obj.harvestorproductiondate = harvestorproductiondate
    obj.cost = cost
    obj.quantityavailable = quantityavailable
    obj.SUPPLIER = Supplier.objects.get(LOGIN_id=request.session['lid'])  # for foreign key
    obj.save()
    return HttpResponse('''<script>alert('editted ');window.location='/myapp/viewrawmaterialsedit/'</script>''')

def deleterawmaterials(request,id):
    obj = Rawmaterials.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert('deleted ');window.location='/myapp/viewrawmaterialsedit/'</script>''')


def delete_rawmaterials(request,id):
    obj=Rawmaterials.objects.get(id=id).delete()
    return HttpResponse('''<script>alert('deleted');window.location='/myapp/viewrawmaterialsedit/'</script>''')


def viewstock(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l = []
    for i in range(blocknumber, 0, -1):

        try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1])
            c = decoded_input[1]
            # if c['typea'] == 'request':

            if int(c['suppliera']) == int(request.session['lid']):

                s = Stockrawmaterial.objects.filter(RAWMATERIAL_id=c['ida'])

                if s.exists():
                    l.append({'ida': c['ida'],
                              'id': s[0].id,
                              'namea': c['namea'],
                              'categorya': c['categorya'],
                              'descriptiona': c['descriptiona'],
                              'suppliera': c['suppliera'],
                              'quantitya': c['quantitya'],
                              'origina': c['origina'],
                              'costa': c['costa'],
                              'productiondatea': c['productiondatea'],
                              'certificatea': c['certificatea'],
                              'stk': s[0].quantity,
                              })

                else:
                    l.append({'ida': c['ida'],
                              'id': s[0].id,
                              'namea': c['namea'],
                              'categorya': c['categorya'],
                              'descriptiona': c['descriptiona'],
                              'suppliera': c['suppliera'],
                              'quantitya': c['quantitya'],
                              'origina': c['origina'],
                              'costa': c['costa'],
                              'productiondatea': c['productiondatea'],
                              'certificatea': c['certificatea'],
                              'stk': '0',
                              })

        except:
            pass
    return render(request, "supplier/viewstock.html", {'data': l})


def viewstockpost(request):
    search=request.POST['textfield']
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l = []
    for i in range(blocknumber, 0, -1):

        try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1])
            c = decoded_input[1]
            # if c['typea'] == 'request':

            if int(c['suppliera']) == int(request.session['lid']):

                s = Stockrawmaterial.objects.filter(RAWMATERIAL_id=c['ida'])
                if str(search).lower() in str(c['namea']).lower():

                    if s.exists():
                        l.append({'ida': c['ida'],
                                  'id': s[0].id,
                                  'namea': c['namea'],
                                  'categorya': c['categorya'],
                                  'descriptiona': c['descriptiona'],
                                  'suppliera': c['suppliera'],
                                  'quantitya': c['quantitya'],
                                  'origina': c['origina'],
                                  'costa': c['costa'],
                                  'productiondatea': c['productiondatea'],
                                  'certificatea': c['certificatea'],
                                  'stk': s[0].quantity,
                                  })
                        print(l)

                    else:
                        l.append({'ida': c['ida'],
                                  'id': s[0].id,
                                  'namea': c['namea'],
                                  'categorya': c['categorya'],
                                  'descriptiona': c['descriptiona'],
                                  'suppliera': c['suppliera'],
                                  'quantitya': c['quantitya'],
                                  'origina': c['origina'],
                                  'costa': c['costa'],
                                  'productiondatea': c['productiondatea'],
                                  'certificatea': c['certificatea'],
                                  'stk': '0',
                                  })

        except:
            pass
    return render(request, "supplier/viewstock.html", {'data': l})



def addstocksupplier(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    l=[]
    for i in range(blocknumber,0, -1):

       try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            c= decoded_input[1]
            if int(c['suppliera']) == int(request.session['lid']):
                l.append({'id':c['ida'],
                      'name':c['namea'],
                      })
       except:
           pass
    return render(request, 'supplier/addstock.html', {'data':l})

def addstocksupplierpost(request):
    quantity=request.POST['textfield']
    rawmaterial=request.POST['textfield2']
    obj = Stockrawmaterial()
    if Stockrawmaterial.objects.filter(RAWMATERIAL_id=rawmaterial).exists():
        obj = Stockrawmaterial.objects.filter(RAWMATERIAL_id=rawmaterial)[0]
    obj.quantity = quantity
    obj.RAWMATERIAL_id = rawmaterial  # for foreign key
    obj.SUPPLIER = Supplier.objects.get(LOGIN_id=request.session['lid'])  # for foreign key
    obj.save()
    return HttpResponse('''<script>alert('stock added ');window.location='/myapp/viewstock/'</script>''')



def editstocksupplier(request,id):
    obj1 = Stockrawmaterial.objects.get(id=id)
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    l=[]
    for i in range(blocknumber,0, -1):

       try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            c= decoded_input[1]
            if int(c['suppliera']) == int(request.session['lid']):
                l.append({'id':c['ida'],
                      'name':c['namea'],
                      })
       except:
           pass
    return render(request, 'supplier/editstock.html', {'data': l,'data1':obj1})


def editstocksupplierpost(request):
    quantity = request.POST['textfield']
    rawmaterial = request.POST['textfield2']
    id = request.POST['id']

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

def viewordersfrommanufacturepost(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    obj =Rawmaterialordermain.objects.filter(date__range=[fromdate, todate])
    return render(request, 'supplier/viewordersfrommanufacture.html', {'data': obj})


def viewordersubsupplier(request,id):
    obj=Rawmaterialoredrsub.objects.filter(RAWMATERIALORDERMAIN=id)
    request.session['osmids'] = id
    return render(request, 'supplier/ordersubsupplier.html', {'data':obj, 'search':''})

def viewordersubpost(request):
    search = request.POST['textfield']
    id = request.session['osmids']
    obj = Rawmaterialoredrsub.objects.filter(RAWMATERIALORDERMAIN_id=id)
    return render(request, 'supplier/ordersubsupplier.html', {'data': obj, 'search':search})

def updateorderstatussupplier(request,id):
    obj=Rawmaterialordermain.objects.filter(pk=id).update(status='updated')
    # return render(request, 'supplier/updateorderstatus.html')
    return HttpResponse('''<script>alert('updated successfully ');window.location='/myapp/viewordersfrommanufacture/'</script>''')


def supplierhome(request):
    return render(request, 'supplier/supplierindex.html')

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
    log=Login.objects.filter(password=Oldpassword,id=request.session['lid'])  #take old password
    if log.exists(): #check oldpassword and enteringpassword are same or not
        log1=Login.objects.get(password=Oldpassword,id=request.session['lid']) # retrieving a single record from the Login model/table where both the password matches a specific value (Oldpassword) and the id matches a value stored in the session variable 'lid'.
        if Newpassword==Confirmpassword:
            log1 = Login.objects.filter(password=Oldpassword, id=request.session['lid']).update(password=Confirmpassword)


            return HttpResponse('''<script>alert('login successfull');window.location='/myapp/loginadmin/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');history.back()</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');history.back()</script>''')


def viewprofilemanufacture(request):
    obj=Manufacture.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'manufacture/viewprofile.html', {'data':obj})

def manufactureeditprofile(request):
    obj=Manufacture.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'manufacture/manufactureedit.html', {'data':obj})

def manufactureeditprofilepost(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    website=request.POST['textfield4']
    location=request.POST['textfield5']


    obj=Manufacture.objects.get(LOGIN_id=request.session['lid'])
    if 'textfield8' in request.FILES:
        logo = request.FILES['textfield8']
        from datetime import datetime  # for the logo images
        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
        fs1 = FileSystemStorage()
        fn1 = fs1.save(date1, logo)
        path1 = fs1.url(date1)
        obj.logo = path1
        obj.save()

    if 'textfield9' in request.FILES:
        certification = request.FILES['textfield9']
        from datetime import datetime  # for the logo images
        date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
        fs2 = FileSystemStorage()
        fn2 = fs2.save(date2, certification)
        path2 = fs2.url(date2)
        obj.certification = path2
        obj.save()

    obj.name=name
    obj.email=email
    obj.phone=phone
    obj.website=website
    obj.location=location
    obj.save()
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/manufactureeditprofile/'</script>''')



def viewsupplier(request):
    obj = Supplier.objects.all()
    return render(request, 'manufacture/viewsupplier.html',{'obj':obj})

def viewsupplierpost(request):
    search = request.POST['textfield']
    obj = Supplier.objects.filter(companyname__icontains=search)
    return render(request, 'manufacture/viewsupplier.html', {'obj': obj})



def viewrawmaterialsandsendorder(request,slid):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Login required');window.location='/myapp/login/'</script>''')
    obj = Stockrawmaterial.objects.filter(SUPPLIER__LOGIN_id=slid)
    return render(request, 'manufacture/viewrawmaterial&sendorder.html',{'data':obj, 'slid': slid, 'search': ''})

def viewrawmaterialsandsendorderpost(request):
    search = request.POST['textfield']
    slid = request.POST['slid']
    obj = Stockrawmaterial.objects.filter(SUPPLIER__LOGIN_id=slid)
    return render(request, 'manufacture/viewrawmaterial&sendorder.html', {'data': obj, 'slid': slid, 'search': search})

def quantity(request,id, cost):
    request.session['mcost'] = cost
    return render(request,'manufacture/addquantity.html',{'id':id})

def orderrawmaterial(request):
    rid=request.POST['id']
    quantity=request.POST['textfield']
    obj=Rawmaterialordermain()
    import datetime
    obj.date=datetime.datetime.now().date()
    obj.amount=float(request.session['mcost'])*float(quantity)
    obj.status='ordered'
    obj.MANUFACTURE=Manufacture.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    r=Rawmaterialoredrsub()
    r.RAWMATERIALORDERMAIN=obj
    r.RAWMATERIAL_id=rid
    r.quantity=quantity
    r.save()

    return HttpResponse('''<script>alert('order placed ');window.location='/myapp/viewsupplier/#tab'</script>''')


def viewrawmaterialsorder(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Login required');window.location='/myapp/login/'</script>''')
    res = Rawmaterialoredrsub.objects.filter(RAWMATERIALORDERMAIN__MANUFACTURE__LOGIN_id=request.session['lid'])
    l = []
    ex = []
    for i in res:
        if i.RAWMATERIALORDERMAIN.id in ex:
            continue
        ex.append(i.RAWMATERIALORDERMAIN.id)
        l.append({
            'id':i.RAWMATERIALORDERMAIN.id,
            'name': i.RAWMATERIAL_id,
            'date': i.RAWMATERIALORDERMAIN.date,
            'amount': i.RAWMATERIALORDERMAIN.amount,
            'status': i.RAWMATERIALORDERMAIN.status,
        })
    return render(request,'Manufacture/vieworders to supplier.html', {'data':l})

def viewrawmaterialsorderpost(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Login required');window.location='/myapp/login/'</script>''')
    fro_=request.POST['textfield']
    to_=request.POST['textfield2']
    res = Rawmaterialoredrsub.objects.filter(
        RAWMATERIALORDERMAIN__MANUFACTURE__LOGIN_id=request.session['lid'],
        RAWMATERIALORDERMAIN__date__range=[fro_, to_],)
    l = []
    ex = []
    for i in res:
        if i.RAWMATERIALORDERMAIN.id in ex:
            continue
        ex.append(i.RAWMATERIALORDERMAIN.id)
        l.append({
            'id':i.RAWMATERIALORDERMAIN.id,
            'name': i.RAWMATERIAL_id,
            'date': i.RAWMATERIALORDERMAIN.date,
            'amount': i.RAWMATERIALORDERMAIN.amount,
            'status': i.RAWMATERIALORDERMAIN.status,
        })
    return render(request,'Manufacture/vieworders to supplier.html', {'data':l})


def manufacturer_viewordersub(request,id):
    request.session['osmid'] = id
    obj=Rawmaterialoredrsub.objects.filter(RAWMATERIALORDERMAIN=id)
    return render(request, 'manufacture/ordersubsupplier.html', {'data': obj, 'search':''})

def manufacturer_viewordersubpost(request):
    search = request.POST['textfield']
    id = request.session['osmid']
    obj = Rawmaterialoredrsub.objects.filter(RAWMATERIALORDERMAIN_id=id)
    return render(request, 'manufacture/ordersubsupplier.html', {'data': obj, 'search':search})


def addmanufacturingproduct(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Login required');window.location='/myapp/login/'</script>''')

    return render(request,'Manufacture/Addmanufacturingproduct.html')

def addmanufacturingproductpost(request):
    name=request.POST['textfield']
    category=request.POST['textfield2']
    description=request.POST['textfield3']
    specification=request.FILES['textfield4']
    unitofmeasurement=request.POST['textfield5']

    from datetime import datetime
    date1 = 'products/'+datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs1 = FileSystemStorage()
    fs1.save(date1, specification)
    path1 = fs1.url(date1)
    from datetime import datetime
    with open(compiled_contract_path)as file:
        contract_json = json.load(file)
        contract_abi = contract_json['abi']
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    message2 = contract.functions.addmproduct(int(blocknumber), str(name), str(category), str(description), str(path1),
                                               str(unitofmeasurement),str(request.session['lid']), str('mproduct')).transact(
        {'from': web3.eth.accounts[0]})



    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/addmanufacturingproduct/#tab'</script>''')

def viewmanufactureproduct(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Login required');window.location='/myapp/login/'</script>''')
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,0, -1):

       try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1])
            c= decoded_input[1]
            # if c['typea'] == 'request':

            if int(c['manufacture_ida']) == int(request.session['lid']):


                l.append({'ida':c['ida'],
                          'namea':c['namea'],
                          'categorya':c['categorya'],
                          'descriptiona':c['descriptiona'],
                          'specificationa':c['specificationa'],
                          'unitofmeasurementa':c['unitofmeasurementa'],
                          'manufacture_ida':c['manufacture_ida'],
                          'typea':c['typea']
                    })
       except:
           pass
    return render(request, 'Manufacture/viewmanufacturingproduct.html',{'data':l})

def viewmanufactureproductpost(request):
    name = request.POST['textfield']
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Login required');window.location='/myapp/login/'</script>''')
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,0, -1):

       try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1])
            c= decoded_input[1]
            # if c['typea'] == 'request':

            if int(c['manufacture_ida']) == int(request.session['lid']):
                if str(name).lower() in str(c['namea']):
                    l.append({
                            'ida':c['ida'],
                            'namea':c['namea'],
                            'categorya':c['categorya'],
                            'descriptiona':c['descriptiona'],
                            'specificationa':c['specificationa'],
                            'unitofmeasurementa':c['unitofmeasurementa'],
                            'manufacture_ida':c['manufacture_ida'],
                            'typea':c['typea']
                            })
       except:
           pass
    return render(request, 'Manufacture/viewmanufacturingproduct.html',{'data':l})



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
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/viewmanufactureproduct/#tab'</script>''')

def manufactureproductdelete(request,id):
    obj = Manufactureproducts.objects.get(id=id).delete
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/viewmanufactureproduct/'</script>''')


def viewsellerorderandverify(request):
    res = Sellerordermain.objects.filter()
    return render(request, 'manufacture/viewsellersorder&verify.html', {'data':res})

def approvesellerorder(request, id):
    res = Sellerordermain.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert('Approved ');window.location='/myapp/viewsellerorderandverify/'</script>''')

def rejectsellerorder(request, id):
    res = Sellerordermain.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert('Rejected ');window.location='/myapp/viewsellerorderandverify/'</script>''')

def viewsellerorderandverifypost(request):
    fro_ = request.POST['textfield']
    to_ = request.POST['textfield2']
    res = Sellerordermain.objects.filter(date__range=[fro_, to_])
    return render(request, 'manufacture/viewsellersorder&verify.html', {'data':res})

def viewseller_suborder(request, id):
    res = Sellerordersub.objects.filter(SELLERORDERMAIN_id=id)
    return render(request, 'manufacture/view seller sub orders.html', {'data':res})


def manufacturehome(request):
    return render(request, 'manufacture/manufactureindex.html')


###SELLER###

def signupseller(request):
    return render(request, 'seller/signup.html')

def signupsellerpost(request):
    companyname = request.POST['textfield']
    email = request.POST['textfield2']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    # address = request.POST['textfield3']
    website = request.POST['textfield4']
    location = request.POST['textfield5']
    dateofbirth = request.POST['textfield6']
    # status = request.POST['textfield7']
    password = request.POST['textfield8']
    confirmpassword = request.POST['textfield9']
    certificate = request.FILES['certificate']
    phone = request.POST['phone']

    log = Login()
    log.username = email
    log.password = confirmpassword
    log.type = 'pending'
    log.save()

    from datetime import datetime  # for the logo images
    date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
    fs2 = FileSystemStorage()
    fn2 = fs2.save(date2, certificate)
    path2 = fs2.url(date2)

    obj = Seller()
    obj.companyname = companyname
    obj.email = email
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.website = website
    obj.location = location
    obj.dateofbirth = dateofbirth
    obj.status = "pending"
    obj.LOGIN = log
    obj.phone=phone
    import datetime
    obj.registrationdate=datetime.datetime.now().date()
    obj.certificate = path2
    obj.save()
    return HttpResponse('''<script>alert(' welcome');window.location='/myapp/loginadmin/'</script>''')


# def loginseller(request):
#     return render(request, 'login.html')


def viewandeditprofile(request):
    obj=Seller.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'seller/view&editprofile.html',{'data':obj})

def editseller(request):
    obj = Seller.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'seller/editprofile.html', {'data': obj})
def editsellerpost(request):
    companyname=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    website=request.POST['textfield4']
    location=request.POST['textfield5']



    obj = Seller.objects.get(LOGIN_id=request.session['lid'])

    if 'textfield6' in request.FILES:
        certificate = request.FILES['textfield6']
        from datetime import datetime  # for the logo images
        date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'  # year,month,date,hour,minute,second
        fs2 = FileSystemStorage()
        fn2 = fs2.save(date2, certificate)
        path2 = fs2.url(date2)
        obj.certificate = path2
        obj.save()

    obj.companyname = companyname
    obj.email = email
    obj.phone = phone
    obj.website = website
    obj.location = location
    obj.save()
    return HttpResponse('''<script>alert('edited ');window.location='/myapp/viewandeditprofile/#tab'</script>''')

def viewcustomerorder(request):
    obj = Customerordermain.objects.all()
    return render(request,'seller/viewcustomerorder.html',{'data':obj})

def viewcustomerorderpost(request):

    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    obj = Customerordermain.objects.filter(date__range=[fromdate,todate])

    return render(request, 'seller/viewcustomerorder.html', {'data': obj})


def viewordersub(request,id):
    obj = Customerordersub.objects.filter(CUSTOMERORDERMAIN_id=id)

    return render(request, 'seller/viewcustomerordersub.html', {'data': obj})


def viewpayments(request):
    obj = Payment.objects.all()
    return render(request,'seller/viewpayments.html',{'data':obj})

def viewpaymentspost(request):
    searchfrom = request.POST['textfield']
    searchto = request.POST['textfield']
    obj = Payment.objects.filter(paymentdate__range=[searchfrom, searchto])
    return render(request,'seller/viewpayments.html',{'data':obj})


def updateorderstatus(request,id):
    obj = Customerordermain.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert(' Approved');window.location='/myapp/viewcustomerorder/'</script>''')

def updateorderreject(request,id):
    obj = Customerordermain.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert(' Rejected');window.location='/myapp/viewcustomerorder/'</script>''')

def viewapprovedcustomerorder(request):
    obj = Customerordermain.objects.filter(status='approved')
    return render(request, 'seller/viewapprovedcustomerorder.html', {'data':obj})
def viewapprovedcustomerorderpost(request):
    searchfrom = request.POST['textfield']
    searchto = request.POST['textfield']
    obj = Customerordermain.objects.filter(status='approved',date__range=[searchfrom, searchto])
    return render(request, 'seller/viewapprovedcustomerorder.html', {'data': obj})

def viewrejectedcustomerorder(request):
    obj = Customerordermain.objects.filter(status='rejected')
    return render(request, 'seller/viewrejectedcustomerorder.html',  {'data':obj})

def viewrejectedcustomerorderpost(request):
    searchfrom = request.POST['textfield']
    searchto = request.POST['textfield']
    obj = Customerordermain.objects.filter(status='rejected',date__range=[searchfrom, searchto])
    return render(request, 'seller/viewrejectedcustomerorder.html', {'data': obj})

def viewmanufacture(request):
    obj = Manufacture.objects.filter(status='approved')
    return render(request, 'seller/viewmanufacture.html', {'data':obj})

def viewmanufacturepost(request):
   search = request.POST['textfield']
   obj = Manufacture.objects.filter(name__icontains=search, status='approved')
   return render(request,'seller/viewmanufacture.html', {'data':obj})

def viewmanufacturingproducts(request, id):
    request.session['manLid'] = id

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,0, -1):

       try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1])
            c= decoded_input[1]

            if int(c['manufacture_ida']) == int(id):


                l.append({'ida':c['ida'],
                          'namea':c['namea'],
                          'categorya':c['categorya'],
                          'descriptiona':c['descriptiona'],
                          'specificationa':c['specificationa'],
                          'unitofmeasurementa':c['unitofmeasurementa'],
                          'manufacture_ida':c['manufacture_ida'],
                          'typea':c['typea']
                    })
       except:
           pass
    return render(request, 'seller/viewmanufacturingproducts.html',{'data':l})

def viewmanufacturingproductspost(request):
    search = request.POST['textfield']
    id = request.session['manLid']
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,0, -1):

       try:

            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1])
            c= decoded_input[1]

            if int(c['manufacture_ida']) == int(id):
                if str(search).lower() in str(c['namea']).lower():
                    l.append({'ida':c['ida'],
                          'namea':c['namea'],
                          'categorya':c['categorya'],
                          'descriptiona':c['descriptiona'],
                          'specificationa':c['specificationa'],
                          'unitofmeasurementa':c['unitofmeasurementa'],
                          'manufacture_ida':c['manufacture_ida'],
                          'typea':c['typea']
                    })
       except:
           pass
    return render(request, 'seller/viewmanufacturingproducts.html',{'data':l})

def seller_product_quantity(request, id):
    return render(request, 'seller/addquantity.html', {'pid': id})

def seller_product_quantity_post(request):
    pid = request.POST['id']
    q = request.POST['textfield']
    date = datetime.date.today()

    sor = Sellerordermain()
    sor.date = date
    sor.SELLER = Seller.objects.get(LOGIN_id=request.session['lid'])
    sor.status = 'ordered'
    sor.save()

    sos = Sellerordersub()
    sos.MANUFACTUREPRODUCT_id = pid
    sos.quantity = q
    sos.SELLERORDERMAIN = sor
    sos.save()

    return HttpResponse('''<script>alert(' Ordered');window.location='/myapp/viewmanufacture/'</script>''')


def viewpurchase(request):
    obj = Sellerordersub.objects.filter(SELLERORDERMAIN__SELLER__LOGIN_id=request.session['lid'])
    spr = Sellerproducts.objects.filter(SELLERORDERSUB__SELLERORDERMAIN__SELLER__LOGIN_id=request.session['lid'])
    l = []
    for i in spr:
        l.append(i.SELLERORDERSUB_id)
    return render(request, 'seller/purchase.html', {'data':obj, 'spr':l})

def viewpurchasesub(request,id):
    obj = Purchasesub.objects.filter(PURCHASEMAIN=id)
    return render(request, 'seller/purchasesub.html', {'data': obj})

def viewpurchasepost(request):
    obj = Seller.objects.all()
    return render(request, 'seller/purchase.html', {'data': obj})

def viewproducts(request):
    return render(request,'seller/viewmanufacturingproducts.html')

def addproductstosale(request, id):
    request.session['selPid'] = id
    return render(request,'seller/addproducttosale.html')

def addproductstosalepost(request):
    id = request.session['selPid']
    saleamount = request.POST['textfield']
    spr = Sellerproducts()
    spr.quantity = Sellerordersub.objects.get(id=id).quantity
    spr.SELLERORDERSUB = Sellerordersub.objects.get(id=id)
    spr.saleamount = saleamount
    spr.status = 'available'
    spr.save()
    return HttpResponse('''<script>alert(' Product added for sale');window.location='/myapp/viewpurchase/#tab'</script>''')

def sellerhome(request):
    return render(request,'seller/sellerindex.html')


###CUSTOMER###







def customer_signup(request):#for signup for customers
    name=request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    gender = request.POST['gender']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']
    photo=request.POST['photo']
    from  datetime import datetime
    date=datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'# Generate a filename based on the current date and time
    import base64
    a=base64.b64decode(photo)# Decode base64 encoded image
    # fh=open("C:\\Users\\HP\\PycharmProjects\\supplychain\\media\\user\\"+date,'wb')# Specify the path to save the image
    fh=open("D:\\sam1\\media\\user\\"+date,'wb')# Specify the path to save the image
    path='/media/user/'+date# Specify the path relative to your media directory
    fh.write(a)
    fh.close()

    lobj=Login()
    lobj.username=email
    lobj.password=password
    lobj.type='user'
    lobj.save()

    if password==confirmpassword:
        obj=User()
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.place=place
        obj.post=post
        obj.pin=pin
        obj.district=district
        obj.gender=gender
        obj.photo=path
        obj.LOGIN=lobj
        obj.save()
        return JsonResponse({'status':'ok'})

def customer_login(request):
    username=request.POST['username']
    password=request.POST['password']
    log=Login.objects.filter(username=username,password=password)
    if log.exists():
        log1=Login.objects.get(username=username,password=password)
        lid=log1.id
        if log1.type == 'user':
            return JsonResponse({'status':'ok','lid':str(lid),'type':log1.type})
        else:
            return  JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status':'no'})
def customer_viewprofile(request):
    lid=request.POST['lid']
    obj=User.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','photo':obj.photo,'name':obj.username,'email':obj.email,'phone':obj.phone,'place':obj.place,'post':obj.post,'pin':obj.pin,'district':obj.district,'gender':obj.gender})
    # return JsonResponse({'status':'ok','photo':'/static/login/images/user.png','name':obj.username,'email':obj.email,'phone':obj.phone,'place':obj.place,'post':obj.post,'pin':obj.pin,'district':obj.district,'gender':obj.gender})

def customer_editprofile(request):
    name=request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    gender = request.POST['gender']
    lid=request.POST['lid']
    photo=request.POST['photo']
    if len(photo)>5:
        from  datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        import base64
        a = base64.b64decode(photo)
        fh = open("D:\\sam1\\media\\user\\" + date, 'wb')
        # fh = open("D:\\sam1\\media\\media\\user\\" + date, 'wb')
        path = '/media/user/' + date
        fh.write(a)
        fh.close()
        obj = User.objects.get(LOGIN_id=lid)
        obj.photo=path
        obj.save()

    obj=User.objects.get(LOGIN_id=lid)
    obj.name=name
    obj.email=email
    obj.phone=phone
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.district=district
    obj.gender=gender
    obj.save()
    oo=Login.objects.get(id=lid)
    oo.username=email
    oo.save()


    return JsonResponse({'status':'ok'})


def forgot_password(request):
    email = request.POST['email']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("safedore3@gmail.com", "yqqlwlyqbfjtewam")

    obj = Login.objects.filter(username=email)
    if obj.exists():
        to = email
        subject = "Test Email"
        body = "Your password is " + obj[0].password
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)

        server.quit()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'no'})

def customer_viewproduct(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    print(blocknumber,'bbbbbbbbbbbbbbb')
    l=[]
    for i in range(blocknumber,0, -1):

       try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1],'decoded_input')
            c= decoded_input[1]
            man=Manufacture.objects.filter(LOGIN_id=c['manufacture_ida'])

            # if Sellerproducts.objects.filter(PURCHASESUB__PURCHASEMAIN__SELLER__status='approve',PURCHASESUB__product=str(c['ida'])).exists():
            if Sellerproducts.objects.filter(SELLERORDERSUB__SELLERORDERMAIN__status='approved',SELLERORDERSUB__MANUFACTUREPRODUCT_id=str(c['ida'])).exists():
                if man.exists():
                    selP = Sellerproducts.objects.filter(SELLERORDERSUB__SELLERORDERMAIN__status='approved',SELLERORDERSUB__MANUFACTUREPRODUCT_id=str(c['ida']))[0]
                    man=man[0]
                    print("hloooooooooooooooooooooo")
                    l.append({'ida':str(c['ida']),
                                  'id':str(selP.id),
                                  'name':c['namea'],
                                  'category':c['categorya'],
                                  'description':c['descriptiona'],
                                  'Image':c['specificationa'],
                                  'unitofmeasurement':str(c['unitofmeasurementa']),
                                  'manufacture_ida':str(c['manufacture_ida']),
                                  'typea':c['typea'],

                              'namme':man.name,'phone':man.phone,'email':man.email


                        })

       except:
           pass
    return JsonResponse({'status':'ok','data':l})

def customer_placeorder(request):
    return JsonResponse({'status':'ok'})

def customer_makepayment(request):
    return JsonResponse({'status':'ok'})

def customer_vieworderstatus(request):
    lid=request.POST['lid']
    obj=Customerordersub.objects.filter(CUSTOMERORDERMAIN__USER__LOGIN_id=lid)
    l=[]
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    l = []
    for j in range(blocknumber, 0, -1):

        try:
            a = web3.eth.get_transaction_by_block(j, 0)
            decoded_input = contract.decode_function_input(a['input'])
            c = decoded_input[1]
            for i in obj:
                if int(i.MANUFACTUREPRODUCT_id) == int(c['ida']):
                    l.append({'id': i.id, 'quantity': i.quantity,
                              'PRODUCT': i.MANUFACTUREPRODUCT_id,
                              'date': i.CUSTOMERORDERMAIN.date, 'amount': i.CUSTOMERORDERMAIN.amount,
                              'status': i.CUSTOMERORDERMAIN.status})
        except Exception as e:
            pass
    return JsonResponse({'status':'ok','data':l})


def customer_sendfeedback(request):
    lid=request.POST['lid']
    rating=request.POST['rating']

    obj=Feedback()
    # obj.type='admin'
    obj.rating=rating
    obj.USER=User.objects.get(LOGIN_id=lid)
    from datetime import datetime
    obj.date=datetime.now().today()
    obj.save()


    return JsonResponse({'status':'ok'})

def customer_sendcomplaint(request):
    lid=request.POST['lid']
    complaint=request.POST['complaint']

    obj=Complaint()
    from datetime import datetime
    obj.date=datetime.now().today()
    obj.complaint=complaint
    obj.staus='pending'
    obj.reply='pending'
    obj.USER=User.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status':'ok'})

def customer_viewreply(request):
    lid=request.POST['lid']
    obj=Complaint.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in obj:
        l.append({'id':i.id,'date':i.date,'complaint':i.complaint,'status':i.status,'reply':i.reply})
    return JsonResponse({'status':'ok','data':l})

def customer_addtocart(request):
    lid = request.POST["lid"]
    pid = request.POST["pid"]
    Quantity = request.POST["Quantity"]
    a = Cart()
    if Cart.objects.filter(PRODUCTS_id = pid, USER = User.objects.get(LOGIN_id=lid)).exists():
        a = Cart.objects.filter(PRODUCTS_id = pid, USER = User.objects.get(LOGIN_id=lid))[0]
    a.quantity = Quantity
    a.PRODUCTS_id = pid
    # a.PRODUCT = Sellerproducts.objects.get(id=pid)
    a.USER = User.objects.get(LOGIN_id=lid)
    from datetime import datetime
    a.date=datetime.now().date().today()

    a.save()
    return JsonResponse({'status': 'ok'})

def user_viewcart(request):
    lid=request.POST['lid']
    total=0
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    l = []
    for i in range(blocknumber, 0, -1):

        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            # print(decoded_input[1], 'decoded_input')
            c = decoded_input[1]
            res = Cart.objects.filter(USER__LOGIN_id=lid,PRODUCTS__SELLERORDERSUB__MANUFACTUREPRODUCT_id=c['ida'])
            if res.exists():
                if Sellerproducts.objects.filter(SELLERORDERSUB__SELLERORDERMAIN__status='approved',
                                                 SELLERORDERSUB__MANUFACTUREPRODUCT_id=str(c['ida'])).exists():
                    selCart = Cart.objects.filter(
                        PRODUCTS__SELLERORDERSUB__MANUFACTUREPRODUCT_id=str(c['ida']))[0]
                    selP = Sellerproducts.objects.filter(SELLERORDERSUB__SELLERORDERMAIN__status='approved',
                                                         SELLERORDERSUB__MANUFACTUREPRODUCT_id=str(c['ida']))[0]
                    total+=(float(selP.saleamount)*int(selCart.quantity))
                    # man = man[0]
                    l.append({
                              'ida': c['ida'],
                              'id': selCart.id,
                              'Productname': c['namea'],
                              'Colour': c['categorya'],
                              'Offerprice': c['descriptiona'],
                              'Image': c['specificationa'],
                              'Primarymaterial': c['unitofmeasurementa'],
                              'MRP':selP.saleamount,
                              'manufacture_ida': c['manufacture_ida'],
                              'typea': c['typea'],

                              # 'namme': man.name, 'phone': man.phone, 'email': man.email

                              })

        except Exception as e:
            pass
    return JsonResponse({'status': "ok", "data": l,"amount":int(total)})

def removefromcart(request):
    cid=request.POST['cid']
    print(cid)
    va=Cart.objects.filter(id=cid).delete()
    return JsonResponse({'status':'ok'})







def user_makepayment(request):
    lid=request.POST['lid']


    mytotal=0
    res2 = Cart.objects.filter(USER__LOGIN_id=lid)
    boj = Customerordermain()
    boj.USER = User.objects.get(LOGIN_id=lid)
    boj.amount = 0
    boj.status='paid'
    import datetime
    boj.date = datetime.datetime.now().date().today()
    boj.save()

    try:
        for j in res2:
            bs = Customerordersub()
            bs.CUSTOMERORDERMAIN_id = boj.id
            bs.MANUFACTUREPRODUCT_id = j.PRODUCTS.SELLERORDERSUB.MANUFACTUREPRODUCT_id
            # bs.MANUFACTUREPRODUCT_id = j.PRODUCTS.id
            bs.quantity = j.quantity
            bs.save()
            mytotal += (float(j.PRODUCTS.saleamount) * int(j.quantity))
    except Exception as e:
        print(e)
        pass
    print(mytotal)
    Cart.objects.filter(USER__LOGIN_id=lid).delete()
    boj=Customerordermain.objects.get(id=boj.id)
    boj.amount=mytotal
    boj.save()
    return JsonResponse({'k':'0','status':"ok"})


