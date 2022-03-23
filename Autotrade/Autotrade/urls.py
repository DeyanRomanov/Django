from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views import generic

from Autotrade.view import Home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', Home.as_view()),
                  # path('', include('Autotrade.accounts.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
