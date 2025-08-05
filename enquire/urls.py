from django.urls import path
from enquire.views import EnquireCreateView

urlpatterns = [
    path('contact_details/contact/', EnquireCreateView.as_view(), name='enquire-create'),
]