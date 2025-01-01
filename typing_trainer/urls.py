from django.contrib import admin
from django.urls import path, include
from trainer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.typing_test, name='typing_test'), 
    path('learn/', views.learn, name='learn'),
    path('custom/', views.custom, name='custom'),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
