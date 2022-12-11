from django.shortcuts import render
from .utils.fetch_speed import get_speed


def home(request):
    return render(request, 'core/home.html')



def check_speed(request):
    ping, download_rate, upload_rate = get_speed()
    context = {
        'ping': ping,
        'download_rate': download_rate,
        'upload_rate': upload_rate
    }

    return render(request, 'core/generate_speed.html', context=context)