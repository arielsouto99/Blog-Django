from applications.home.models import Home

# Procesor para recuperar email y telefono del registro home

def home_contact(request):
    home = Home.objects.latest('created')
    return {
        'phone': home.phone,
        'correo': home.contact_email,
    }