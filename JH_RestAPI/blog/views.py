from django.shortcuts import render

from blog.models import Blog
from . import models
from .serializers import BlogSerializer
from .serializers import BlogSnippetSerializer
from django.http import JsonResponse
from utils.generic_json_creator import create_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from users.models import Profile
from utils.error_codes import ResponseCodes
from utils.logger import log
from JH_RestAPI import pagination
from utils import utils
import uuid
from datetime import datetime


@csrf_exempt
@api_view(["GET", "PUT", "POST", "DELETE"])
def blogs(request):
    if request.method == "GET":
        mine = request.GET.get('mine')
        if mine is None:
            queryset = models.Blog.objects.all()
        else:
            queryset = models.Blog.objects.filter(publisher_profile__user=request.user)
        paginator = pagination.CustomPagination()
        blogs = paginator.paginate_queryset(queryset, request)
        serialized_blogs = BlogSnippetSerializer(
            instance=blogs, many=True, context={'user': request.user}).data
        return JsonResponse(create_response(data=serialized_blogs, paginator=paginator), safe=False)
    elif request.method == "PUT":
        body = request.data
        file = body['header_image']
        ext = file.name.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)

        title = body['title']
        content = body['content']
        snippet = content[:130] + '...'
        publisher_profile = Profile.objects.get(user=request.user)

        blog = Blog(title=title, snippet=snippet, content=content, publisher_profile=publisher_profile)
        blog.header_image.save(filename, file, save=True)
        blog.save()
        return JsonResponse(create_response(data=None), safe=False)
    elif request.method == "POST":
        body = request.data
        blog = Blog.objects.get(pk=body['blog_id'], publisher_profile__user=request.user)
        if 'title' in body:
            blog.title = body['title']
        if 'content' in body:
            blog.content = body['content']
            blog.snippet = body['content'][:130] + '...'
        if 'header_image' in body:
            file = body['header_image']
            ext = file.name.split('.')[-1]
            filename = "%s.%s" % (uuid.uuid4(), ext)
            blog.header_image.save(filename, file, save=True)
        blog.update_date = datetime.now()
        blog.save()
        return JsonResponse(create_response(data=None), safe=False)
    elif request.method == "DELETE":
        body = request.data
        blog = Blog.objects.get(pk=body['blog_id'], publisher_profile__user=request.user)
        blog.delete()
        return JsonResponse(create_response(data=None), safe=False)


@csrf_exempt
@api_view(["GET"])
def blog(request, blog_pk):
    try:
        blog = models.Blog.objects.get(pk=blog_pk)
    except:
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.blog_couldnt_found), safe=False)
    return JsonResponse(create_response(BlogSerializer(instance=blog, many=False, context={'user': request.user}).data), safe=False)


@csrf_exempt
@api_view(["POST"])
def upvote(request, blog_pk):
    body = request.data
    if 'recaptcha_token' in body and utils.verify_recaptcha(None, body['recaptcha_token'], 'blog_stats') == ResponseCodes.verify_recaptcha_failed:
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.verify_recaptcha_failed), safe=False)

    try:
        blog = models.Blog.objects.get(pk=blog_pk)
        vote = models.Vote.objects.filter(user=request.user, blog=blog)
        if len(vote) == 0:
            vote = models.Vote(user=request.user, blog=blog, vote_type=True)
        else:
            vote = vote[0]
            vote.vote_type = True
        vote.save()
        return JsonResponse(create_response(data=BlogSnippetSerializer(instance=blog, many=False, context={'user': request.user}).data), safe=False)
    except Exception as e:
        log(e, 'e')
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.blog_couldnt_found), safe=False)


@csrf_exempt
@api_view(["POST"])
def downvote(request, blog_pk):
    body = request.data
    if 'recaptcha_token' in body and utils.verify_recaptcha(None, body['recaptcha_token'], 'blog_stats') == ResponseCodes.verify_recaptcha_failed:
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.verify_recaptcha_failed), safe=False)

    try:
        blog = models.Blog.objects.get(pk=blog_pk)
        vote = models.Vote.objects.filter(user=request.user, blog=blog)
        if len(vote) == 0:
            vote = models.Vote(user=request.user, blog=blog, vote_type=False)
        else:
            vote = vote[0]
            vote.vote_type = False
        vote.save()
        return JsonResponse(create_response(data=BlogSnippetSerializer(instance=blog, many=False, context={'user': request.user}).data), safe=False)
    except Exception as e:
        log(e, 'e')
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.blog_couldnt_found), safe=False)


@csrf_exempt
@api_view(["POST"])
def view(request, blog_pk):
    body = request.data
    if 'recaptcha_token' in body and utils.verify_recaptcha(None, body['recaptcha_token'], 'blog_stats') == ResponseCodes.verify_recaptcha_failed:
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.verify_recaptcha_failed), safe=False)

    try:
        blog = models.Blog.objects.get(pk=blog_pk)
        blog.view_count = blog.view_count+1
        blog.save()
        return JsonResponse(create_response(data=None), safe=False)
    except:
        return JsonResponse(create_response(data=None, success=False, error_code=ResponseCodes.blog_couldnt_found), safe=False)
