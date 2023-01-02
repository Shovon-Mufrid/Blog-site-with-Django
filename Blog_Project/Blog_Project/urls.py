
from django.contrib import admin
from django.urls import path,include
from . import views 
# for MEDIA
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account/', include('Login_App.urls')),
    path('blog/', include('Blog_App.urls')),
    path('', views.Index, name='index' )
]

# FOR MEDIA
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)