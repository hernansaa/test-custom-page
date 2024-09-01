from django.shortcuts import render
from .forms import QuotationAdminForm

# Create your views here.

def test(request):
  form = QuotationAdminForm
  context = {
    'form': form,
  }

  return render(request, 'quotations/test.html', context)