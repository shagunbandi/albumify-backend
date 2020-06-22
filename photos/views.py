from django.http import JsonResponse
from os import listdir
from os.path import isfile, join
from django.conf import settings
from PIL import Image
from PIL.ExifTags import TAGS
from django.shortcuts import render
import math


from . import helper


path = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL
IMAGES_PER_PAGE = 500000000


def get_all_images_with_path(request):
    return JsonResponse({
        'response': "Success",
        'data': helper.get_all_images_with_path(path, 'home')
    })



def all_images_urls(request):
    page = 1
    if request.method == 'GET':
        page = int(request.GET['page'])

    data = helper.get_image_url_rec(path, 'home')
    total_files = len(data)
    total_pages = math.ceil(total_files / IMAGES_PER_PAGE)


    index_start = IMAGES_PER_PAGE * (page - 1)
    index_end = IMAGES_PER_PAGE * page

    data = data[index_start:index_end]
    return JsonResponse({
        'response': "Success",
        'data': data,
        'total_pages': total_pages,
        'total_files':  total_files,
        'total_till_now': (page - 1) * IMAGES_PER_PAGE + len(data),
        'page_number': page
    })
