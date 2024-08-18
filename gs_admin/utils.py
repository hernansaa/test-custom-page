from providers.models import School

# utils.py
def dashboard_callback(request, context):
    context.update({
        "variable": School.objects.all()
    })

    return context