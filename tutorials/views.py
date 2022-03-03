from django.shortcuts import render
from.models import Tutorial
from rest_framework.views import APIView
from.serializers import TutorialSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class tutorialview(APIView):
    def get(self,request):
        data = Tutorial.objects.all()
        serialized_data =TutorialSerializer(data,many=True)
        return Response(serialized_data.data)
    def post(self,request):
        data = request.data
        serialized_data = TutorialSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(request,pk):
        obj = Tutorial.objects.get(pk=pk)
        serializer = TutorialSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(request,pk):
        try:
            obj = Tutorial.ojects.get(pk=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            raise Http404






# @api_view(['GET','POST','DELETE'])
# def tutorial_list(request):
#     pass
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     # find tutorial by pk (id)
#     try:
#         tutorial = Tutorial.objects.get(pk=pk)
#     except Tutorial.DoesNotExist:
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#         # GET / PUT / DELETE tutorial
#
#
# @api_view(['GET'])
# def tutorial_list_published(request):
# # GET all published tutorials