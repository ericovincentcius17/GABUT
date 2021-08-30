#import ini dulu di cmd
import pyautogui, time, emoji, pyperclip
#perkiraan waktu delay (10 detik)
time.sleep(10)
#teks yang mau di kirim + emot
text = "Happy Birthday Maria Oksana Vedorova" + emoji.emojize(":birthday_cake:")
pyperclip.copy(text)
#berapa banyak teksnya ?
for i in range(3000):
#copas otomatis    
    pyautogui.hotkey("ctrl", "v")
#kirim otomatis    
    pyautogui.press("enter")