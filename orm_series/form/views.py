from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import MyForm
from django.urls import reverse

def get_name(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("thanks"))
    else:
        form = MyForm()
    return render(request, "form/name.html", {"form": form})

def thanks_view(request):
    return render(request, "form/thanks.html")