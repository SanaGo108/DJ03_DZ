from django.shortcuts import render

def home(request):
    return render(request, 'Jyotish/home.html')  # Убедитесь, что путь к шаблону правильный
