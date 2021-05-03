import os
import sys
import time
import subprocess

import uiautomation as auto

auto.uiautomation.DEBUG_EXIST_DISAPPEAR = False  # set it to False and try again, default is False
auto.uiautomation.DEBUG_SEARCH_TIME = False  # set it to False and try again, default is False
auto.uiautomation.TIME_OUT_SECOND = 10  # global time out
auto.uiautomation.MAX_MOVE_SECOND = .2 # Moves the cursor to the position Default is of 1 second


def openGlobalPass():
    subprocess.Popen('C:\Program Files (x86)\Symantec\VIP Access Client\VIPUIManager.exe')
    time.sleep(0.5)

def getHandle():
    handles = [win.NativeWindowHandle for win in auto.GetRootControl().GetChildren() if win.ClassName == '#32770']
    if len(handles) == 1:
        return handles[0]
    return 0

closeWindow = False
handle = getHandle()
if handle == 0:
    openGlobalPass()
    handle = getHandle()
    closeWindow = True

#Get the current cursor position
curCursorPos = auto.GetCursorPos()

win = auto.ControlFromHandle(handle)
win.SetActive()
win.ButtonControl(AutomationId = '11008').Click()

if closeWindow == True:
    win.Hide(0)

#Move cursor to where it should have been
x,y = curCursorPos
auto.SetCursorPos(x, y)