from django.urls import path

from .views import home, test, test2, top_sellers

urlpatterns = [
    path("", home, name = 'home'), 
    path("top_sellers", top_sellers, name='top_sellers'), 
    path("test/", test, name = 'test'), 
    path("test2/", test2, name = 'test2'), 
]   
