from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer, UserProfileSerilalizer
from .models import UserProfile
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile
from rest_framework.filters import SearchFilter


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function(get,post,patch,put,delete)",
            "Is simitlar to a traditional Django View",
            "Gives you the most control over your application logic",
        ]
        return Response({"message": "hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello! {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses HTTP methods as function(list,create,retrieve,update,partial_update)",
            "Automatically maps to URLs using routers",
            "Provide more functionality with less code",
        ]
        return Response({"message": "hello!", "a_viewset": a_viewset})


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerilalizer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ("name", "email")
