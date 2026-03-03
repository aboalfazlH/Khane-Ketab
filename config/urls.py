from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("apps.accounts.urls")),
    path('library/',include("apps.library.urls")),
    path('cart/',include("apps.cart.urls")),
    path('race/',include("apps.race.urls")),
    path('',include("apps.core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
