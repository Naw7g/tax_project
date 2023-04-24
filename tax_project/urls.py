from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tax_app.urls')),
]







# from django.contrib import admin
# from django.urls import include, path
# from . import views
# urlpatterns = [
#     path("", views.index,name="index") ,
#     path('admin/', admin.site.urls),
#     path("", include('tax_app.urls')),
# ]
