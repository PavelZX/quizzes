from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import QuizSerializer, MatterSerializer
from .models import Quiz, Author, Matter
from rest_framework import status
import json
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def welcome(request):
  content = { 'message': 'Welcome interview App!' }
  return JsonResponse(content, status=200)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_quizzes(request):
  user = request.user.id
  quizzes = Quiz.objects.filter(added_by=user)
  serializer = QuizSerializer(quizzes, many=True)
  return JsonResponse({'quizzes': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_quiz(request):
  payload = json.loads(request.body)
  user = request.user
  author = Author.objects.get(id=payload["author"])
  quiz = Quiz.objects.create(
    title = payload["title"],
    description = payload["description"],
    added_by = user,
    author = author
  )
  serializer = QuizSerializer(quiz)
  return JsonResponse({'quizzes': serializer.data}, safe=False, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_quiz(request, quiz_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        quiz_item = Quiz.objects.filter(added_by=user, id=quiz_id)
        # returns 1 or 0
        quiz_item.update(**payload)
        quiz = Quiz.objects.get(id=quiz_id)
        serializer = QuizSerializer(quiz)
        return JsonResponse({'quiz': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_quiz(request, quiz_id):
  user = request.user.id
  try:
    quiz = Quiz.objects.get(added_by=user, id=quiz_id)
    quiz.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_matters(request):
  user = request.user.id
  matters = Matter.objects.filter(added_by=user)
  serializer = MatterSerializer(matters, many=True)
  return JsonResponse({'matters': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_matter(request):
  payload = json.loads(request.body)
  user = request.user
  author = Author.objects.get(id=payload["author"])
  matter = Matter.objects.create(
    title = payload["title"],
    description = payload["description"],
    added_by = user,
    author = author
  )
  serializer = MatterSerializer(matter)
  return JsonResponse({'matters': serializer.data}, safe=False, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_matter(request, matter_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        matter_item = Matter.objects.filter(added_by=user, id=matter_id)
        # returns 1 or 0
        matter_item.update(**payload)
        matter = Matter.objects.get(id=matter_id)
        serializer = MatterSerializer(matter)
        return JsonResponse({'matter': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_matter(request, matter_id):
  user = request.user.id
  try:
    matter = Matter.objects.get(added_by=user, id=matter_id)
    matter.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)