from django.http import HttpResponse

def check_status(request):
	return HttpResponse("<h6>TEST check status<h6>")