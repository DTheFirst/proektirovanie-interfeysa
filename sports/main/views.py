import http

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Hello', 'Some', 'Fun'],
        'obj': {
            'car': 'BMW',
            'age': '18',
            'hobby': 'Basketball'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})

def rent(request):
    return render(request, 'main/rent.html', {'title': 'Прокат'})

def shipment(request):
    return render(request, 'main/shipment.html', {'title': 'Доставка'})

def payment(request):
    return render(request, 'main/payment.html', {'title': 'Оплата'})

def reviews(request):
    return render(request, 'main/reviews.html', {'title': 'Отзывы'})

def FAQ(request):
    return render(request, 'main/FAQ.html', {'title': 'FAQ'})
