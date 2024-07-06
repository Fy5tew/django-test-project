import requests

from django.http import JsonResponse, HttpResponse

# Create your views here.

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}

def index_view(request):
    return HttpResponse("<h1>Index page!!!!!!!!!</h1>")


def test_view(request):
    return JsonResponse({"running": True})


def url_view(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({"error": "Please, enter the url"})
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return HttpResponse(response.text)
    except Exception as ex:
        return JsonResponse({"error": str(ex)})
