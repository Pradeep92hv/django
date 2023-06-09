from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect
from .models import ToDoList
from .models import Item
from .forms import CreateNewList
# import database(models)



# # Create your views here.
# def index(request):
#    return HttpResponse("this is a homepage 1")
#    # return render(request,'index.html')

def about(request):
 return HttpResponse("this is a hompage")

# def db(request,idd):
#  ls=ToDoList.objects.get(id=idd)
#  return HttpResponse("%s" %ls.name)

# def db1(request,name):
#  ls=ToDoList.objects.get(name=name)


def db1(request,name):
 ls=ToDoList.objects.get(name=name)
 return HttpResponse("%s" %ls.name)

def home(request):
#   return render(request,"home/home.html",{})
  return render(request, 'home/home.html',{})



#  templates

def index(response):   
   #   return render(response,"home/home.html",{'name":"text"})
   #  3rd par "name"  must match to key in html,  text is passed as value  name is replaced by text  in html file
    return render(response,"home/home.html",{})

def db(response,idd):
  ls=ToDoList.objects.get(id=idd)

  if response.method == "POST":
     if response.POST.get("save"):
        for item in ls.item_set.all():
          if response.POST.get("c"+ str(item.id)) == "clicked":
             item.complete = True
          else:
             item.complete = False
             
          item.save()

     elif response.POST.get("newItem"):
        txt=response.POST.get("new")

        if len(txt)>2:
           ls.item_set.create(text=txt, complete=False)
        else:
           print("invalid")        
  return render(response,"home/list.html",{"ls":ls })


def create(response):
#   form=CreateNewList()
 if response.method=="POST":
      form=CreateNewList(response.POST)

      if form.is_valid():
         n=form.cleaned_data["name"] 
         t=ToDoList(name=n)
         t.save() 

         return HttpResponsePermanentRedirect("/%i" %t.id)
 else:
       form=CreateNewList()
 return render(response,"home/createform.html",{"formm":form})