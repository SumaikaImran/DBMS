from django.contrib import admin
from django.urls import path, include
from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
     path("order", views.order, name='order.html'),
    path("contact", views.contact, name='contact.html'),
    # path("login", views.login, name='login.html'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
     path("designer-detail", views.designer_detail, name='designer-detail.html'), # type: ignore
    path("design-list", views.design_list, name='design-list.html'),
    path("my-account", views.myaccount, name='my-account.html'),
    path('index',views.index,name='index')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
