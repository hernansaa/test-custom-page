from .models import NavbarItem

def site_context(request):
    navbar_items = NavbarItem.objects.filter(visible=True).order_by('order')
    
    context = {
        'navbar_items': navbar_items,
    }

    return (context)