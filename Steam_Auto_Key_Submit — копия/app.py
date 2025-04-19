"""
Главный файл который использует модуль tkinter для управления функций файлов:\n
steamAutenfecation.py в котором есть password.py с паролем от аккаунтов\n
web.py который использует vk.py\n
В которых все функции для работы приложения \n
"""
import tkinter as tk
from web import *
from steamAutenfecation import *
#Создание окна приложения
app = tk.Tk()
app.title('Steam Key Manager')
app.geometry('500x550')
app['bg'] = '#121212'

#Кнопка старта браузеров
start_button= tk.Button(app, text='Start Browsers', command= start_process)
start_button.pack(pady=20)
#Кнопка процесса
process_button = tk.Button(app, text='Process Keys', command= process_keys)
process_button.pack(pady=20)
# Кнопка перезаписи Cookie file
def rewrite_cokie():
    """ Функция которая создает окно в приложении \n
    Для работы с файлом steamAutenfecation"""
    frame = tk.Frame(app, bg='#121212')
    frame.place(relwidth=1, relheight=1)
    title = tk.Label(frame, text='Нажать чтобы перезаписывать COOKIE', bg='#1E1E1E', font=('Themr Ner Year\'s', 15, 'bold'), fg= '#FFFFFF')
    title.place(relwidth=1)
    exit_button21 = tk.Button(frame, text="Start", command=start_process_cok)
    exit_button21.place(relwidth=1)
    exit_button21.pack(pady=15)
    exit_button31 = tk.Button(frame, text="login", command=login)
    exit_button31.place(relwidth=1)
    exit_button31.pack(pady=15)
    exit_button41 = tk.Button(frame, text="Rewrite", command=rewrite)
    exit_button41.place(relwidth=1)
    exit_button41.pack(pady=15)
    exit_button2 = tk.Button(frame, text="Exit", command=frame.destroy)
    exit_button2.place(relwidth=1)
    exit_button2.pack(pady=15)
# перезапись COOKIE
rewrite_cookie = tk.Button(app, text='Rewrite Cookie', command= rewrite_cokie)
rewrite_cookie.pack(pady=30)
#Кнопка выхода
exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.pack(pady=20)

# запускает приложение
app.mainloop()