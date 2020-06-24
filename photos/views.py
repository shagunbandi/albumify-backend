from django.http import JsonResponse
from django.conf import settings
import pickle
import json
from django.views.decorators.csrf import csrf_exempt
from . import helper


path = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL
IMAGES_PER_PAGE = 500000000


def get_all_images_with_path(request):
    return JsonResponse({
        'response': "Success",
        'data': helper.get_all_images_with_path(path, 'home')
    })


@csrf_exempt
def get_all_album_with_path(request):
    try:
        with open('album.albumify') as json_file:
            data = json.load(json_file)
    except:
        data = {
            "response": "Success",
            "data": {
                "file": {},
                "folder": {},
                "root": "home"
            }
        }

    if request.method == 'GET':
        return JsonResponse(data)

    payload = json.loads(request.body)
    album_name = payload['album_name']
    album_path = payload['album_path']
    folder_path = album_path + '/' + album_name

    if album_path in data['data']['folder']:
        if folder_path in data['data']['folder'][album_path]:
            return JsonResponse({
                "response": "Fail",
                "msg": "Album Name Already Exists"
            })
        data['data']['folder'][album_path].append(folder_path)
    else:
        data['data']['folder'][album_path] = [folder_path]

    with open("album.albumify", "w") as write_file:
        json.dump(data, write_file)

    data['current_directory'] = album_path
    return JsonResponse(data)



def all_images_urls(request):
    data = helper.get_image_url_rec(path, 'home')
    total_files = len(data)

    return JsonResponse({
        'response': "Success",
        'data': data,
        'total_files':  total_files,
    })
