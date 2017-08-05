from django.conf.urls import url
from webApp import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', v.index, name='home'),
    url(r'^(?P<desc_id>[\w+-]{1,})$', v.redirectDDG, name='redirectDDG'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
