from django.shortcuts import render
import Students.maksim_kotulskiy.main as func
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

x1 = int(input("Перше число: "))
x2 = int(input("Друге число: "))
print(func.multiplication(x1, x2))