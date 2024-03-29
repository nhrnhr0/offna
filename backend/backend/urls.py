"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from resourses.api import sizes_api,sizes_groups_api,detail_sizes_api,detail_sizes_groups_api,colors_api,detail_colors_api,categories_api,detail_categories_api,products_api,detail_products_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/sizes/', sizes_api.as_view()),
    path('api/sizes/<int:pk>/', detail_sizes_api.as_view()),
    
    path('api/sizes_groups/', sizes_groups_api.as_view()),
    path('api/sizes_groups/<int:pk>/', detail_sizes_groups_api.as_view()),
    
    path('api/colors/', colors_api.as_view()),
    path('api/colors/<int:pk>/', detail_colors_api.as_view()),
    
    path('api/categories/', categories_api.as_view()),
    path('api/categories/<int:pk>/', detail_categories_api.as_view()),
    
    path('api/products/', products_api.as_view()),
    path('api/products/<int:pk>/', detail_products_api.as_view()),
    # path('api/products/<int:pk>/header_image/', detail_products_api_header_image.as_view()),
    
    path("__debug__/", include("debug_toolbar.urls")),

]



print('settings: ', settings)
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)