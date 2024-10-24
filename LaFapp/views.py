from django.shortcuts import render,redirect
from LaFapp.models import category_db,product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Frontend.models import contact_db
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def category(request):
    return render(request,"AddCategory.html")


def save_category(request):
    if request.method=="POST":
        cn = request.POST.get('category')
        cd = request.POST.get('desription')
        ci = request.FILES['img']
        obj = category_db(Category_Name=cn,Category_Description=cd,Category_Image=ci)
        obj.save()
        messages.success(request, "Data Added Successfully")
        return redirect(category)

def dis_category(request):
    category = category_db.objects.all()
    return render(request,"dis_category.html",{'category':category})

def edit_category(request,dataid):
    category = category_db.objects.get(id=dataid)
    return render(request,"edit_category.html",{'category':category})

def update_category(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('category')
        cd = request.POST.get('desription')
        try:
            ci = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(ci.name,ci)
        except MultiValueDictKeyError:
            file = category_db.objects.get(id=dataid).Category_Image
        category_db.objects.filter(id=dataid).update(Category_Name=cn,Category_Description=cd,Category_Image=file)
        messages.success(request, "Saved Changed ")

        return redirect(dis_category)

def delete_category(request,dataid):
    category = category_db.objects.filter(id=dataid)
    category.delete()
    messages.success(request, "Data removed")

    return redirect(dis_category)

def admin_login(request):
    return render(request,"adminlogin.html")

def adminlogin(request):
    if request.method=="POST":
        un = request.POST.get('user_name')
        psw = request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=psw)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=psw
                messages.success(request, "Login Successfully")

                return redirect(index)
            else:
                messages.error(request, "Login Failed")

                return redirect(admin_login)
        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)


def product(request):
    category = category_db.objects.all()
    return render(request,"AddProduct.html", {'category': category})

def save_product(request):
    if request.method=="POST":
        cn = request.POST.get('category')
        pn = request.POST.get('product')
        pp = request.POST.get('price')
        pd = request.POST.get('description')
        pi = request.FILES['img']
        obj = product_db(Category=cn,Product_Name=pn,Price=pp,Description=pd,Product_Image=pi)
        obj.save()
        messages.success(request, "Product added Successfully")

        return redirect(product)

def dis_product(request):
    product = product_db.objects.all()
    return render(request,"dis_product.html",{'product':product})

def edit_product(request,dataid):
    category = category_db.objects.all()
    product = product_db.objects.get(id=dataid)
    return render(request,"edit_product.html",{'category':category,'product':product})


def update_product(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('category')
        pn = request.POST.get('product')
        pp = request.POST.get('price')
        pd = request.POST.get('description')
        try:
            pi = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(pi.name,pi)
        except MultiValueDictKeyError:
            file = product_db.objects.get(id=dataid).Product_Image
        product_db.objects.filter(id=dataid).update(Category=cn,Product_Name=pn,Price=pp,Description=pd,Product_Image=file)
        messages.success(request, "Save Change ")

        return redirect(dis_product)

def delete_product(request,dataid):
    product = product_db.objects.filter(id=dataid)
    product.delete()
    messages.success(request, "Product Removed")

    return redirect(dis_product)

def dis_contact(req):
    contact = contact_db.objects.all()
    return render(req,"dis_contact_frontend.html",{'contact':contact})
