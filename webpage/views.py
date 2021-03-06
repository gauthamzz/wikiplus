from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect

import datetime
from .models import Article
# Create your views here.

#view articles at random.

def Timeline(request):
	SummaryList = []
	query = request.GET.get("q")
	if query :
		return HttpResponseRedirect("/webpage/"+query)
	for item in range (10):
		Summary= requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary',verify=False)
	
		SummaryData = Summary.json()
		SummaryList.append(SummaryData)

	context={
	"summary_list" : SummaryList
	}
	return render(request,"timeline.html",context)


	# TempData = Temp.json()
		# TempTitle = TempData["items"][0]["title"]
		# Summary = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/' + TempTitle) 

def RelatedTimeline(request,Topic):
	#returns top 5 related to a topic
	RelatedList = requests.get('https://en.wikipedia.org/api/rest_v1/page/related/'+ Topic,verify=False)
	RelatedListData = RelatedList.json()

	query = request.GET.get("q")
	if query :
		return HttpResponseRedirect("/webpage/related/"+query)


	context={
	"Data" : RelatedListData
	}
	return render(request,"relatedtimeline.html",context)

def Today(request):
	List= requests.get('https://en.wikipedia.org/api/rest_v1/feed/featured/'+ datetime.date.today().strftime ("%Y/%m/%d"))
	ListData = List.json()

	query = request.GET.get("q")
	if query :
		return HttpResponseRedirect("/webpage/related/"+query)


	context={
	"Data" : ListData
	}
	return render(request,"today.html",context)