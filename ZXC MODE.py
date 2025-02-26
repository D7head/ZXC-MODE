import pyautogui
import time
import keyboard
import threading

running = False
current_value = 1000
step = 7

def calculate_and_type():
    global running, current_value
    while running:
        try:
            pyautogui.press('enter') 
            pyautogui.write(str(current_value))
            pyautogui.press('enter')  
            
            current_value -= step
            time.sleep(0.1)
        except pyautogui.FailSafeException:
            print("Программа прервана пользователем.")
            running = False
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            running = False
            break

def toggle_running():
    global running, current_value
    running = not running
    if running:
        print("Программа запущена.")
        threading.Thread(target=calculate_and_type).start()
    else:
        print("Программа остановлена.")
        current_value = 1000  

def main():
    keyboard.add_hotkey('f9', toggle_running)
    try:
        keyboard.wait()
    except Exception as e:
        print(f"Произошла ошибка при запуске: {e}")


if __name__ == "__main__":
    main()