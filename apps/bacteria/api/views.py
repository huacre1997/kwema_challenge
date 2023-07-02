from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.base import calculate_bacteria
from apps.bacteria.api.serializers import BacteriaSerializer

class GetNumberOfBacteriaView(APIView):
    """
    Vista de API para obtener el número de bacterias.
    """

    def post(self, request):
        """
        Método POST para procesar la solicitud de obtener el número de bacterias.
        """
        serializer = BacteriaSerializer(data=request.data)  # Inicializar el serializador con los datos de la solicitud.
        if serializer.is_valid():  # Verificar si el serializador es válido.
            # Obtener los datos validados del serializador.
            days = serializer.validated_data.get("days")
            maturation_period = serializer.validated_data.get("maturation_period")
            life_expectancy = serializer.validated_data.get("life_expectancy")
            reproduction_rate = serializer.validated_data.get("reproduction_rate")
            # Calcular el número total de bacterias utilizando la función "calculate_bacteria".
            total_bacteria = calculate_bacteria(
                days, maturation_period, life_expectancy, reproduction_rate
            )
            # Devolver una respuesta con el número total de bacterias.
            return Response({"total_bacteria": total_bacteria}, status=status.HTTP_200_OK)
        # Si el serializador no es válido, devolver los errores de validación.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)