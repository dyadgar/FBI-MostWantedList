from django.urls import path, include
from django.conf import settings
from . import views
from django.views.static import serve
from django.conf.urls import url

from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('<username>/', views.profile, name='profile'),




]

# if settings.DEBUG:
#     urlpatterns += url(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         })