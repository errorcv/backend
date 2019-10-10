from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobPositionSerializer
from .models import JobPosition


class JobPositionAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class JobPositionList(APIView):
    def get(self, request):
        model = JobPosition.objects.all()
        serializer = JobPositionSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobPositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobPositionDetail(APIView):
    def get_user(self, job_id):
        try:
            model = JobPosition.objects.get(id=job_id)
            return model
        except JobPosition.DoesNotExist:
            return 
        
    def get(self, request, job_id):
        if not self.get_user(job_id):
            return Response(f"Job ID:{job_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = JobPositionSerializer(self.get_user(job_id))
        return Response(serializer.data)

    def put(self, request, job_id):
        if not self.get_user(job_id):
            return Response(f"Job Seeker with id:{job_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = JobPositionSerializer(self.get_user(job_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, job_id):
        if not self.get_user(job_id):
            return Response(f"Job Seeker with id:{job_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(job_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)