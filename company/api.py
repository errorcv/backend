from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer 
from .models import Company

class CompanyAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class CompanyList(APIView):
    def get(self, request):
        model = Company.objects.all()
        serializer = CompanySerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    def get_user(self, company_id):
        try:
            model = Company.objects.get(id=company_id)
            return model
        except Company.DoesNotExist:
            return 
        
    def get(self, request, company_id):
        if not self.get_user(company_id):
            return Response(f"Company id {company_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(self.get_user(company_id))
        return Response(serializer.data)

    def put(self, request, company_id):
        if not self.get_user(company_id):
            return Response(f"Company id {company_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(self.get_user(company_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_id):
        if not self.get_user(company_id):
            return Response(f"Job Seeker with id:{company_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(company_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)