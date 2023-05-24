from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')




urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('chatgpt/', include('chatgpt.urls')),
    path('signlanguagetochatgpt/', include('signlanguagetochatgpt.urls')),
    path("selfchatgpt/", include("selfchatgpt.urls")),
    path('selfsignlanguagetochatgpt/', include("selfsignlanguagetochatgpt.urls")),
    #path("", test),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
