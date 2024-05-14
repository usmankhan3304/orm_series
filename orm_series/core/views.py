from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class RestaurantTemplate(LoginRequiredMixin,TemplateView):
    template_name='core/restaurant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Restaurant.objects.get(pk=1)
        context['post']="hello"
        context['name']="Ali Khan Afridi"
        return context

def home(request):
    try:
        query=Restaurant.objects.all()
        rating=Rating.objects.all()
        sale=Sale.objects.all() 
       
    except Restaurant.DoesNotExist:
        # If no restaurants are found
        raise Http404("No restaurants found")
    except Rating.DoesNotExist:
        # If no ratings are found
        raise Http404("No ratings found")
    except Sale.DoesNotExist:
        # If no sales are found
        raise Http404("No sales found")
       
    return render(request,'core/index.html',context={'data':query,'rating':rating,'sale':sale})
def login(request):
    return render(request, 'user/login.html')