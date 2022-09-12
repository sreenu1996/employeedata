

# Create your views here.
from os import stat
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import EmployeModel
from .serializers import EmploySerializer
  


@api_view(['GET'])
def ApiOverview(request):
    try:
        api_urls = {
            'all_items': '/',
            'Search by Category': '/?category=category_name',
            'Search by Subcategory': '/?subcategory=category_name',
            'Add': '/create',
            'Update': '/update/pk',
            'Delete': '/item/pk/delete'
        }
    
        return Response(api_urls,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message":"failed",status:status.HTTP_400_BAD_REQUEST})

@api_view(['GET', 'POST'])
def Emp_list(request):
    if request.method == 'GET':
        try:
            Emp = EmployeModel.objects.all()

            name = request.GET.get('name', None)
            if name is not None:
                Emp = EmployeModel.filter(name__icontains=name)

            Emp_serializer = EmploySerializer(Emp, many=True)
            return JsonResponse(Emp_serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({'message': 'The empdata details not exist','sucuss':'false'},status=status.HTTP_400_BAD_REQUEST)

        #return JsonResponse({'message': 'The empdata details found','sucuss':"True"},Emp_serializer.data)
            # 'safe=False' for objects serialization

    elif request.method == 'POST':
        try:
            Emp_data = JSONParser().parse(request)
            Employ_serializer = EmploySerializer(data=Emp_data)
            if Employ_serializer.is_valid():
                Employ_serializer.save()
                return JsonResponse(Employ_serializer.data, status=status.HTTP_201_CREATED)
            
            return JsonResponse({'message':"employee created scussful"},Employ_serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return JsonResponse({'message':"employee created failed",'succuss':'false'},Employ_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def Emp_detail(request, pk):
    try:
        Empdata = EmployeModel.objects.get(pk=pk)
    except EmployeModel.DoesNotExist:
        return JsonResponse({'message': 'The empdata does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            Emp_serializer = EmploySerializer(Empdata)
            return JsonResponse(Emp_serializer.data,safe=False)

        except Exception as e:
            return JsonResponse({'message': 'The empdata details not exist','sucuss':'false'},Emp_serializer.data)


    elif request.method == 'PUT':
        try:
            Emp_data = JSONParser().parse(request)
            Emp_serializer = EmploySerializer(Empdata, data=Emp_data)
            if Emp_serializer.is_valid():
                Emp_serializer.save()
                return JsonResponse({'message':"employee created sucuss",'succuss':'True'},Emp_serializer.data)
        except Exception as e:
            return JsonResponse({'message':"employee created failed",'succuss':'True'},Emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            Empdata.delete()
            return JsonResponse({'message': 'emp details was deleted successfully!','succuss':'True'}, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'message': 'emp details was not found details','succuss':'False'}, status=status.HTTP_200_OK)

