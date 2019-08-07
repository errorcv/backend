from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from utils.error_codes import ResponseCodes
from utils.generic_json_creator import create_response
from django.http import JsonResponse
from .models import College
from users.models import Profile
from .serializers import CollegeSerializer
from JH_RestAPI import pagination


@csrf_exempt
@api_view(["GET"])
def colleges(request):
    q = request.GET.get('q')
    if q is None:
        colleges = College.objects.all()
    else:
        colleges = College.objects.filter(name__icontains=q)
    paginator = pagination.CustomPagination()
    colleges = paginator.paginate_queryset(colleges, request)
    serialized_colleges = CollegeSerializer(
        instance=colleges, many=True,).data
    return JsonResponse(create_response(data=serialized_colleges, paginator=paginator), safe=False)


@csrf_exempt
@api_view(["GET"])
def majors(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.user_type < int(Profile.UserTypes.student):
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.not_supported_user),
                            safe=False)
    college = College.objects.get(pk=user_profile.college.pk)
    alumni = Profile.objects.filter(~Q(major=None), college=college)
    data = []
    for a in alumni:
        data.append(a.major)
    data = set(data)
    serialized_majors = MajorSerializer(
        instance=data, many=True, ).data
    return JsonResponse(create_response(data=serialized_majors), safe=False)