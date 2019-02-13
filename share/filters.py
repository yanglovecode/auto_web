import django_filters

from share.models import Upload


class ProductFilter(django_filters.FilterSet):



    DownloadDocount = django_filters.NumberFilter(lookup_expr='iexact')  # iexact表示精确匹配, 并且忽略大小写
    code = django_filters.CharFilter(lookup_expr='icontains') #icontains表示模糊查询（包含），并且忽略大小写
    Datatime = django_filters.DateFilter(look_expr='exact')  #exact表示精确匹配
    name = django_filters.CharFilter(lookup_expr="icontains")

    # desc = django_filters.CharFilter('description', lookup_expr='contains') #对'description'字段进行操作，不填默认为desc
    #price__lte = django_filters.NumberFilter('price', lookup_expr='lte') #lte表示小于
    #price__gte = django_filters.NumberFilter('price', look_expr='gte')  # gte表示大于
class Meta:
        model = Upload
        fields = ['DownloadDocount', 'code', 'Datatime', 'name']
