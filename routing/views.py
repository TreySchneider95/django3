from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def display_name(request):
    return render(request, 'info.html', {'key':'Name', 'value':'Trey Schneider'})

def display_food(request):
    return render(request, 'info.html', {'key':'Food', 'value':'Pizza', 'food_img': 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2021/06/1200/675/iStock-1222455274.jpg?ve=1&tl=1'})

def display_vacation(request):
    return render(request, 'info.html', {'key':'Vacation', 'value':'LaPaz Mexico', 'food_img': 'https://upload.wikimedia.org/wikipedia/commons/0/06/La_Paz_coastline.jpg'})