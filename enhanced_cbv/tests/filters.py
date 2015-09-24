import django_filters

from .models import Author

class AuthorFilterSet(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ['name', ]
