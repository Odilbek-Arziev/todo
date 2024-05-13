from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app.urls', 'app'), namespace='app')),
    path('ale', include(('ale.urls', 'app'), namespace='app')),
    path('ale2', include(('ale2.urls', 'app'), namespace='app')),
    path('ale3', include(('ale3.urls', 'app'), namespace='app')),
    path('ale4', include(('ale4.urls', 'app'), namespace='app')),
] + staticfiles_urlpatterns()
