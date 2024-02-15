from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<tag>/', views.index, name='category_tag'),
    path('home/', views.home, name='homes'),

]
