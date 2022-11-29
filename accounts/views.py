from django.urls import reverse_lazy
from django.views.generic import CreateView

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import HTML, Layout, Submit

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
