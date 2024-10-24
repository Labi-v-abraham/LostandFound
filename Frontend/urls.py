from django.urls import path
from Frontend import views


urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('productpage/', views.productpage, name="productpage"),
    path('product_filter_page/<cat_name>/', views.product_filter_page, name="product_filter_page"),
    path('single_pro/<int:proid>/', views.single_pro, name="single_pro"),
    path('about_page/', views.about_page, name="about_page"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('service_page/', views.service_page, name="service_page"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('register_page/', views.register_page, name="register_page"),
    path('save_register/', views.save_register, name="save_register"),
    path('delete_cart_pro/<int:dataid>/', views.delete_cart_pro, name="delete_cart_pro"),
    path('checkout/', views.checkout, name="checkout"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('save_cart/', views.save_cart, name="save_cart"),
]