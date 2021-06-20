import wx
from loginFrame import loginFrame

class MainApp(wx.App):
    def OnInit(self):
        self.frame = loginFrame(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()