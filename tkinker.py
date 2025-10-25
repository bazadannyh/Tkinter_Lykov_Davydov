import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        """Настройки графического интерфейса приложения."""
        self.geometry("250x400")
        self.title("2.1 - User Profile GUI - Tkinter")
        self.setUpMainWindow()
        
    def createImageLabels(self):
        """Создаёт метки с изображениями."""
        try:
        # Фон
            bg_image = Image.open("C:/Users/ilya1/Desktop/проекты py/images/skyblue.png")
            bg_image = bg_image.resize((250, 150))  # Подгоняем размер
            bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(self, image=bg_photo)
            bg_label.image = bg_photo
            bg_label.place(x=0, y=0)
            
            # Изображение профиля
            profile_image = Image.open("C:/Users/ilya1/Desktop/проекты py/images/profile_image.png")
            profile_image = profile_image.resize((100, 100))  # Подгоняем размер
            profile_photo = ImageTk.PhotoImage(profile_image)
            profile_label = tk.Label(self, image=profile_photo)
            profile_label.image = profile_photo
            profile_label.place(x=80, y=20)
            
        except:
        # Заглушки если не получилось
            bg_label = tk.Label(self, bg="lightblue", width=35, height=5)
            bg_label.place(x=0, y=0)
            profile_label = tk.Label(self, text="Фото", bg="white", width=15, height=5)
            profile_label.place(x=80, y=20)
    
    def setUpMainWindow(self):
        """Создаёт метки, которые будут отображаться в окне."""
        self.createImageLabels()
        
        # Имя пользователя
        user_label = tk.Label(self, text="Иван Драго", font=("Arial", 14, "bold"))
        user_label.place(x=60, y=140)
        
        # Биография
        bio_label = tk.Label(self, text="Биография", font=("Arial", 12, "bold"))
        bio_label.place(x=15, y=170)
        
        about_label = tk.Label(self, 
                              text="Я инженер-программист с 10-летним опытом создания потрясающего кода.",
                              wraplength=220, justify="left")
        about_label.place(x=15, y=190)
        
        # Умения
        skills_label = tk.Label(self, text="Умения", font=("Arial", 12, "bold"))
        skills_label.place(x=15, y=240)
        
        languages_label = tk.Label(self, text="Python | PHP | SQL | JavaScript")
        languages_label.place(x=15, y=260)
        
        # Опыт работы
        experience_label = tk.Label(self, text="Опыт", font=("Arial", 12, "bold"))
        experience_label.place(x=15, y=290)
        
        developer_label = tk.Label(self, text="Python Разработчик")
        developer_label.place(x=15, y=310)
        
        dev_dates_label = tk.Label(self, text="Март 2011 - настоящее время", font=("Arial", 8))
        dev_dates_label.place(x=15, y=330)
        
        driver_label = tk.Label(self, text="Водитель доставки пиццы")
        driver_label.place(x=15, y=350)
        
        driver_dates_label = tk.Label(self, text="Aug 2015 - Dec 2017", font=("Arial", 8))
        driver_dates_label.place(x=15, y=370)

# Запуск программы
if __name__ == '__main__':
    # Создаем папку images если её нет
    os.makedirs("images", exist_ok=True)
    
    app = MainWindow()
    app.mainloop()