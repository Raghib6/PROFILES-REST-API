from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function(get,post,patch,put,delete)",
            "Is simitlar to a traditional Django View",
            "Gives you the most control over your application logic",
        ]
        return Response({"message": "hello!", "an_apiview": an_apiview})
