from api.models import SchoolProfile
from api.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Submitted Sucessfully', 'status':'success', 'schooldetail':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        schools = SchoolProfile.objects.all()
        serializer = ProfileSerializer(schools, many = True)
        return Response({'status':'success', 'schools':serializer.data}, status=status.HTTP_200_OK)

