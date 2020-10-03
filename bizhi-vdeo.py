import win32gui
# 遍历所有窗口，关闭Pogman前面的WokerW窗口，否则会遮挡被嵌入的窗口
tmpHwnd = None

def EnumWindowsProc(hwnd,lParam):
    global tmpHwnd
    className = win32gui.GetClassName(hwnd)
    if className == "WorkerW":
        SHELLDLL_DefView = win32gui.FindWindowEx(hwnd,0,"SHELLDLL_DefView",None)
        if SHELLDLL_DefView == 0:
            tmpHwnd = hwnd
    if className == "Progman":
        win32gui.SendMessage(tmpHwnd, 16, 0, 0)

# 嵌入到桌面
def embed(programName):

    desk = win32gui.FindWindow("Progman","Program Manager")
    background = win32gui.FindWindowEx(desk,0,"SHELLDLL_DefView",None)


    program = win32gui.FindWindow(None,programName)
    #pyqt5 QWidget.winId()获得program

    win32gui.SendMessage(desk, 0x052c, 0, 0)
    win32gui.EnumWindows(EnumWindowsProc,0)
    win32gui.SetParent(program,desk)



embed("微信")





 
