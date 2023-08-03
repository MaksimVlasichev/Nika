
import win32gui
import win32api
import time

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


    now_active = win32gui.GetWindowText(win32gui.GetForegroundWindow())
def getWindow(name:str):
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    print(top_windows)
    for i in top_windows:
        if name in i[1]:
            return i[0]
        elif len(top_windows)-1 == top_windows.index(i):
            
            return "Окно не запущено"
def top_wind(code: int):
    print(code)
    print(type(code))
    # win32gui.ShowWindow(code, 4)
    win32gui.SetForegroundWindow(int(code))
    return 1

temp = ""
main = ""
# for i in top_windows:
#     if now_active in i[1]:
#         main = i[0]
#     if "Discord" in i[1]:
#         temp = i[0]
#         print(i[0], i[1])
print(main)
print("-----------------------------------d------")
# print(top_windows)
# print(win32gui.EnumWindows(windowEnumerationHandler, top_windows))
print(win32api.EnumDisplayMonitors())
# print(win32api.GetMonitorInfo(temp))
# win32gui.MoveWindow(461306,2048, 432, 1920,1080,False)
# win32gui.SetForegroundWindow(temp)
# time.sleep(1)
# win32gui.MoveWindow(temp, 1, 200, 512, 432,True )
# win32gui.MoveWindow(temp, 1463, 200, 512, 432,True )
# win32gui.SetForegroundWindow(temp)
# win32gui.window
# win32gui.ShowWindow(main, 1)
# win32gui.ShowWindow(temp, 3)
# win32gui.SetActiveWindow(temp)
# win32gui.SetForegroundWindow(temp)

