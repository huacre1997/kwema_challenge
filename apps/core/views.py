from django.http import JsonResponse


def main_view(self):
    return JsonResponse({"message": "Server on!"})
