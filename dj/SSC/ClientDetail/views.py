from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PropertyInquirySerializer
from .models import PropertyInquiry
import json

class PropertyInquiryViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'property_inquiry_form.html')  # Render your HTML form page

    def create(self, request):
        data = json.loads(request.body)
        print(data)
        # serializer = PropertyInquirySerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"message": "Inquiry submitted successfully!"}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"Status":"True"})
