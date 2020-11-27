from django.shortcuts import render

from .forms import UserForm ,RawUserForm

from .models import User

# Create your views here.
# def user_create_view(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = UserForm()
#     context={
#         'form' : form
#     }
#     return render(request,"users/create_user.html",context)

# def user_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     context={
        
#     }
#     return render(request,"users/create_user.html",context)
def user_create_view(request):
    form = RawUserForm()
    if request.method == "POST":
        form = RawUserForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            User.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    
    context={
        "form": form
    }
    return render(request,"users/create_user.html",context)

def user_detail_view(request):
    obj = User.objects.get(id=4)
    # context = {
    #     'name': obj.name,
    #     'number': obj.number
    # }
    context={
        'object' : obj
    }
    return render(request,"users/detail.html",context)