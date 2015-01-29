from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rank.views.home', name='home'),
    url(r'^posts$', 'rank.views.post_list', name='post_list'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/posts$', 'rank.api.post_list', name="api_posts"),

    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
