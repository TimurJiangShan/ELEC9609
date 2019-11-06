from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import Goods, GoodsCategory, HotSearchWords, Banner
from .serializers import GoodsSerializer, CategorySerializer, BannerSerializer, IndexCategorySerializer
from .filters import GoodsFilter

class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100

class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    goods list page, pagination, search, order, filter
    '''
    #throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ['name', 'goods_brief', 'goods_desc']
    ordering_fields = ['sold_num', 'shop_price']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        goods category list data
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

class BannerViewset(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    get banner image list
    '''
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer

class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    home page category
    '''
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["Clothing", "Shoes", "Others"])
    serializer_class = IndexCategorySerializer