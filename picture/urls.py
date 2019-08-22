from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    url(r'^$',views.location,name='location'),
    url(r'^mombasa/', views.mombasa, name='mombasa'),
    url(r'^kisii/', views.kisii, name='kisii'),
    url(r'^nakuru/', views.nakuru, name='nakuru'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
