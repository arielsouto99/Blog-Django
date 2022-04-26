from django.db import models
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    """ Modelo pagina principal """

    title = models.CharField ('Nombre', max_length=50)
    description = models.TextField()
    about_title = models.CharField ('Titulo nosotros', max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField('Email de contacto', blank=True, null=True)
    phone = models.CharField('Telefono', max_length=20)

    class Meta:
        verbose_name = 'Pagina principal'
        verbose_name_plural = 'Pagina principal'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):
    """ Modelo suscriptores"""

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    """ Modelo contacto """
    
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name