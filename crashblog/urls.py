from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import about, FrontpageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FrontpageView.as_view(), name='frontpage'),
    path('about', about, name='about'),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
