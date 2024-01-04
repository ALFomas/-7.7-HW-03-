import django_filters
from django.forms.widgets import DateInput
from .models import Post, Author


class PostFilter(django_filters.FilterSet):
    """class post filter"""
    title = django_filters.CharFilter(lookup_expr='icontains',
                                      label='title'
                                      )
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all(),
                                              label='author',
                                              empty_label='select the author'
                                              )
    start_date = django_filters.DateFilter(field_name='data_create',
                                           label='date after',
                                           lookup_expr='gte',
                                           widget=DateInput(attrs={'type': 'date'}),
                                           )
    end_date = django_filters.DateFilter(field_name='data_create',
                                         lookup_expr='lte',
                                         label='date before',
                                         widget=DateInput(attrs={'type': 'date'}, )
                                         )

    class Meta:
        model = Post
        fields = ['title', 'author', ]
