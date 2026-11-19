"""
URL configuration for eventapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atracao/', include('atracao.urls', namespace='atracao')),
    path('organizador/', include('organizador.urls', namespace='organizador')),
    path('local/', include('local.urls', namespace='local')),
    path('evento/', include('evento.urls', namespace='evento')),
    path('cupom/', include('cupom.urls', namespace='cupom')),
    path('lote/', include('lote.urls', namespace='lote')),
    path('', include('core.urls', namespace='core')),
    path('setor/', include('setor.urls', namespace='setor')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
