from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from .views import (

	Timeline,
	RelatedTimeline,
	Today,
	)

urlpatterns = [
	url(r'^$', Timeline,name="Timeline"),
	url(r'related/(?P<Topic>[^/]+)$',RelatedTimeline, name='RelatedTimeline'),
	url(r'now/$',Today, name='Today'),
	# url(r'^rank$', rank,name="ranks"),
	# url(r'^$',index,name="index"),

	]
