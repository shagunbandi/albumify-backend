from django.urls import path

from . import views

urlpatterns = [
    # path('', views.all_images, name='index'),
    path('api/', views.all_images_urls, name='index_api'),
    path('api/folder', views.get_all_images_with_path, name='index_api_folder'),
    path('api/album', views.get_all_album_with_path, name='index_api_album'),
    path('api/album/images', views.add_images_to_albums, name='add_api_images'),
    path('api/album/images/delete', views.delete_images_from_albums, name='add_api_images'),
]

