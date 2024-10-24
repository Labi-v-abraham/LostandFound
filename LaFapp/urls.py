from django.urls import path
from LaFapp import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('category/', views.category, name="category"),
    path('save_category/', views.save_category, name="save_category"),
    path('dis_category/', views.dis_category, name="dis_category"),
    path('edit_category/<int:dataid>/', views.edit_category, name="edit_category"),
    path('update_category/<int:dataid>/', views.update_category, name="update_category"),
    path('delete_category/<int:dataid>/', views.delete_category, name="delete_category"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('product/', views.product, name="product"),
    path('save_product/', views.save_product, name="save_product"),
    path('dis_product/', views.dis_product, name="dis_product"),
    path('edit_product/<int:dataid>/', views.edit_product, name="edit_product"),
    path('update_product/<int:dataid>/', views.update_product, name="update_product"),
    path('delete_product/<int:dataid>/', views.delete_product, name="delete_product"),
    path('dis_contact/', views.dis_contact, name="dis_contact"),

]