from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.home, name="home")
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls")),
                    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
