from django.shortcuts import (redirect, render)

import webApp.ddScrape


def index(request):
    return render(request, "webApp/index.html")


def redirectDDG(request, desc_id):
    return redirect(webApp.ddScrape.getLink(desc_id))
