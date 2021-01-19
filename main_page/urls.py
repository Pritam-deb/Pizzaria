from django.urls import path
from . import views

#app_name = 'main_page'
urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('blog/', views.blog, name="blog"),
    path('blog-single/', views.blogsingle, name="blog-single"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register")
]
