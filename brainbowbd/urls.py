
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from card import views

urlpatterns = [
    path('api/card/', include('card.urls')),
    path('api/sign/', include('mgr.urls')),
    path('admin/', admin.site.urls),
    # 设置了framework后设置,访问'127.0.0.1:80'+'api'时返回first_api函数
    path('api/', views.first_api),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
