import time
import threading
import keyboard
import pyautogui

class AutoClicker:
    def __init__(self, button='left', toggle_key='f6', stop_key='esc'):
        
        self.button = button      
        self.toggle_key = toggle_key  
        self.stop_key = stop_key      
        self.clicking = False
        self.running = True
        self.click_thread = None
    
    def clicker_worker(self):
        """Функция, выполняющая клики в отдельном потоке"""
        while self.running == True :
          if self.clicking:
              pyautogui.mouseDown(button=self.button)
          
              
              
              
              
    
    def toggle_clicking(self):
        """Включение/выключение автокликера"""
        self.clicking = not self.clicking
        status = "ВКЛЮЧЕН" if self.clicking else "ВЫКЛЮЧЕН"
        if self.clicking == False :
              pyautogui.mouseUp(button=self.button)
              print("отжал!")
        print(f"Автокликер {status}")
    
    def stop_clicker(self):
        
        print("Остановка автокликера...")
        
        self.running = False
        self.clicking = False

    
    def start(self):
        """Запуск автокликера и прослушивание горячих клавиш"""


        keyboard.add_hotkey(self.toggle_key, self.toggle_clicking)
        keyboard.add_hotkey(self.stop_key, self.stop_clicker)
        
        # Запуск потока с кликами
        self.click_thread = threading.Thread(target=self.clicker_worker)
        self.click_thread.daemon = True
        self.click_thread.start()
        
        print(f"Автокликер запущен")
        print(f"- Нажмите {self.toggle_key.upper()} для включения/выключения кликов")
        print(f"- Нажмите {self.stop_key.upper()} для выхода из программы")
        
        
        keyboard.wait(self.stop_key)
        print("Программа завершена")


if __name__ == "__main__":
    
    clicker = AutoClicker(     
        button='left',       
        toggle_key='f6',     
        stop_key='esc'       
    )
    
    clicker.start()