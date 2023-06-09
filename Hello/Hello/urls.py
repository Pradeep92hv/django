"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from register import views as v
# to differntiate the register project "views.py"  from  home  project "views.py"
urlpatterns = [
    path('admin/', admin.site.urls),   
    # if path is /admin then open admin page  
    path('',include('home.urls')),
    #  if path is null(''),  then move to home(app) open urls(file)
     path("register/",v.register, name="register")
]
 