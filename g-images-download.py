# автоматизированное скачивание картинок для самых маленьких

# pip install git+https://github.com/Joeclinton1/google-images-download.git

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords": '',
             "limit": 0,
             "print_urls": True
             }

keyword = input('Что будем скачивать? ').strip()
imglimit = int(input('Сколько будем скачивать? ').strip())

arguments['keywords'] = keyword
arguments['limit'] = imglimit

paths = response.download(arguments)
