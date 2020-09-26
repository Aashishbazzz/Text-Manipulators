# Not made my django

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index_2.html')

	
def analyze(request):

	return render(request, 'analyze_2.html')
	
	
	djtext = request.GET.get('text', 'default')
	removepunc = request.GET.get('removepunc', 'off')
	fullcaps = request.GET.get('fullcaps', 'off')
	newlineremover = request.GET.get('newlineremover', 'off')
	extraspaceremover = request.GET.get('extraspaceremover', 'off')
	email = request.GET.get('email', 'off')

    #Check which checkbox is on
	if removepunc == "on":
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
		params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
		return render(request, 'analyze_2.html', params)
	
	elif(fullcaps=="on"):
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
			
		params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
		return render(request, 'analyze_2.html', params)
		
	elif(extraspaceremover=="on"):
		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index+1]==" "):
				analyzed = analyzed + char
		
		params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
		return render(request, 'analyze_2.html', params)
		
	elif (newlineremover == "on"):
		analyzed = ""
		for char in djtext:
			if char != "\n":
				analyzed = analyzed + char
				
		params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
		
		return render(request, 'analyze_2.html', params)
		
	elif(extraspaceremover=="on"):
		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index+1]==" "):
				analyzed = analyzed + char
		
		params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
		return render(request, 'analyze_2.html', params)
		
	else:
		return HttpResponse("Error")

