import os
from secrets import token_hex
from PIL import Image
                        #Pillow - популярная библиотека для обработки изображений: открытие, создание, редактирование,
                        # сохранение и конвертация изображений.
from flask import url_for, current_app

def save_picture(form_picture):
    """код функции, которая обеспечивает изменение аватарки пользователя."""
    random_hex = token_hex(8)
    # случайное 16 значное число в 16-ти значной системе, чтобы избежать конфликта имён картинок (8 байт)
    _, f_ext = os.path.splitext(form_picture.filename) # получаем расширение файла, имя в мусор
    picture_fn = random_hex + f_ext # create a new unique file name
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn) # create a path

    output_size = (150, 150) # Задаётся кортеж с размерами - ширина и высота в пикселях.
    i = Image.open(form_picture) # Используется библиотека Pillow (PIL) для работы с изображениями.
                                # В переменную i сохраняется объект изображения.
    i.thumbnail(output_size)    # Метод thumbnail() изменяет размер изображения пропорционально,
                                # чтобы оно вписалось в указанные размеры (150x150).
                                # Если исходное изображение меньше 150x150, оно останется без изменений.
    i.save(picture_path)        # Сохраняет изменённое изображение в файл по пути picture_path.

    return picture_fn
