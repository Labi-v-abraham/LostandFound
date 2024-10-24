from django.shortcuts import render,redirect
from LaFapp.models import category_db,product_db
from Frontend.models import contact_db,register_db,cart_db
from django.contrib import messages
# Create your views here.
def homepage(request):
    cat = category_db.objects.all()
    return render(request,"Home.html",{'cat':cat})

def productpage(request):
    cat = category_db.objects.all()
    pro = product_db.objects.all()
    return render(request,"products.html",{'pro':pro,'cat':cat})

def product_filter_page(req,cat_name):
    cat = category_db.objects.all()
    data = product_db.objects.filter(Category=cat_name)
    return render(req,"product_filter.html",{'data':data,'cat':cat})

def single_pro(req,proid):
    cat = category_db.objects.all()
    data = product_db.objects.get(id=proid)
    return render(req,"single_product.html",{'data':data,'cat':cat})

def about_page(req):
    cat = category_db.objects.all()
    return render(req,"about.html",{'cat':cat})

def contact_page(req):
    cat = category_db.objects.all()
    return render(req,"contacts.html",{'cat':cat})

def service_page(req):
    cat = category_db.objects.all()
    return render(req,"service.html",{'cat':cat})

def save_contact(req):
    if req.method=="POST":
        na = req.POST.get('Name')
        em = req.POST.get('Email')
        msg = req.POST.get('Message')
        obj = contact_db(Name=na,Email_id=em,Message=msg)
        obj.save()
        return redirect(contact_page)

def register_page(req):
    return render(req,"register.html")

def save_register(req):
    if req.method=="POST":
        un = req.POST.get('uname')
        em = req.POST.get('email')
        mob = req.POST.get('mobile')
        pd = req.POST.get('psd')
        obj = register_db(Username=un,Email_id=em,Mobile=mob,Password=pd)
        obj.save()
        messages.success(req, "Register Successfully")

        return redirect(register_page)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        psd = request.POST.get('password')
        if register_db.objects.filter(Username=un,Password=psd).exists():
            request.session['Username'] =un
            request.session['Password'] =psd
            messages.success(request, "Login Successfully")

            return redirect(homepage)
        else:
            messages.error(request, "Login Failed")

            return redirect(register_page)
    return redirect(register_page)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(register_page)

def cart_page(request):
    cat = category_db.objects.all()
    data = cart_db.objects.filter(Username=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.Total_price
    return render(request,"cart.html",{'data':data,'cat':cat,'total_price':total_price})

def save_cart(request):
    if request.method=="POST":
        un = request.POST.get('uname')

        pr = request.POST.get('price')
        pn = request.POST.get('pname')
        des = request.POST.get('des')
        si = request.POST.get('size')
        cl = request.POST.get('color')
        qn = request.POST.get('quantity')
        tp = request.POST.get('tprice')
        obj = cart_db(Username=un,Price=pr,Product=pn,Description=des,Size=si,Color=cl,Quantity=qn,Total_price=tp)
        obj.save()
        messages.success(request, "Saved to Cart")

        return redirect(homepage)

def delete_cart_pro(req,dataid):
    data = cart_db.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Item removed from cart")
    return redirect(cart_page)


def checkout(request):
    cat = category_db.objects.all()
    data = cart_db.objects.filter(Username=request.session['Username'])
    return render(request,"checkout.html",{'data':data,'cat':cat})