from django.db import models

# Create your models here.
#login

class Login(models.Model):
    username =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    type =models.CharField(max_length=100)

#supplier

class Supplier(models.Model):
    companyname =models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    website = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    logo = models.CharField(max_length=250)
    certification = models.CharField(max_length=250)

#manufacture

class Manufacture(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    website = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    registrationdate = models.DateField()
    status = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)
    certification = models.CharField(max_length=250)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    district = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)

class Complaint(models.Model):
    date = models.DateField()
    complaint = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    USER = models.ForeignKey(User,on_delete=models.CASCADE)

class Feedback(models.Model):
    date = models.DateField()
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
    feedbacktype = models.CharField(max_length=100)

class  Seller(models.Model):
    companyname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    website = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    dateofbirth = models.DateField()
    status = models.CharField(max_length=100)
    certificate = models.CharField(max_length=250)

class Rawmaterials(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    SUPPLIER = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    harvestorproductiondate = models.DateField()
    certification = models.CharField(max_length=250)
    cost = models.CharField(max_length=100)
    quantityavailable=models.CharField(max_length=100)

class Stockrawmaterial(models.Model):
    quantity = models.IntegerField()
    RAWMATERIAL = models.ForeignKey(Rawmaterials,on_delete=models.CASCADE)

class Rawmaterialordermain(models.Model):
    date = models.DateField()
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    MANUFACTURE=models.ForeignKey(Manufacture,on_delete=models.CASCADE)

class Rawmaterialoredrsub(models.Model):
    RAWMATERIALORDERMAIN=models.ForeignKey(Rawmaterialordermain,on_delete=models.CASCADE)
    RAWMATERIAL=models.ForeignKey(Rawmaterials,on_delete=models.CASCADE,default="")
    productdescription=models.CharField(max_length=250)
    quantity=models.CharField(max_length=100)


class Sellerorder(models.Model):
    orderdate=models.DateField()
    address=models.CharField(max_length=250)
    status=models.CharField(max_length=100)
    totalquantity=models.CharField(max_length=100)
    totalordervalue=models.CharField(max_length=100)
    paymentmethod=models.CharField(max_length=100)
    paymentstatus=models.CharField(max_length=100)

class Customerordermain(models.Model):
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Sellerordermain(models.Model):
    SELLER = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Payment(models.Model):
    ORDER=models.ForeignKey(Customerordermain,on_delete=models.CASCADE)
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    paymentdate=models.DateField()
    paymentamount=models.CharField(max_length=100)
    paymentstatus=models.CharField(max_length=100)

class Manufactureproducts(models.Model):
    MANUFACTUREID=models.ForeignKey(Manufacture,on_delete=models.CASCADE)
    productname=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    specification=models.CharField(max_length=250)
    unitofmeasurement=models.CharField(max_length=250)

class Customerordersub(models.Model):
    CUSTOMERORDERMAIN = models.ForeignKey(Customerordermain, on_delete=models.CASCADE)
    MANUFACTUREPRODUCT = models.ForeignKey(Manufactureproducts, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

class Sellerordersub(models.Model):
    SELLERORDERMAIN = models.ForeignKey(Customerordermain, on_delete=models.CASCADE)
    MANUFACTUREPRODUCT = models.ForeignKey(Manufactureproducts, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

class Products(models.Model):
    productname=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    unitofmeasurement=models.CharField(max_length=100)

class Purchasemain(models.Model):
    manufacture=models.CharField(max_length=250)
    PRODUCT=models.ForeignKey(Products,on_delete=models.CASCADE)
    SELLER=models.ForeignKey(Seller,on_delete=models.CASCADE)

class Purchasesub(models.Model):
    PURCHASEMAIN=models.ForeignKey(Purchasemain,on_delete=models.CASCADE)
    product=models.CharField(max_length=250)
    quantity=models.CharField(max_length=100)

# class Sales(models.Model):
#     SELLER=models.ForeignKey(User,on_delete=models.CASCADE)
#     seller=models.CharField(max_length=250)
#
#     customer=models.CharField(max_length=250)
#     orderid=models.CharField(max_length=100)
#     saledate=models.DateField()
#     deliverydate=models.DateField()
#     saleamount=models.IntegerField()
#     paymentstatus=models.CharField(max_length=100)
#     status=models.CharField(max_length=100)
#
class Sellerproducts(models.Model):
     sellerid=models.CharField(max_length=250)
     productname=models.CharField(max_length=250)
     category=models.CharField(max_length=250)
     description=models.CharField(max_length=250)
     modelnumber=models.IntegerField()
     measurement=models.CharField(max_length=250)

class Customer(models.Model):
    customername=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()



class Productordermain(models.Model):
    PRODUCTS=models.ForeignKey(Products,on_delete=models.CASCADE)
    orderdate=models.DateField()
    orderstatus=models.CharField(max_length=100)
    price=models.CharField(max_length=100)

class Productsub(models.Model):
    PRODUCTSUBORDERMAIN=models.ForeignKey(Productordermain,on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)

# class Feedback(models.Model):
#     rating=models.CharField(max_length=100)
#     status=models.CharField(max_length=100)
#     date=models.DateField()
#     USER=models.ForeignKey(User,on_delete=models.CASCADE)



# class Complaint(models.Model):
#     complaint=models.CharField(max_length=250)
#     status=models.CharField(max_length=100)
#     date=models.DateField()
#     USER=models.ForeignKey(User,on_delete=models.CASCADE)
#     reply=models.CharField(max_length=100)











