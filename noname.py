# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class login
###########################################################################

class login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bank Sampah", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer9.SetMinSize( wx.Size( 0,0 ) )
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"loginas.bmp", wx.BITMAP_TYPE_ANY ), wx.Point( 0,0 ), wx.Size( 200,300 ), 0 )
		bSizer9.Add( self.m_bitmap2, 0, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer10.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.textUsername = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer10.Add( self.textUsername, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer10.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.textPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_PASSWORD )
		bSizer10.Add( self.textPassword, 0, wx.ALL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.buttonDaftar = wx.Button( self.m_panel1, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.buttonDaftar, 0, wx.ALL, 5 )

		self.buttonLogin = wx.Button( self.m_panel1, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.buttonLogin, 0, wx.ALL, 5 )


		bSizer10.Add( wSizer1, 1, wx.ALIGN_RIGHT, 5 )


		bSizer9.Add( bSizer10, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel1.SetSizer( bSizer9 )
		self.m_panel1.Layout()
		bSizer9.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonDaftar.Bind( wx.EVT_BUTTON, self.btnDaftar )
		self.buttonLogin.Bind( wx.EVT_BUTTON, self.btnLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnDaftar( self, event ):
		event.Skip()

	def btnLogin( self, event ):
		event.Skip()


###########################################################################
## Class daftar
###########################################################################

class daftar ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bank Sampah", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer9.SetMinSize( wx.Size( 0,0 ) )
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"loginas.bmp", wx.BITMAP_TYPE_ANY ), wx.Point( 0,0 ), wx.Size( 200,300 ), 0 )
		bSizer9.Add( self.m_bitmap2, 0, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer10.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.textEmail = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer10.Add( self.textEmail, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer10.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.textNama = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer10.Add( self.textNama, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer10.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.textPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_PASSWORD )
		bSizer10.Add( self.textPassword, 0, wx.ALL, 5 )

		self.m_staticText511 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Konfirmasi Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		bSizer10.Add( self.m_staticText511, 0, wx.ALL, 5 )

		self.textKonfirmasiPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_PASSWORD )
		bSizer10.Add( self.textKonfirmasiPassword, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer9.Add( bSizer10, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel1.SetSizer( bSizer9 )
		self.m_panel1.Layout()
		bSizer9.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.btnDaftar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnDaftar( self, event ):
		event.Skip()


###########################################################################
## Class test
###########################################################################

class test ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


