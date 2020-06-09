from django.contrib import admin
from django.urls import path
from .views import contacts, add_contact


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('add/contacts/', add_contact),
]
