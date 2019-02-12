from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.home, name='home'),
   # path('<int:question_id>/', views.detail, name='detail'),
]
