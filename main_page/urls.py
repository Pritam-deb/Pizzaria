from django.urls import path
from . import views

#app_name = 'main_page'
urlpatterns = [
    path('', views.home, name="home"),
    path('menu.html', views.menu, name="menu"),
    path('blog.html', views.blog, name="blog"),
    path('blog-single.html', views.blogsingle, name="blog-single"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('services.html', views.services, name="services"),
    path('log-in.html', views.login, name="login"),
]
