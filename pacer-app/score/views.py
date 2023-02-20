from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Score

class ScoreView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            input = int(request.query_params["input"])
            score = input + 1
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            Score.objects.create(
                input=input,
                score=score,
            )
        except:
            pass

        return Response({ "score": score }, status=status.HTTP_200_OK)