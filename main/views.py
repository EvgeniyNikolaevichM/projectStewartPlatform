from django.shortcuts import render, redirect

import  logging
logger = logging.getLogger('TEST_LOGGER_NAME')

def index(request):
    logger.info("Загрузка страницы 'Главная'")
    return render(request, 'main/index.html')

def admin(request):
    logger.info("Загрузка страницы 'Админ'")
    return redirect('admin')