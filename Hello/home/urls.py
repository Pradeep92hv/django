from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
     path("",views.index,name='home'),
    #  if path is matched to 1st arg  then move to views file ,perform index function  and give path name so home

      path("about",views.home,name='about'),
       path("<int:idd>",views.db,name="db"),  
       #  path refer to integer path, pass idd as parameter to db function 
               path("home",views.home,name='about'),
#              path("<str:name>",views.db1,name="db"),
      #  path refer to string path, pass idd as parameter to db function 
      

# -----------------------------------

   path("create",views.create,name='create'),
       
]
 