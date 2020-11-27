from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {

    })


def about_view(request, *args, **kwargs):
    my_context = {
        "cellphone": 3163016688,
        "email": "cdelgado376@unab.edu.co",
        "enterprises": ["Crisfon6", "IAM", 365],
        "helloWorld":"<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Cotact World</h1>")
