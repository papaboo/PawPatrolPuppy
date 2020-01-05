from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

def download_paw_patrol(folder, query): 
    arguments = {"keywords": query, 
                "output_directory": "C:/Users/Asger Hoedt/Development/MachineLearning/PawPatrol",
                "image_directory": folder,
                # "format": "jpg",
                "limit": 50, 
                "print_urls": True}

    try:
        paths = response.download(arguments)
        print(paths)
    except Exception as e:
        print('Exception ' + str(e))

marshall_query = 'paw patrol marshall -chase -rubble -rocky -skye -zuma -everest'
chase_query = 'paw patrol -marshall chase -rubble -rocky -skye -zuma -everest'
rubble_query = 'paw patrol -marshall -chase rubble -rocky -skye -zuma -everest'
rocky_query = 'paw patrol -marshall -chase -rubble rocky -skye -zuma -everest'
zuma_query = 'paw patrol -marshall -chase -rubble -rocky -skye zuma -everest'
skye_query = 'paw patrol -marshall -chase -rubble -rocky skye -zuma -everest'

# download_paw_patrol("marshall", marshall_query)
# download_paw_patrol("chase", chase_query)
# download_paw_patrol("rubble", rubble_query)
# download_paw_patrol("rocky", rocky_query)
# download_paw_patrol("zuma", zuma_query)
download_paw_patrol("skye", skye_query)
