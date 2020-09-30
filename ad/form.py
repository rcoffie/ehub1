from django.forms import ModelForm
from .models import *

class AdForm(ModelForm):
  class Meta:
    model = Ad
    fields = '__all__'