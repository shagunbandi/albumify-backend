from os import listdir
from os.path import isfile, join
from PIL import Image
from PIL.ExifTags import TAGS
import imghdr


def get_image_url_rec(path, join_with):
    photos_in_directory = []
    for f in listdir(path):
        if isfile(join(path, f)):
            url = join(join_with, f)
            photos_in_directory.append(url)
        else:
            photos_in_directory += get_image_url_rec(join(path, f), join(join_with, f))
    return photos_in_directory


def get_all_images_with_path_helper(path, join_with, file_dict, folder_dict):
    for f in listdir(path):
        if(isfile(join(path, f))):
            if imghdr.what(join(path, f)) is None:
                continue;
            if join_with not in file_dict:
                file_dict[join_with] = []
            file_dict[join_with].append(join(join_with, f))
        else:
            if join_with not in folder_dict:
                folder_dict[join_with] = []
            folder_dict[join_with].append(join(join_with, f))
            get_all_images_with_path_helper(join(path, f), join(join_with, f), file_dict, folder_dict)



def get_all_images_with_path(path, join_with):
    file_dict = {}
    folder_dict = {}
    get_all_images_with_path_helper(path, join_with, file_dict, folder_dict)
    return {
        'file': file_dict,
        'folder': folder_dict,
        'root': join_with
    }


def get_metadata(path):
    image = Image.open(path)
    exifdata = image.getexif()

    metadata = {}

    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode('utf-8')
        metadata[tag] = data
    return metadata
