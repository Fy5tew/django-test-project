import requests

from django.http import JsonResponse, HttpResponse

# Create your views here.

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

def index_view(request):
    return HttpResponse("<h1>Index page!!!!!!!!!</h1>")


def test_view(request):
    return JsonResponse({"running": True})


def avby_view(request):
    response = requests.get('https://cars.av.by/audi/a8', headers=HEADERS)
    response.raise_for_status()
    return HttpResponse(response.text)


def kufar_view(request):
    response = requests.get('https://auto.kufar.by/l/cars/audi-a8?cur=BYR', headers=HEADERS)
    response.raise_for_status()
    return HttpResponse(response.text)
