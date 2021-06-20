from controller import MyGui
from database import Database
import noname
import wx

class daftarFrame( noname.daftar ):
        def __init__( self, parent=None ):
            noname.daftar.__init__( self, parent=None )
            self.db = Database()

        def setUser(self):
            self.a = self.textEmail.GetValue().lower()
            self.b = self.textNama.GetValue().lower()
            self.c = self.textPassword.GetValue()
            self.d = self.textKonfirmasiPassword.GetValue()

        def btnDaftar( self, event ):
            self.setUser()
            if self.a == "" or self.b == "" or self.c == "" or self.d == "":
                wx.MessageBox("kolom tidak boleh kosong")
            elif self.c != self.d:
                wx.MessageBox("Password dan konfirmasi Password harus sama")
            else:
                val = (self.a, self.b, self.c, self.d)
                sql = "INSERT INTO users ([email], [nama], [password], [konfirmasi password]) VALUES (?, ?, ?, ?)"
                self.db.cursor.execute(sql, val)
                self.db.conn.commit()
                wx.MessageBox("Daftar Berhasil")
                frame = MyGui(parent=None)
                frame.Show()
                self.Destroy()