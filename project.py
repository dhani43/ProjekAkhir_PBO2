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
## Class BankData
###########################################################################

class BankData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 753,380 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		bSizer161.SetMinSize( wx.Size( 100,-1 ) )
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( -1,40 ) )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"1234.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer24.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Welcome, User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer24.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		fgSizer2.Add( bSizer24, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )


		fgSizer2.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer21.Add( fgSizer2, 0, wx.ALL, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer27.Add( self.m_panel11, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer23.Add( bSizer27, 0, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )


		bSizer23.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self.m_panel2, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer28, 0, wx.EXPAND, 5 )


		bSizer21.Add( bSizer23, 1, wx.EXPAND, 5 )


		bSizer20.Add( bSizer21, 1, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer20 )
		self.m_panel2.Layout()
		bSizer20.Fit( self.m_panel2 )
		bSizer161.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer1.Add( bSizer161, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Data Bank Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 17, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer18.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Cari berdasarkan nama:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer18.Add( bSizer3, 1, wx.ALIGN_RIGHT, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer15.Add( self.m_listCtrl2, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.Add = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.Add, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer18.Add( bSizer4, 1, wx.EXPAND, 5 )


		fgSizer1.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnClickButtonLogout )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClickButtonCari )
		self.Add.Bind( wx.EVT_BUTTON, self.addItemBtn )
		self.m_button2.Bind( wx.EVT_BUTTON, self.deleteItemBtn )
		self.m_button3.Bind( wx.EVT_BUTTON, self.refreshItemBtn )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnClickButtonExit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClickButtonLogout( self, event ):
		event.Skip()

	def OnClickButtonCari( self, event ):
		event.Skip()

	def addItemBtn( self, event ):
		event.Skip()

	def deleteItemBtn( self, event ):
		event.Skip()

	def refreshItemBtn( self, event ):
		event.Skip()

	def OnClickButtonExit( self, event ):
		event.Skip()


###########################################################################
## Class Add_item
###########################################################################

class Add_item ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 397,317 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"INPUT DATA BANK SAMPAH", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer7.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer2 = wx.GridSizer( 0, 2, 0, 100 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Nama Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer2.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.namaSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer2.Add( self.namaSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer9.Add( gSizer2, 0, wx.EXPAND, 5 )


		bSizer5.Add( bSizer9, 1, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer4 = wx.GridSizer( 0, 2, 0, 100 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Harga Kiloan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer4.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hargaSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer4.Add( self.hargaSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer10.Add( gSizer4, 1, 0, 5 )


		bSizer5.Add( bSizer10, 1, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer5 = wx.GridSizer( 0, 2, 0, 100 )

		self.jenisSampahtxt = wx.StaticText( self, wx.ID_ANY, u"Jenis Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenisSampahtxt.Wrap( -1 )

		gSizer5.Add( self.jenisSampahtxt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jenisSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer5.Add( self.jenisSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer11.Add( gSizer5, 1, 0, 5 )


		bSizer5.Add( bSizer11, 1, wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer6 = wx.GridSizer( 0, 2, 0, 100 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Berat Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer6.Add( self.m_staticText6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.beratSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer6.Add( self.beratSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer12.Add( gSizer6, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer12, 1, 0, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer7 = wx.GridSizer( 0, 2, 0, 100 )

		self.Kondisitxt = wx.StaticText( self, wx.ID_ANY, u"Kondisi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Kondisitxt.Wrap( -1 )

		gSizer7.Add( self.Kondisitxt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kondisi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer7.Add( self.kondisi, 0, wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( gSizer7, 1, 0, 5 )


		bSizer5.Add( bSizer13, 1, wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button5, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer14, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer5.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.saveItemBtn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def saveItemBtn( self, event ):
		event.Skip()


###########################################################################
## Class Edit_item
###########################################################################

class Edit_item ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 397,317 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"INPUT DATA BANK SAMPAH", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer7.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer2 = wx.GridSizer( 0, 2, 0, 100 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Nama Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer2.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.namaSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer2.Add( self.namaSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer9.Add( gSizer2, 0, wx.EXPAND, 5 )


		bSizer5.Add( bSizer9, 1, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer4 = wx.GridSizer( 0, 2, 0, 100 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Harga Kiloan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer4.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hargaSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer4.Add( self.hargaSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer10.Add( gSizer4, 1, 0, 5 )


		bSizer5.Add( bSizer10, 1, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer5 = wx.GridSizer( 0, 2, 0, 100 )

		self.jenisSampahtxt = wx.StaticText( self, wx.ID_ANY, u"Jenis Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenisSampahtxt.Wrap( -1 )

		gSizer5.Add( self.jenisSampahtxt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jenisSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer5.Add( self.jenisSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer11.Add( gSizer5, 1, 0, 5 )


		bSizer5.Add( bSizer11, 1, wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer6 = wx.GridSizer( 0, 2, 0, 100 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Berat Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer6.Add( self.m_staticText6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.beratSampah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer6.Add( self.beratSampah, 0, wx.ALIGN_RIGHT, 5 )


		bSizer12.Add( gSizer6, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer12, 1, 0, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer7 = wx.GridSizer( 0, 2, 0, 100 )

		self.Kondisitxt = wx.StaticText( self, wx.ID_ANY, u"Kondisi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Kondisitxt.Wrap( -1 )

		gSizer7.Add( self.Kondisitxt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kondisi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer7.Add( self.kondisi, 0, wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( gSizer7, 1, 0, 5 )


		bSizer5.Add( bSizer13, 1, wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button5, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer14, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer5.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.saveItemBtn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def saveItemBtn( self, event ):
		event.Skip()


###########################################################################
## Class Home
###########################################################################

class Home ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 612,323 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( -1,40 ) )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"1234.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Welcome, User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer24.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		fgSizer2.Add( bSizer24, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )


		fgSizer2.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer21.Add( fgSizer2, 0, wx.ALL, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer27.Add( self.m_panel11, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer23.Add( bSizer27, 0, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self.m_panel2, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer28, 1, wx.EXPAND, 5 )


		bSizer21.Add( bSizer23, 1, wx.EXPAND, 5 )


		bSizer20.Add( bSizer21, 1, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer20 )
		self.m_panel2.Layout()
		bSizer20.Fit( self.m_panel2 )
		bSizer161.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer1.Add( bSizer161, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 17, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer18.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus. Semper feugiat nibh sed pulvinar proin gravida hendrerit lectus a. Sapien eget mi proin sed libero. Tempor nec feugiat nisl pretium fusce id. Ut faucibus pulvinar elementum integer enim. Convallis posuere morbi leo urna molestie at elementum. Tincidunt augue interdum velit euismod in. Est sit amet facilisis magna etiam tempor. Egestas tellus rutrum tellus pellentesque. Arcu non sodales neque sodales ut etiam. Mauris a diam maecenas sed enim ut sem. Et malesuada fames ac turpis egestas maecenas pharetra. Faucibus ornare suspendisse sed nisi lacus sed viverra.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetMinSize( wx.Size( -1,200 ) )

		bSizer3.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer18.Add( bSizer3, 1, wx.ALIGN_RIGHT, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Data Bank Sampah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizer16, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer18.Add( bSizer4, 1, wx.EXPAND, 5 )


		fgSizer1.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnClickButtonLogout )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnClickButtonDataBank )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClickButtonLogout( self, event ):
		event.Skip()

	def OnClickButtonDataBank( self, event ):
		event.Skip()


