from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8000/user/hello-world
# => Hello World


def hello(request) -> HttpResponse:
    """
    /user/hello-world

    Eingabe ist das request-Objekt
    Rückgabke ist HttpRepsonse
    """
    return HttpResponse("Hello Welt")
