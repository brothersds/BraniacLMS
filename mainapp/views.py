from django.http import HttpResponse

# функция обработчик
def hello_view(request):
    return HttpResponse("Hello world")
