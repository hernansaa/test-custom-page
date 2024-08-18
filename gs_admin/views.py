from django.shortcuts import render

# Create your views here.

def dashboard_callback(request, context):
    context.update({
        "custom_variable": "value",
    })

    return context