from django.shortcuts import render
from django.http import HttpResponse
from  first_app.models import Topic, AccessRecord, Webpage

# Create your views here.
def index(request):
    # here in place of request you can add any name but one variable should always be necessary
    webpages_list=AccessRecord.objects.order_by('date')
    # order_by is used to sort the fetched data in either ascending or descending according to one or more column
    date_dict={'access_records':webpages_list}
    # with render function you have to create a dictionary with variables as key which you have written in html file
    return render(request,'first_app/index.html',context=date_dict)
