from django.http import HttpResponse

def aboutUS(request):
    return HttpResponse("Welcome TO WSCube Tech")

def courseDetails(request,courseid):
    return HttpResponse(courseid)