from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from home import views


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', 'search.views.search', name='search'),
    url(r'product_list/$', views.product_list, name='product_list'),
    url(r'inventory_logs/$', views.inventory_logs, name='inventory_logs'),
    url(r'order/$', views.base_order, name='base_order'),
    url(r'order/(\d+)/$', views.order, name='order'),
    url(r'metrics/$', views.metrics, name='metrics'),
    url(r'^sales_data/(\d+)/$', views.get_sales_data, name='sales_data'),
    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
