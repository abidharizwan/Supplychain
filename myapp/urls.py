"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("loginadmin/", views.loginadmin),
    path("loginpost/", views.loginpost),
    path("changepasswordadmin/", views.changepasswordadmin),
    path("changepasswordadminpost/", views.changepasswordadminpost),
    path("viewsupplieradmin/", views.viewsupplieradmin),
    path("viewsupplieradminpost/", views.viewsupplieradminpost),
    path("supplierapprove/<id>", views.supplierapprove),
    path("supplierreject/<id>", views.supplierreject),
    path("approvesupplieradmin/", views.approvesupplieradmin),
    path("approvesupplieradminpost/", views.approvesupplieradminpost),
    path("rejectsupplieradmin/", views.rejectsupplieradmin),
    path("rejectsupplieradminpost/", views.rejectsupplieradminpost),
    path("viewmanufactureadmin/", views.viewmanufactureadmin),
    path("viewmanufactureadminpost/", views.viewmanufactureadminpost),
    path("manufactureapprove/<id>", views.manufactureapprove),
    path("manufacturereject/<id>", views.manufacturereject),
    path("approvemanufactureadmin/", views.approvemanufactureadmin),
    path("approvemanufactureadminpost/", views.approvemanufactureadminpost),
    path("rejectmanufactureadmin/", views.rejectmanufactureadmin),
    path("rejectmanufactureadminpost/", views.rejectmanufactureadminpost),
    path("viewselleradmin/", views.viewselleradmin),
    path("viewselleradminpost/", views.viewselleradminpost),
    path("sellersapprove/<id>", views.sellersapprove),
    path("sellersreject/<id>", views.sellersreject),
    path("approveselleradmin/", views.approveselleradmin),
    path("approveselleradminpost/", views.approveselleradminpost),
    path("rejectselleradmin/", views.rejectselleradmin),
    path("rejectselleradminpost/", views.rejectselleradminpost),
    path("viewcomplaintadmin/", views.viewcomplaintadmin),
    path("viewcomplaintadminpost/", views.viewcomplaintadminpost),
    path("sendreply/<id>", views.sendreply),
    path("sendreplypost/", views.sendreplypost),
    path("viewfeedback/", views.viewfeedback),
    path("viewfeedbackpost/" , views.viewfeedbackpost),
    path("viewuser/", views.viewuser),
    path("viewuserpost/" ,views.viewuserpost),
    path("adminhome/", views.adminhome),



    path("signupsupplier/", views.signupsupplier),
    path("signupsupplierpost/" , views.signupsupplierpost),
    path("loginsupplier/", views.loginsupplier),

    path("viewprofilesupplier/", views.viewprofilesupplier),
    path("editsupplier/", views.editsupplier),
    path("editsupplierpost/", views.editsupplierpost),
    path("addrawmaterialssupplier/", views.addrawmaterialssupplier),
    path("managerawmaterialsaddsupplierpost/", views.managerawmaterialsaddsupplierpost),
    path("viewrawmaterialsedit/", views.viewrawmaterialsedit),
    path("viewrawmaterialspost/", views.viewrawmaterialspost),
    path("editrawmaterials/<id>", views.editrawmaterials),
    path("editrawmaterialspost/", views.editrawmaterialspost),
    path("deleterawmaterials/<id>", views.deleterawmaterials),
    path("delete_rawmaterials/<id>", views.delete_rawmaterials),
    path("viewstock/", views.viewstock),
    path("viewstockpost/", views.viewstockpost),
    path("addstocksupplier/", views.addstocksupplier),
    path("addstocksupplierpost/", views.addstocksupplierpost),
    path("editstocksupplier/<id>", views.editstocksupplier),
    path("editstocksupplierpost/", views.editstocksupplierpost),
    path("deletestocksupplier/<id>", views.deletestocksupplier),
    path("viewordersfrommanufacture/", views.viewordersfrommanufacture),
    path("viewordersfrommanufacturepost/", views.viewordersfrommanufacturepost),
    path("viewordersubsupplier/<id>", views.viewordersubsupplier),
    path("viewordersubpost/", views.viewordersubpost),
    path("updateorderstatussupplier/<id>", views.updateorderstatussupplier),
    path("supplierhome/", views.supplierhome),

    path("signupmanufacture/", views.signupmanufacture),
    path("signupmanufacturepost/", views.signupmanufacturepost),
    # path("loginmanufacture/", views.loginmanufacture),
    path("changepasswordmanufacture/", views.changepasswordmanufacture),
    path("changepasswordmanufacturepost/" , views.changepasswordmanufacturepost),
    path("viewprofilemanufacture/", views.viewprofilemanufacture),
    path("manufactureeditprofile/", views.manufactureeditprofile),
    path("manufactureeditprofilepost/", views.manufactureeditprofilepost),
    path("viewsupplier/", views.viewsupplier),
    path("viewsupplierpost/", views.viewsupplierpost),
    path("viewrawmaterialsandsendorder/<slid>", views.viewrawmaterialsandsendorder),
    path("viewrawmaterialsandsendorderpost/", views.viewrawmaterialsandsendorderpost),
    path("orderrawmaterial/", views.orderrawmaterial),
    path("quantity/<id>/<cost>", views.quantity),

    path("viewrawmaterialsorder/", views.viewrawmaterialsorder),
    path("viewrawmaterialsorderpost/", views.viewrawmaterialsorderpost),
    path("manufacturer_viewordersub/<id>", views.manufacturer_viewordersub),
    path("manufacturer_viewordersubpost/", views.manufacturer_viewordersubpost),

    path("viewmanufactureproduct/", views.viewmanufactureproduct),
    path("viewmanufactureproductpost/", views.viewmanufactureproductpost),

    path("addmanufacturingproduct/", views.addmanufacturingproduct),
    path("addmanufacturingproductpost/", views.addmanufacturingproductpost),
    path("managemanufactureproductadd/", views.addmanufacturingproduct),
    path("managemanufactureproductaddpost/",views.addmanufacturingproductpost),
    path("managemanufactureproductedit/", views.managemanufactureproductedit),
    path("manufactureproductdelete/<id>", views.manufactureproductdelete),
    path("managemanufactureproducteditpost/", views.managemanufactureproducteditpost),
    path("viewsellerorderandverify/", views.viewsellerorderandverify),
    path("approvesellerorder/<id>", views.approvesellerorder),
    path("rejectsellerorder/<id>", views.rejectsellerorder),
    path("viewsellerorderandverifypost/", views.viewsellerorderandverifypost),
    path("viewseller_suborder/<id>", views.viewseller_suborder),
    path("manufacturehome/", views.manufacturehome),

    path("signupseller/", views.signupseller),
    path("signupsellerpost/", views.signupsellerpost),
    # path("loginseller/", views.loginseller),
    path("viewandeditprofile/", views.viewandeditprofile),
    path("editseller/", views.editseller),
    path("editsellerpost/", views.editsellerpost),
    path("viewcustomerorder/", views.viewcustomerorder),
    path("viewcustomerorderpost/", views.viewcustomerorderpost),

    path("updateorderstatus/<id>", views.updateorderstatus),
    path("updateorderreject/<id>", views.updateorderreject),

    path("viewordersub/<id>", views.viewordersub),
    path("viewpayments/", views.viewpayments),
    path("viewpaymentspost/", views.viewpaymentspost),
    path("viewapprovedcustomerorder/", views.viewapprovedcustomerorder),
    path("viewapprovedcustomerorderpost/", views.viewapprovedcustomerorderpost),
    path("viewrejectedcustomerorder/", views.viewrejectedcustomerorder),
    path("viewrejectedcustomerorderpost/", views.viewrejectedcustomerorderpost),
    path("viewmanufacture/", views.viewmanufacture),
    path("viewmanufacturepost/", views.viewmanufacturepost),
    path("viewmanufacturingproducts/<id>", views.viewmanufacturingproducts),
    path("viewmanufacturingproductspost/", views.viewmanufacturingproductspost),
    path("seller_product_quantity/<id>", views.seller_product_quantity),
    path("seller_product_quantity_post/", views.seller_product_quantity_post),

    path("viewpurchase/", views.viewpurchase),
    path("viewpurchasesub/<id>",views.viewpurchasesub),
    path("viewpurchasepost/", views.viewpurchasepost),
    path("addproductstosale/<id>", views.addproductstosale),
    path("addproductstosalepost/", views.addproductstosalepost),
    path("sellerhome/", views.sellerhome),
# customer

    path("customer_signup/", views.customer_signup),
    path("customer_login/", views.customer_login),
    path("user_viewcart/", views.user_viewcart),
    path("customer_sendcomplaint/", views.customer_sendcomplaint),
    path("customer_viewprofile/", views.customer_viewprofile),
    path("customer_editprofile/", views.customer_editprofile),
    path("forgot_password/", views.forgot_password),
    path("customer_viewproduct/", views.customer_viewproduct),
    path("customer_placeorder/", views.customer_placeorder),
    path("customer_makepayment/", views.customer_makepayment),
    path("customer_vieworderstatus/", views.customer_vieworderstatus),
    path("customer_sendfeedback/", views.customer_sendfeedback),
    path("customer_viewreply/", views.customer_viewreply),
    path("customer_addtocart/", views.customer_addtocart),
    path("customer_makepayment/", views.customer_makepayment),
    path("removefromcart/", views.removefromcart),
    path("user_makepayment/", views.user_makepayment),


]
