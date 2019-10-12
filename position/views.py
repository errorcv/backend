from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from JH_RestAPI import pagination
from utils.generic_json_creator import create_response
from .models import JobPosition
from .serializers import JobPositionSerializer


@csrf_exempt
@api_view(["GET"])
def positions(request):
    q = request.GET.get('q')
    if q:
        positions = JobPosition.objects.filter(job_title__icontains=q)
    else:
        positions = JobPosition.objects.all()
        
    if request.GET.get('count') is not None:
        cnt = int(request.GET.get('count'))
        positions = positions[:cnt]

    paginator = pagination.CustomPagination()
    positions = paginator.paginate_queryset(positions, request)
    serialized_positions = JobPositionSerializer(
        instance=positions, many=True).data
    return JsonResponse(create_response(data=serialized_positions, paginator=paginator), safe=False)
