from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<tag>/', views.index, name='category_tag')
]
