from django.urls import path
from . import views
urlpatterns = [
    path('your-name/', views.get_name, name='get_name'),
    path('thanks-you/', views.thanks_view, name='thanks'),
    # Other URL patterns...
]