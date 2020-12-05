from import_export import resources
from .models import Teachers

class PersonResource(resources.ModelResource):
    class Meta:
        model = Teachers