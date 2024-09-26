"""
URL configuration for config project.

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
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    #customer
    path('login/customer',main_views.customer_login_view,name='customer_login'),
    path('register/customer',main_views.customer_register_view,name='customer_register'),
    path('forgot/customer',main_views.customer_forgot_pass_view,name='customer_forgot_pass'),
    #seller
    path('login/seller',main_views.seller_login_view,name='seller_login'),
    path('register/seller',main_views.seller_register_view,name='seller_register'),
    path('forgot/seller',main_views.seller_forgot_pass_view,name='seller_forgot_pass'),
    path('detail/<int:id>', main_views.detail_view, name='detail'),
    #logout
     path('logout', main_views.logout_view, name='logout'),
     path('cat/<slug:name>', main_views.category_view, name='category'),
    #indexx
    path('',main_views.home_view,name='home'),
    # path('cat/<slug:name>',main_views.Category_view,name='Category'),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)