from django_filters import rest_framework as filters
from .models import Todo


class TodoFilter(filters.FilterSet):
    status = filters.CharFilter(method="filter_by_status")

    class Meta:
        model = Todo
        fields = ["status"]

    def filter_by_status(self, queryset, name, value):
        if value.lower() == "completed":
            return queryset.filter(is_completed=True)
        if value.lower() == "pending":
            return queryset.filter(is_completed=False)
        return queryset.none()  # invalid status -> empty results