from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import random

students = ['Мийманов Абдуллах',
            'Каныбеков Абдурахим',
            'Жетимишова Нурпери',
            'Мундузов Кубатбек',
            'Тойчуваева Мээрим',
            'Уланбек к Аделина',
            'Мамадраимов Нурболсун'
]


class FirstAPI(APIView):
    def get(self, request):
        return Response({f'student': {random.choice(students)}})

