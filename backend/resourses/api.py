from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductSize,ProductSizeGroup
from .serializers import ProductSizeSerializer, ProductSizeGroupSerializer


def apply_filters(request, queryset, filters_fields):
    #request: http://localhost:5173/dashboard/sizes?name__icontains=t&order=5&group_in=2
    # queryset: ProductSize.objects.all()
    # filters_fields: [{'db_key': 'size', 'url_key':'name','lookups':['icontains', '']},{'db_key': 'order', 'url_key': 'order','lookups': ['', 'lte', 'gte']},{'db_key': 'size_group', 'url_key': 'size_group', 'lookups': ['in']},]
    for filter_field in filters_fields:
        key = filter_field['url_key']
        lookups = filter_field['lookups']
        for lookup in lookups:
            url_key = key
            db_key = filter_field['db_key']
            if lookup != '':
                url_key += '__' + lookup
                db_key += '__' + lookup
            if url_key in request.GET:
                if request.GET[url_key] == '': continue
                clean_func = filter_field.get('input_clean', lambda x: x)
                value = clean_func(request.GET[url_key])
                filter = {db_key: value}
                print('filter: ', filter)
                queryset = queryset.filter(**filter)
    return queryset
class sizes_api(APIView):
    filters_fields = [
                        {'db_key': 'size_group', 'url_key': 'group', 'lookups': ['in'], 'input_clean': (lambda x: x.split(','))},
                        {'db_key': 'size', 'url_key':'name','lookups':['icontains', '']},
                      {'db_key': 'order', 'url_key': 'order','lookups': ['', 'lte', 'gte'], 'input_clean': int},
                      ]
    def get(self, request):
        sizes = ProductSize.objects.all()
        qs = apply_filters(request, sizes, self.filters_fields)
        serializer = ProductSizeSerializer(qs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)

class detail_sizes_api(APIView):
    def get(self, request, pk):
        sizes = ProductSize.objects.get(pk=pk)
        serializer = ProductSizeSerializer(sizes)
        return Response(serializer.data)
    def put(self, request, pk):
        sizes = ProductSize.objects.get(pk=pk)
        serializer = ProductSizeSerializer(sizes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, pk):
        sizes = ProductSize.objects.get(pk=pk)
        sizes.delete()
        return Response(status=204)


class sizes_groups_api(APIView):
    def get(self, request):
        sizes = ProductSizeGroup.objects.all()
        serializer = ProductSizeGroupSerializer(sizes, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSizeGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)