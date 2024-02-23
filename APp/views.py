from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response

class ProductCrud(ViewSet):
    def list(self, request):
        PQS = Product.objects.all()
        PJD = ProductSerializer(PQS, many = True)
        return Response(PJD.data)
    def retrieve(self, request, pk):
        PQS = Product.objects.get(pid = pk)
        PJD = ProductSerializer(PQS)
        return Response(PJD.data)
    def create(self, request):
        PMSD = ProductSerializer(data = request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'Product is created'})
        return Response({'Failed':'Product is not created'})
    def update(self, request, pk):
        PO = Product.objects.get(pk = pk)
        UPO = ProductSerializer(PO,data = request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'Product is Updated'})
        return Response({'Failed':'Product is not Updated'})
    def partial_update(self, request, pk):
        PO = Product.objects.get(pk = pk)
        UPO = ProductSerializer(PO,data = request.data,partial = True)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'Product is partially Updated'})
        return Response({'Failed':'Product is not Updated'})
    def destroy(self, request, pk):
        PO = Product.objects.get(pk = pk)
        PO.delete()
        return Response({'message':'Product Deleted Successfully'})

# class ProductCrudActions(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer