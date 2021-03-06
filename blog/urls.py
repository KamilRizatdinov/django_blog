from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('read/', views.read, name='read'),
    path('publish/', views.publish, name='publish'),
    path('contributors/', views.contributors, name='contributors'),
]
