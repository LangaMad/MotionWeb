"""motion_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from rest_framework import permissions

schema_view = get_schema_view(  # new
    openapi.Info(
        title="Motion API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    # url=f'{settings.APP_URL}/api/v3/',

    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  path('api/', schema_view.with_ui('swagger',cache_timeout=0),
        name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui('swagger',cache_timeout=0),
        name='redoc-swagger-ui'),
  path('admin/', admin.site.urls),
  path('',include('backend.apps.api.urls')),
  path('api-token-auth', views.obtain_auth_token),
  path('accounts/', include('backend.apps.accounts.urls')),
]



