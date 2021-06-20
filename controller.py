from os import error
import wx
import project
import sqlite3, os
import pathlib
from wx.core import NotifyEvent
from os import SEEK_CUR
from database1 import Database
import loginFrame

connection = None

try:
    connection = sqlite3.connect(os.path.abspath('banksampah.db'))

except Exception as err:
    print(err)

class BaseModel:
    def __init__(self):
        self._connection = connection

    def _convertValueToSqlValue(self, values):
        convertedVals = []
        for value in values:
            if not isinstance(value, str):
                value = str(value)
            convertedVals.append(value)

        joined = '", "'.join(convertedVals)
        return f'("{joined}")'

    def insert(self, values, columns=[]):
        columns_query = '' if len(columns) < 1 else f'({", ".join(columns)})'

        # check if nested values [[1,2,3,4,5], [2,3,4,5,6,7,8]]
        values_query = []
        if any(isinstance(v, list) for v in values):
            for value in values:
                values_query.append(self._convertValueToSqlValue(value))
            values_query = ', '.join()
        else:
            values_query = self._convertValueToSqlValue(values)

        query = f'INSERT INTO {self.table}{columns_query} VALUES {values_query}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.rowcount > 0
        self._connection.commit()

        return result

    def update(self, colValues, identifierValue, identifierColumn='id'):
        result = False

        update_query = []
        for key in colValues:
            update_query.append(f'{key} = "{colValues[key]}"')

        update_query = ', '.join(update_query)
        query = f'UPDATE {self.table} SET {update_query} WHERE {identifierColumn} = {identifierValue}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.rowcount > 0
        self._connection.commit()

        return result

    def delete(self, value, column='id'):
        result = False
        query = f'DELETE FROM {self.table} WHERE {column} = {value}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.rowcount > 0
        self._connection.commit()

        return result

    def find(self, value, column='id'):
        result = False
        query = f'SELECT * FROM {self.table} WHERE {column} = {value}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        return result

    def get(self, columns='*', orderByColumn=None, orderByDirection='ASC', limit=10):
        result = []
        selectColumns = ', '.join(columns) if isinstance(columns, list) else '*'

        if orderByColumn is not None:
            orders_query = f'ORDER BY {orderByColumn} {orderByDirection}'

        query = f'SELECT {columns} FROM {self.table} {orders_query} LIMIT {limit}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result

class databank(BaseModel):
    table = 'bank'

#data Controller


#add item controller


wxframe2 = project.Add_item
class MyGui2(wxframe2):
    def __init__(self, parent):
        project.Add_item.__init__(self, parent=None)
        self.db = Database()
    def setProductName(self, productName):
        self.namaSampah.SetValue(productName)
    def setCategory(self, category):
        self.jenisSampah.SetValue(str(category))
    def setUnitPrice(self, unitPrice):
        self.hargaSampah.SetValue(str(unitPrice))
    def setUnitQuantity(self, UnitQuantity):
        self.beratSampah.SetValue(str(UnitQuantity))
    def setUnitCondition(self, UnitCondition):
        self.kondisi.SetValue(str(UnitCondition))
    def saveItemBtn(self, event):
        product_name = self.namaSampah.GetValue()
        category = self.jenisSampah.GetValue()
        unit_price = self.hargaSampah.GetValue()
        unit_quantity = self.beratSampah.GetValue()
        unit_condition = self.kondisi.GetValue()
        val=(product_name, category, unit_price, unit_quantity, unit_condition)
        try:
            sql = "INSERT INTO bank ([nama_sampah], [jenis_sampah], [harga_sampah], [berat_sampah], [kondisi_sampah]) VALUES (?, ?, ?, ?, ?)"
            self.db.cursor.execute(sql, val)
            self.db.conn.commit()
        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()

        finally:
            wx.MessageDialog(None, 'New Data successfully added.', 'Success',
                                 style=wx.OK | wx.ICON_INFORMATION).ShowModal()


wxframe = project.Home
class MyGui(wxframe) :
    def __init__(self, parent) :
        wxframe.__init__(self, parent)
    
    def OnClickButtonDataBank(self, event):
        self.Close()
        frame1 = MyGui1(None)
        frame1.Show()
    def OnClickButtonLogout(self, event):
        self.Close()
        frame3 = loginFrame.loginFrame(None)
        frame3.Show()

wxframe1 = project.BankData
class MyGui1(wxframe1) :
    def handleSelectedItem(self, event):
        selectedId = event.GetItem().GetText()
        if not selectedId: return
        self.selectedItem = selectedId
        print(selectedId)

    def __init__(self, parent) :
        self.bankModel= databank ()
        wxframe1.__init__(self, parent)
        self.ItemModel=databank()
        self.columns = ['ID','Nama','Harga sampah','Jenis', 'Berat', 'Kondisi', 'Added']
        self.selectedItem = None
        self.initColom()
        self.initData()
        self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedItem)
        selectedItem = None

    def initColom(self):
        for index, col in enumerate(self.columns):
            self.m_listCtrl2.InsertColumn(index, col)

    def initData(self):
            Item = self.ItemModel.get(columns="*",orderByColumn='id_sampah', orderByDirection='DESC')
            for rowIndex, row in enumerate(Item):
                self.m_listCtrl2.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    self.m_listCtrl2.SetItem(rowIndex, columnIndex, str(row[columnIndex]))

    def addItemBtn(self, event):
        frame2 = MyGui2(None)
        frame2.Show()

    def editItemBtn(self, event):
        if self.selectedItem == None: return

        prod = self.bankModel.find(self.selectedItem, column='id_sampah')
        MyGui2.setProductName(prod[1])
        MyGui2.setCategory(prod[2])
        MyGui2.setUnitPrice(prod[3])
        MyGui2.setUnitQuantity(prod[4])
        MyGui2.setUnitCondition(prod[5])
        self.id = self.selectedItem
        self.Show()

    def deleteItemBtn(self, event):
        if self.selectedItem == None: return
        r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure',
                            style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

        if r == wx.ID_YES:
            self.bankModel.delete(value=self.selectedItem, column='id_sampah')
            wx.MessageDialog(None, 'Author has been deleted.', 'Delete Success',
                            style=wx.OK | wx.ICON_INFORMATION).ShowModal()

    def refreshItemBtn(self, event):
        self.m_listCtrl2.DeleteAllItems()
        data = self.bankModel.get(columns="*",orderByColumn='id_sampah', orderByDirection='DESC')
        for rowIndex, row in enumerate(data):
            self.m_listCtrl2.InsertItem(rowIndex, row[0])
            for columnIndex, col in enumerate(self.columns):
                self.m_listCtrl2.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
    
    def OnClickButtonExit(self, event):
        self.Close()
        frame3 = MyGui(None)
        frame3.Show()

    def OnClickButtonLogout(self, event):
        self.Close()
        frame3 = loginFrame.loginFrame(None)
        frame3.Show()









