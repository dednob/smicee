from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile
from rest_framework import status

# Create your views here.
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create(request):
    company_data = request.data
    slug = None
    # if 'image' in company_data:
    #     fmt, img_str = str(company_data['image']).split(';base64,')
    #     ext = fmt.split('/')[-1]
    #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
    #     company_data['image'] = img_file

    # slug = slugify(data['title'])
    # suffix = 1

    if Company.objects.filter(title__exact=company_data['name']).exists():
        print("yes")
        count = Company.objects.filter(title__exact=company_data['name']).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(company_data['name']), suffix)

    else:
        print("No")
        slug = "%s-%s" % (slugify(company_data['name']), suffix)

    company_data['slug'] = slug
    serializer = CompanySerializer(data=company_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def company_list(request):
    try:
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
                "data": serializer.data
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['GET'])
def aow_detail(request, slug):
    try:
        if slug is not None:
            company = Company.objects.get(slug=slug)
            serializer = CompanySerializer(company)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
                "data": serializer.data
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    try:
        company_data = request.data
        company = Company.objects.get(id=pk)

        # if ('image' in data and data['image']==None) and areaofwork.image != None:
        #     data.pop('image')


        # if 'image' in data and data['image'] != None :
        #     fmt, img_str = str(data['image']).split(';base64,')
        #     ext = fmt.split('/')[-1]
        #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        #     data['image'] = img_file

            # slug = slugify(data['title'])
            

        if Company.objects.filter(title__exact=company_data['name']).exists():
            print("yes")
            count = Company.objects.filter(title__exact=company_data['name']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(company_data['name']), suffix)

        else:
            slug = "%s-%s" % (slugify(company_data['name']), suffix)

        company_data['slug'] = slug

        
        serializer = CompanySerializer(company, data=company_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data updated successfully",
                'data': serializer.data

            })
        else:
            return Response({
                    'code': status.HTTP_400_BAD_REQUEST,
                    'response': "Data not found",
                    'error': serializer.errors
                })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    try:
        company = Company.objects.get(id=pk)
        company.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Data Deleted"
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })