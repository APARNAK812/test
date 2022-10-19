from django.urls import path
from.import views
app_name='cust'

urlpatterns=[
    path('home',views.home,name='hey'),
  
]