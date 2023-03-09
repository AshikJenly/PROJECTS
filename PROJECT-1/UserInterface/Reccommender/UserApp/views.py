from django.shortcuts import render

# Create your views here.
def home_page_view(requests):
    return render(requests,'front/home.html',{})