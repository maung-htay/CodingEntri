from django.db import transaction
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .ProductSerializer import ProductSerializer

# Generic
from rest_framework import generics, mixins


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send a django signal


# Update api View
class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title


# Delete Api View
class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# By Id
class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # look field primary key


# By List
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_create_list_api_view = ProductListCreateApiView.as_view()
product_detail_view = ProductDetailApiView.as_view()
product_list_api_view = ProductListApiView.as_view()
product_update_api_view = ProductUpdateApiView.as_view()
product_destroy_api_view = ProductDeleteApiView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        # get by id
        if pk is not None:
            # queryset = Product.objects.get(id=pk)
            # data = ProductSerializer(queryset).data
            # return Response(data)
            obj = get_object_or_404(Product, id=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        else:
            # list view
            print("list ")
            product_obj = Product.objects.all()
            product = ProductSerializer(product_obj, many=True).data
            return Response(product)

    elif method == 'POST':
        # get_object_or_404
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'msg': 'Error occur'}, status=404)


# Mixing View
class ModelMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # permission_classes = IsAdminUser

    def get(self, request, *args, **kwargs):
        print(kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'This is mixing view example'
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


model_mixin_view = ModelMixinView.as_view()


@api_view(['GET'])
def say_hello(request, *args, **kwargs):
    print(request.body)
    print(request.GET)
    return Response({"msg": "Hello Welcome"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@transaction.atomic
def get_products(request, *args, **kwargs):
    if request.method == 'GET':
        product_obj = Product.objects.all()
        if product_obj is None:
            return Response({'data': []})
        # product = model_to_dict(product_obj,
        #                         fields=['id', 'title', 'price', 'discount_price'])
        product = ProductSerializer(product_obj, many=True).data
        return Response(product)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(serializer.data)
        return Response({'msg': 'Error occur'})
