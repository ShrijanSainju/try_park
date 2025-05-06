# processor/views.py
import os
import cv2
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_image(request):
    context = {}
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_path = fs.path(filename)

        # Process with OpenCV: convert to grayscale
        img = cv2.imread(uploaded_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_path = uploaded_path.replace('.', '_gray.')
        cv2.imwrite(gray_path, gray)

        context['original'] = fs.url(filename)
        context['processed'] = fs.url(os.path.basename(gray_path))

    return render(request, 'upload.html', context)
