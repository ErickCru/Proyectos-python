from django.shortcuts import get_object_or_404
from rest_framework import views, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Pelicula, PeliculaFavorita
from .serializers import PeliculaFavoritaSerializer, PeliculaSerializer


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'estreno']
    ordering_fields = ['favoritos']


class MarcarPeliculaFavorita(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):

        pelicula = get_object_or_404(
            Pelicula, id=self.request.data.get('id', 0)
        )

        favorita, created = PeliculaFavorita.objects.get_or_create(
            pelicula=pelicula, usuario=request.user
        )

        # Por defecto suponemos que se crea bien
        content = {
            'id': pelicula.id,
            'favorita': True
        }

        # Si no se ha creado es que ya existe, entonces borramos el favorito
        if not created:
            favorita.delete()
            content['favorita'] = False

        return Response(content)


class ListarPeliculasFavoritas(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET -> Se usa para hacer lecturas

    def get(self, request):

        peliculas_favoritas = PeliculaFavorita.objects.filter(
            usuario=request.user)
        serializer = PeliculaFavoritaSerializer(
            peliculas_favoritas, many=True)

        return Response(serializer.data)
