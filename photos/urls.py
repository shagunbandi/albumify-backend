from django.urls import path

from . import views

urlpatterns = [
    # path('', views.all_images, name='index'),
    path('api/', views.all_images_urls, name='index_api'),
    path('api/folder', views.get_all_images_with_path, name='index_api_folder'),
]

