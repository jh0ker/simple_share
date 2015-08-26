# from django.shortcuts import render
from django.shortcuts import render
from time import time
from ipware.ip import get_ip
import os

from django.conf import settings

from share.models import File

def index(request):
    if request.method == 'POST':
        success = handle_uploaded_file(request.FILES['upload'], request.POST['note'], get_ip(request))
        return render(request, 'index.html', {'upload': True, 'upload_success': success, 'filelist': get_filelist()})
    else:
        return render(request, 'index.html', {'upload': False, 'filelist': get_filelist()})

def handle_uploaded_file(f, message, ip):
    try:
        dname = hex(int(time() * 10000000)).split('x')[1]
        fname = os.path.join(dname, str(f))

        os.makedirs(os.path.join(settings.UPLOAD_LOCATION, dname))

        with open(os.path.join(settings.UPLOAD_LOCATION, fname), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        f = File(ip=(ip if ip is not None else "UNKNOWN"), note=message, path=fname)
        f.save()

        return True

    except Exception as e:
        print(e)
        return False

def get_filelist():
    filelist = File.objects.order_by('-timestamp')
    for f in filelist:
        f.name = f.path.split(os.path.sep)[-1]
        f.path = '/'.join(['static', 'share', 'uploads', f.path])

    return filelist
