from django.contrib import admin
from django.urls import path, include
from django.apps import apps
from paypal.express.urls import urlpatterns as paypal_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('checkout/paypal/', include(paypal_urls)),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    import silk

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
