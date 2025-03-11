from django.contrib import admin
from django.urls import path, include
from trainer import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Typing Trainer API",
        default_version='v1',
        description="API для аутентификации, работы с пользователями и статистики тренировок",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.typing_test, name='typing_test'), 
    path('learn/', views.learn, name='learn'),
    path('custom/', views.custom, name='custom'),
    path('users/', include('users.urls')),
    path('swagger/', schema_view.as_view(), name='swagger-docs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
