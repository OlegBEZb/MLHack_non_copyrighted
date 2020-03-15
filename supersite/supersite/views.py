from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from django.http import JsonResponse
import shutil
import time
import os

def main(request):
	response_data = {}
	if request.POST.get('action') == 'post':
		text = request.POST.get('text')
		# text - это строка которую считали с формы
		response_data['text'] = text
		print(text)

		time.sleep(4)
		# сюда добавить функцию, которая создает картинку и сохраняет ее в
		# static/img/
		print(os.getcwd())
		shutil.copy('/home/vlad/111.jpeg', dst='supersite/static/img/photo_1.jpeg')

		# Сейчас сайт работает с изображением static/img/photo_1.jpeg

		return JsonResponse(response_data)

	return render(request, 'main.html')
