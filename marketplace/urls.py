from django.urls import path
from . import views

app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('computers/', views.all_computers, name='all_computers'),
    path('monitors/', views.all_monitors, name='all_monitors'),
    path('computers/<int:computer_id>', views.single_computer, name='single_computer'),
    path('monitors/<int:monitor_id>', views.single_monitor, name='single_monitor')
]
