"""pizzaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

#from accounts import views as av
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    #path('accounts/',include('django.contrib.auth.urls')),
    #path('accounts/',av.register_request),
    #path('accounts/',include('accounts.urls')),
    #path('menu', views.menu, name='menu'),
    #path('blog', views.blog, name='blog'),
    #path('about', views.about, name='about'),
    #path('services', views.services, name='services'),
    #path('contact', views.contact, name='contact'),
    #path('login', views.login, name='login'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
