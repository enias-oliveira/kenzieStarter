from django_filters import rest_framework as filters

from .models import Project


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    state = filters.CharFilter(field_name="state", lookup_expr="iexact")

    class Meta:
        model = Project
        fields = ['name', 'state']
