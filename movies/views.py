from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .models import Movie
from .serializers import MoviesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .permissions import MyCustomPermission


class MovieViews (APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]
    
    
    def get (self, request):
        all_moviels = Movie.objects.all()
        serializer = MoviesSerializer(all_moviels, many=True)
        return Response(serializer.data)

    def post (self, request):
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class MovieParamsViews (APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get (self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

    def delete (self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



# Create your views here.