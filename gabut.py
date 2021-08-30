#import ini dulu di cmd
import pyautogui, time, emoji, pyperclip
#perkiraan waktu delay (10 detik)
time.sleep(10)
#teks yang mau di kirim + emot
text = "I Love You 3.000" + emoji.emojize(":red_heart:")
pyperclip.copy(text)
#berapa banyak teksnya ?
for i in range(10):
#copas otomatis    
    pyautogui.hotkey("ctrl", "v")
#kirim otomatis    
    pyautogui.press("enter")
    
    pyautogui.typewrite("Aku Bosan")
    pyautogui.press("enter")
