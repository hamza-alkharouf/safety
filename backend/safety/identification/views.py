
from rest_framework.views import APIView
from .models import Coin
from .serializers import CoinSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, mixins
from django.db.models import Q
import math
# #5 Mixins 
# #5.1 mixins list
# class coin_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Coin.objects.all()
#     serializer_class = CoinSerializer

#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)

# #5.2 mixins get put delete 
# class coin_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Coin.objects.all()
#     serializer_class = CoinSerializer
#     def get(self, request, pk):
#         return self.retrieve(request)
#     def put(self, request, pk):
#         return self.update(request)
#     def delete(self, request, pk):
#         return self.destroy(request)










#get coins and Create coin 
class coin_list(APIView):
    def get(self, request):
        search = request.GET.get('search')
        sort = request.GET.get('sort')
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('page-size', 1))

        print(per_page)
        coin = Coin.objects.all()

        if search:
            coin = coin.filter(Q(name__icontains=search) | Q(currency__icontains=search))

        if sort == 'asc':
            coin = coin.order_by('name')
        elif sort == 'desc':
            coin = coin.order_by('-name')

        total = coin.count()
        start = (page - 1) * per_page
        end = page * per_page

        serializer = CoinSerializer(coin[start:end], many=True)
        return Response({
            'data': serializer.data,
            'total': total,
            'page': page,
            'pageSize':per_page,
            'last_page': math.ceil(total / per_page)
        })


    def post(self, request):
        serializer = CoinSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)

        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


# GET PUT DELETE coin -- pk 
class  coin_detail(APIView):

    def get_object(self, pk):
        try:
            return Coin.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404
    def get(self, request, pk):
        coin = self.get_object(pk)
        serializer = CoinSerializer(coin)
        return Response(serializer.data)
    def put(self, request, pk):
        coin = self.get_object(pk)
        serializer = CoinSerializer(coin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        coin = self.get_object(pk)
        print(coin)
        coin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
