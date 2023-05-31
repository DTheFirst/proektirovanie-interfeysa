from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('rent', views.rent, name='rent'),
    path('shipment', views.shipment, name='shipment'),
    path('payment', views.payment, name='payment'),
    path('reviews', views.reviews, name='reviews'),
    path('faq', views.FAQ, name='FAQ')
]