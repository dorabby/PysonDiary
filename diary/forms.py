from django.forms import ModelForm
from .models import Page

class PageForm(ModelForm):
  class Meta:
    model=Page
    # htmlなどで呼び出せるようにする
    fields=["title","body","page_date","picture"]