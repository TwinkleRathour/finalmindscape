
from django.contrib import admin
from django.urls import path
from flask_to_django.mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('ml/', views.ml, name='ml'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('ai/', views.ai, name='ai'),
    path('project/', views.project, name='project'),
]
