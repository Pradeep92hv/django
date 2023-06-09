from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')  # Replace 'home' with the name of your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, "register/register.html", {"form": form})