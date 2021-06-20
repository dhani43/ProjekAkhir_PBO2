from controller import MyGui
from database import Database
import wx
import noname
import project
from daftarFrame import daftarFrame

class loginFrame( noname.login ):
	def __init__( self, parent=None ):
		noname.login.__init__( self, parent=None )
		self.db = Database()
		

	def cek(self):
		self.username = self.textUsername.GetValue().lower()
		self.password = self.textPassword.GetValue()

	def btnLogin( self, event ):
		self.cek()
		self.db.query("SELECT nama, password FROM users WHERE nama=? and password=?", (self.username, self.password))
		self.dataUser = self.db.resultOne()
		try:
			if self.username == "" or self.password == "":
				wx.MessageBox("Username atau Password tidak boleh kosong")
			elif self.dataUser != None:
				wx.MessageBox("Login Berhasil")
				self.Close()
				frame = MyGui(parent=None)
				frame.Show()
			else:
				wx.MessageBox("Login Gagal")
		except:
			wx.MessageBox("Login Gagal")
		
	def btnDaftar( self, event ):
		frame = daftarFrame(parent=None)
		frame.Show()
		self.Destroy()

