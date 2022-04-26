from datetime import timedelta, datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
# Modelos
from applications.entrada.models import Entry

class EntrySitemap(Sitemap):
    changefreq = "weekly" # Recibir cambios cada semana
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Entry.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.created
        
# Redefiniendo (regla que pide django para que el sitemap funcione correctamente)
class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self, names):
        self.names = names
        
    def items(self):
        return self.names
    
    def changefreq(self, obj):
        return 'weekly'
    
    def lastmod(self, obj):
        return datetime.now()

    def location(self,obj):
        return reverse_lazy(obj)