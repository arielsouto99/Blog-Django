from django.db import models

class EntryManager(models.Manager):
    """ Procedimiento para entrada """

    def entrada_portada(self):
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created').first()

    
    def entradas_home(self):
        # Devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home = True,
        ).order_by('-created')[:4] # Primeros 4

    
    def entradas_recientes(self):
        # Devuelve las ultimas 6 entradas recientes
        return self.filter(
            public=True,
        ).order_by('-created')[:6] # Ultimos 6

    
    def buscar_entrada(self, kword, categoria):
        # Procedimiento para buscar entradas por categoria o palabra clave
        if len(categoria) > 0:
            return self.filter(
                category__shorname=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')