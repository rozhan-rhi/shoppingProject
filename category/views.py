from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import CategoryModel
from .serializers import CategorySerializer
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema




class CategoryDetail(APIView):
    def get_category(self,pk):
        try:
            category = CategoryModel.objects.filter(id=pk).first()
            return category
        except CategoryModel.DoesNotExist:
            raise Http404

    def put(self, request: Request,pk):
        category=self.get_category(pk)
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message":"error"},status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request: Request,pk):
        category=self.get_category(pk)
        category.delete()
        return Response({"message":"category deleted"}, status.HTTP_200_OK)

    def get(self, request: Request,pk):
        category=self.get_category(pk)
        serializer=CategorySerializer(category)
        return Response(serializer.data, status.HTTP_200_OK)


class CategoryList(APIView):
    def get(self,request:Request):
        categories=CategoryModel.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self,request:Request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response({"message":"error"},status.HTTP_406_NOT_ACCEPTABLE)

