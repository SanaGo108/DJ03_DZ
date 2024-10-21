from django.contrib import admin
from django.urls import path, include
from Jyotish import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('articles/', include('articles.urls')),  # Статьи
    path('users/', include('users.urls')),  # Регистрация и профиль
]

# Настройка аутентификации
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
