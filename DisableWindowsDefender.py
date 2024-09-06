import pyautogui
import pyperclip
import time
from ctypes import windll



#Enters the CMD
def OpenCMD():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    pyautogui.hotkey('win', 'r')
    pyperclip.copy("cmd")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    



def EnterPowershell():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    
    time.sleep(0.3)
    
    pyperclip.copy("cd %SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\")
    time.sleep(0.2)
    
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('enter')
    
    
    
    
    

    
def OpenPowershellAsAdministrator():
    time.sleep(0.2)
    pyperclip.copy("powershell.exe Start-Process powershell -Verb RunAs")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    
    time.sleep(1)
    
    pyautogui.click(1060, 690)
    
    pyautogui.press('enter')
    
OpenCMD()
EnterPowershell()
OpenPowershellAsAdministrator()
