from django.urls import path, include

urlpatterns = [
    path('',
         include('crm.lead.urls')
         ),
]
