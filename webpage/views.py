from django.shortcuts import render
import requests

from .models import Article
# Create your views here.

#view articles at random.

def Timeline(request):
	SummaryList = []
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