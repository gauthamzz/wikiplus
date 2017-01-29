from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from .views import (

	Timeline,
	RelatedTimeline,
	)

urlpatterns = [
	url(r'^$', Timeline,name="Timeline"),
	url(r'(?P<Topic>[A-Za-z0-9]+)$',RelatedTimeline, name='RelatedTimeline'),
	# url(r'^rank$', rank,name="ranks"),
	# url(r'^$',index,name="index"),

	]
