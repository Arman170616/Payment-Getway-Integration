from django.urls import path
from django.conf.urls import url
from payment import views


app_name = 'payment'

urlpatterns = [
    path('checkout/', views.payment, name='checkout'),
    path('', views.index, name='payment'),
    path('status/', views.complete, name='complete'),
]