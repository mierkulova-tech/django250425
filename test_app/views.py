from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest, user_name):
    # DB request
    # data serialization
    # create Response

    return HttpResponse(
        f"<h1>Hello from our first endpoint!!!!!  --  {user_name}</h1>"
    )
