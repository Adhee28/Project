
from django.contrib import admin
from django.urls import path,include
from new import views 




urlpatterns = [
    path('', include('new.urls')),
    path('admin/', admin.site.urls),
    path('accouts/', include('accouts.urls')),
    path('sendmails/', include('sendmails.urls')),
]
