from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('movies/',TemplateView.as_view(template_name="index.html")),
]