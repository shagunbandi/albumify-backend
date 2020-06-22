
# get_all_images_with_path

file_with_path = {
    '/': ['img1', 'img2'],
    '/wallpaper': ['wall1', 'wall2'],
    '/wallpaper/clicked': ['click1', 'click2'],
    '/wallpaper/downloads': ['down1', 'down2'],
    '/holi':[],
    '/holi/home': ['home_holi1', 'home_holi2'],
    '/holi/bang': ['bang_holi1', 'bang_holi2'],
}

folder_with_path = {
    '/': ['/wallpaper', '/holi']
    '/wallpaper': ['/wallpaper/clickd', '/wallpaper/downloads'],
    '/wallpaper/clickd': [],
    '/wallpaper/downloads': [],
    '/holi': ['/holi/home', '/holi/bang'],
    '/holi/home': [],
    '/holi/bang': [],
}

