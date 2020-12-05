from django.shortcuts import render
from .models import Teachers
from django.http import HttpResponse
from .resources import PersonResource
from tablib import Dataset
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Teachers


class HomePageView(TemplateView):
    template_name = 'index.html'



class SearchResultsView(ListView):
    model = Teachers
    template_name = 'search_result.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Teachers.objects.filter(
            Q(last_name__startswith=query) 
        )
        return object_list

class SearchResultsViewSubject(ListView):
    model = Teachers
    template_name = 'search_result.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Teachers.objects.filter(
            Q(subjects_taught__icontains=query)
        )
        return object_list



def Profile(request,id):
    teach = Teachers.objects.get(id=id)
    print("check id",teach)
    return render(request, "profile.html", {"teacher":teach})

    

def index(request):

    people = Teachers.objects.all()
    return render(request, 'index.html',{'people':people})


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response



def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'import.html')