from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', views.login_request, name='login'),
    # path('signup/', views.register_request, name='register'),
    # path('logout/', views.user_logout, name='logout'),
]