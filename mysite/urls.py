from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'todo.views.home_page', name='home'),
	url(r'^$', 'todo.views.mainmenu', name='mainmenu'),
	
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^statinfo/$', 'todo.views.stat_info'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/accounts/login'}),
    (r'^mainmenu/$', 'todo.views.mainmenu'),
	#(r'^mainmenu/(?P<action>\w+)/$', 'todo.views.mainmenu'),
    (r'^updateitem/(-?\d)/(-?\d)/$', 'todo.views.updateitem'),
    (r'^additem/$', 'todo.views.additem'),
	
	#url(r'^login/$', 'todo.views.login_user'),
	#(r'^login/$', 'django.contrib.auth.views.login'),
    #(r'^logout/$', 'django.contrib.auth.views.logout'),
)