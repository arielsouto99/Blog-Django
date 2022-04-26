"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Seo
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap


urlpatterns_main = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls')),
    path('', include('applications.home.urls')),
    path('', include('applications.entrada.urls')),
    path('', include('applications.favoritos.urls')),
    # urls para ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# objeto site map que genera xml
sitemaps = {
    'site':Sitemap(
        [
            'home_app:index'
        ]
    ),
    'entradas':EntrySitemap
}

urlpatterns_sitemap = [
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name = 'django.contrib.sitemaps.views.sitemap')
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap