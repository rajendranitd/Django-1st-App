from django.conf.urls import include, url
from django.contrib import admin
from . import views
from djangoapp.views import login_redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	#redirect pages
	url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

