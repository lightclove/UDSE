# -*- coding: utf-8 -*-

from pprint import pprint

from dpa.client.XMLRPCProxy import XMLRPCProxy

import json

from PyQt4 import QtCore, QtGui

import sys

import set_tko_ui, dialog1

import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class DialogEditClass(QtGui.QDialog, dialog1.Ui_Dialog):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def get_sn(self):
        item_sn = self.lineEdit_sn.text()
        return item_sn


class SetTkoUi(QtGui.QMainWindow, set_tko_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        settings = QtCore.QSettings('MyTestSettings', 'MyTestApp')
        # self.menu_actions()
        self.ReadBtn.clicked.connect(self.tree_view)
        self.DelBtn.clicked.connect(self.table_del)
        self.InsUpBtn.clicked.connect(self.table_ins_upd)
        self.tableWidget.customContextMenuRequested.connect(self.tableMenu)
        # self.treeWidget.customContextMenuRequested.connect(self.treeMenu)
        self.table_view()
        self.tree_view()

    def SelectRow(self, QTableWidgetItem):
        item_sn = self.tableWidget.item(QTableWidgetItem.row(), 0).text()
        item_type = self.tableWidget.item(QTableWidgetItem.row(), 1).text()
        item_name = self.tableWidget.item(QTableWidgetItem.row(), 2).text()
        item_blocks = self.tableWidget.item(QTableWidgetItem.row(), 3).text()
        item_interfaces = self.tableWidget.item(QTableWidgetItem.row(), 4).text()
        item_list = [str(item_sn), str(item_type), str(item_name), str(item_blocks), str(item_interfaces)]
        self.lineEdit_sn.setText(item_sn)
        self.lineEdit_type.setText(item_type)
        self.lineEdit_name.setText(item_name)
        self.lineEdit_blocks.setText(item_blocks)
        self.lineEdit_interfaces.setText(item_interfaces)
        self.dialog_edit(item_list)

    def dialog_edit(self, item_list=[]):
        if len(item_list) > 0:
            dialog = DialogEditClass()
            dialog.lineEdit_sn.setText(item_list[0])
            dialog.lineEdit_type.setText(item_list[1])
            dialog.lineEdit_name.setText(item_list[2])
            dialog.lineEdit_blocks.setText(item_list[3])
            dialog.lineEdit_interfaces.setText(item_list[4])
            dialog.exec_()
            # dialog.show()
        else:
            dialog = DialogEditClass()
            dialog.show()

        #    def dialog_edit(self):
        #        dialog = QtGui.QDialog()
        #        dialog.resize(300, 300)
        #        dialog.pushButton = QtGui.QPushButton(dialog)
        #        dialog.pushButton.setGeometry(QtCore.QRect(130, 240, 85, 26))
        #        dialog.pushButton.setObjectName(_fromUtf8("pushButton"))
        #        dialog.pushButton.setText(_translate("dialog", "Сохранить", None))
        #        dialog.setWindowTitle(_translate("dialog", "Изменить", None))
        #        dialog.exec_()

    def tableMenu(self, position):
        menu = QtGui.QMenu()
        # menu.addAction(self.AddAction)
        menu.addAction(self.EditAction)
        # menu.addAction(self.DelAction)
        menu.exec_(self.tableWidget.viewport().mapToGlobal(position))

    #    def treeMenu(self, position):
    #        menu = QtGui.QMenu()
    #        menu.addAction(self.AddAction)
    #        menu.addAction(self.EditAction)
    #        menu.addAction(self.DelAction)
    #        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))

    def tree_view(self):
        self.treeWidget.clear()
        all_data = MyServer.read_set_tko('0')
        dict_keys = all_data.keys()
        dict_keys.sort()
        # j_str = all_data[dict_keys[0]]['blocks']
        # print blocks_json[blocks_json.keys()[0]]
        for i, item in enumerate(dict_keys):
            item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
            item_0.setFlags(QtCore.Qt.ItemIsEnabled)
            self.treeWidget.topLevelItem(i).setText(0, _translate("MainWindow", "{}".format(item), None))

            item_1 = QtGui.QTreeWidgetItem(item_0)
            item_1.setFlags(QtCore.Qt.ItemIsEnabled)
            self.treeWidget.topLevelItem(i).child(0).setText(0, _translate("MainWindow", "Тип", None))
            self.treeWidget.topLevelItem(i).child(0).setText(1, _translate("MainWindow",
                                                                           "{}".format(all_data[item]['type']), None))

            item_1 = QtGui.QTreeWidgetItem(item_0)
            item_1.setFlags(QtCore.Qt.ItemIsEnabled)
            self.treeWidget.topLevelItem(i).child(1).setText(0, _translate("MainWindow", "Название", None))
            self.treeWidget.topLevelItem(i).child(1).setText(1, _translate("MainWindow",
                                                                           "{}".format(all_data[item]['name']), None))

            item_1 = QtGui.QTreeWidgetItem(item_0)
            item_1.setFlags(QtCore.Qt.ItemIsEnabled)
            self.treeWidget.topLevelItem(i).child(2).setText(0, _translate("MainWindow", "Блоки", None))

            blocks_json = json.loads(all_data[dict_keys[i]]['blocks'])
            interfaces_json = json.loads(all_data[dict_keys[i]]['interfaces'])

            for ii, bl_item in enumerate(blocks_json.keys()):
                item_2 = QtGui.QTreeWidgetItem(item_1)
                item_2.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(2).child(ii).setText(0, _translate("MainWindow",
                                                                                         "{}".format(bl_item), None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(0).setText(0, _translate("MainWindow", "Тип",
                                                                                                  None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(1).setText(0, _translate("MainWindow",
                                                                                                  "Мин. кол-во", None))
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(1).setText(1, _translate("MainWindow",
                                                                                                  "{}".format(
                                                                                                      blocks_json[
                                                                                                          bl_item][
                                                                                                          "quantity_min"]),
                                                                                                  None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(2).setText(0, _translate("MainWindow",
                                                                                                  "Макс. кол-во", None))
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(2).setText(1, _translate("MainWindow",
                                                                                                  "{}".format(
                                                                                                      blocks_json[
                                                                                                          bl_item][
                                                                                                          "quantity_max"]),
                                                                                                  None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(3).setText(0, _translate("MainWindow", "Слоты",
                                                                                                  None))
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(3).setText(1, _translate("MainWindow",
                                                                                                  "{}".format(
                                                                                                      blocks_json[
                                                                                                          bl_item][
                                                                                                          "slots"]),
                                                                                                  None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(2).child(ii).child(4).setText(0, _translate("MainWindow",
                                                                                                  "Интерфейсы", None))

                for iii, bl_inter_item in enumerate(blocks_json[bl_item]['interfaces'].keys()):
                    item_4 = QtGui.QTreeWidgetItem(item_3)
                    item_4.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.treeWidget.topLevelItem(i).child(2).child(ii).child(4).child(iii).setText(0, _translate(
                        "MainWindow", "{}".format(bl_inter_item), None))

                    item_5 = QtGui.QTreeWidgetItem(item_4)
                    item_5.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.treeWidget.topLevelItem(i).child(2).child(ii).child(4).child(iii).child(0).setText(0,
                                                                                                            _translate(
                                                                                                                "MainWindow",
                                                                                                                "Тип",
                                                                                                                None))

                    item_5 = QtGui.QTreeWidgetItem(item_4)
                    item_5.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.treeWidget.topLevelItem(i).child(2).child(ii).child(4).child(iii).child(1).setText(0,
                                                                                                            _translate(
                                                                                                                "MainWindow",
                                                                                                                "Мин. кол-во",
                                                                                                                None))
                    self.treeWidget.topLevelItem(i).child(2).child(ii).child(4).child(iii).child(1).setText(1,
                                                                                                            _translate(
                                                                                                                "MainWindow",
                                                                                                                "{}".format(
                                                                                                                    blocks_json[
                                                                                                                        bl_item][
                                                                                                                        'interfaces'][
                                                                                                                        bl_inter_item][
                                                                                                                        "quantity_min"]),
                                                                                                                None))

                    item_5 = QtGui.QTreeWidgetItem(item_4)
                    item_5.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.treeWidget.topLevelItem(i).child(2).child(ii).child(4).child(iii).child(2).setText(0,
                                                                                                            _translate(
                                                                                                                "MainWindow",
                                                                                                                "Макс. кол-во",
                                                                                                                None))
                    self.treeWidget.topLevelItem(i).child(2).child(ii).child(4).child(iii).child(2).setText(1,
                                                                                                            _translate(
                                                                                                                "MainWindow",
                                                                                                                "{}".format(
                                                                                                                    blocks_json[
                                                                                                                        bl_item][
                                                                                                                        'interfaces'][
                                                                                                                        bl_inter_item][
                                                                                                                        "quantity_max"]),
                                                                                                                None))

            item_1 = QtGui.QTreeWidgetItem(item_0)
            item_1.setFlags(QtCore.Qt.ItemIsEnabled)
            self.treeWidget.topLevelItem(i).child(3).setText(0, _translate("MainWindow", "Интерфейсы", None))

            for iiii, inter_item in enumerate(interfaces_json.keys()):
                item_2 = QtGui.QTreeWidgetItem(item_1)
                item_2.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(3).child(iiii).setText(0, _translate("MainWindow",
                                                                                           "{}".format(inter_item),
                                                                                           None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(3).child(iiii).child(0).setText(0, _translate("MainWindow", "Тип",
                                                                                                    None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(3).child(iiii).child(1).setText(0, _translate("MainWindow",
                                                                                                    "Мин. кол-во",
                                                                                                    None))
                self.treeWidget.topLevelItem(i).child(3).child(iiii).child(1).setText(1, _translate("MainWindow",
                                                                                                    "{}".format(
                                                                                                        interfaces_json[
                                                                                                            inter_item][
                                                                                                            'quantity_min']),
                                                                                                    None))

                item_3 = QtGui.QTreeWidgetItem(item_2)
                item_3.setFlags(QtCore.Qt.ItemIsEnabled)
                self.treeWidget.topLevelItem(i).child(3).child(iiii).child(2).setText(0, _translate("MainWindow",
                                                                                                    "Макс. кол-во",
                                                                                                    None))
                self.treeWidget.topLevelItem(i).child(3).child(iiii).child(2).setText(1, _translate("MainWindow",
                                                                                                    "{}".format(
                                                                                                        interfaces_json[
                                                                                                            inter_item][
                                                                                                            'quantity_max']),
                                                                                                    None))

    def table_view(self):
        sn_t = self.lineEdit_sn.text()
        if sn_t == '':
            all_data = MyServer.read_set_tko('0')
            dict_keys = all_data.keys()
            dict_keys.sort()
            self.tableWidget.setRowCount(len(all_data))
            # self.tableWidget.setSortingEnabled(True)
            for i, item in enumerate(dict_keys):
                sn = QtGui.QTableWidgetItem(item)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(item))
                self.tableWidget.setItem(i, 0, sn)
            for ii in range(0, len(all_data)):
                var = all_data[dict_keys[ii]]['type']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(ii, 1, sn)
                var = all_data[dict_keys[ii]]['name']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(ii, 2, sn)
                var = all_data[dict_keys[ii]]['blocks']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(ii, 3, sn)
                var = all_data[dict_keys[ii]]['interfaces']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(ii, 4, sn)
        elif sn_t == '0':
            self.tableWidget.setRowCount(0)
            QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None), 'Invalid Serial number')
        else:
            all_data = MyServer.read_set_tko('{}'.format(sn_t))
            if all_data == False:
                self.tableWidget.setRowCount(0)
                QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None), 'Invalid Serial number')

            else:
                self.tableWidget.setRowCount(1)
                sn = QtGui.QTableWidgetItem(sn_t)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(sn_t))
                self.tableWidget.setItem(0, 0, sn)

                var = all_data['type']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(0, 1, sn)
                var = all_data['name']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(0, 2, sn)
                var = all_data['blocks']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(0, 3, sn)
                var = all_data['interfaces']
                sn = QtGui.QTableWidgetItem(var)
                sn.setData(QtCore.Qt.UserRole, QtCore.QVariant(var))
                self.tableWidget.setItem(0, 4, sn)

    def table_del(self):
        DelText = self.lineEdit_sn.text()
        if DelText == '':
            QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None),
                                      'Enter Serial number of item you want to delete')
        else:
            check_data = MyServer.read_set_tko('{}'.format(DelText))
            if check_data == False:
                QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None), 'Wrong Serial number')
                self.lineEdit_sn.clear()
            else:
                reply = QtGui.QMessageBox.question(self, '!?',
                                                   'Are you sure to delete row with sn:{} from date base forever?'.format(
                                                       DelText), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    del_data = MyServer.delete_set_tko('{}'.format(DelText))
                    self.tableWidget.setRowCount(0)
                    self.lineEdit_sn.clear()
                    self.lineEdit_type.clear()
                    self.lineEdit_name.clear()
                    self.lineEdit_blocks.clear()
                    self.lineEdit_interfaces.clear()
                    self.table_view()
                else:
                    pass

    def table_ins_upd(self):
        sn_t = self.lineEdit_sn.text()
        if sn_t == '':
            QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None), 'Enter Serial number')
        else:

            type_t = self.lineEdit_type.text()
            if type_t == '':
                QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None), 'Enter Type value')
            else:

                name_t = self.lineEdit_name.text()
                if name_t == '':
                    QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None), 'Enter Name value')
                else:

                    blocks_t = self.lineEdit_blocks.text()
                    if blocks_t == '':
                        QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None),
                                                  'Enter blocks set (json format only)')
                    else:

                        interfaces_t = self.lineEdit_interfaces.text()
                        if interfaces_t == '':
                            QtGui.QMessageBox.warning(self, _translate("MainWindow", "Ошибка", None),
                                                      'Enter interfaces set (json format only)')
                        else:

                            MyServer.create_set_tko(
                                '{}%{}%{}%{}%{}'.format(sn_t, type_t, name_t, blocks_t, interfaces_t))
                            # MyServer.create_set_tko(['{}'.format(sn_t), '{}'.format(type_t), '{}'.format(name_t), '{}'.format(blocks_t), '{}'.format(interfaces_t)])
                            self.lineEdit_sn.clear()
                            self.lineEdit_type.clear()
                            self.lineEdit_name.clear()
                            self.lineEdit_blocks.clear()
                            self.lineEdit_interfaces.clear()
                            self.table_view()

                        #    def menu_actions(self):
                        #        self.QuitAction.triggered.connect(QtGui.qApp.quit)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, ':(',
                                           'Are you sure to quit?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    form = SetTkoUi()
    form.show()
    app.exec_()


if __name__ == '__main__':
    h = '%s:%s' % ('127.0.0.1', str(12345))
    MyServer = XMLRPCProxy(h, path='/test/')

    main()

    # json1 = json_creator()
    # json2 = json_creator()

    # print MyServer.read_set_tko('sn3')['blocks']
    # print MyServer.create_set_tko(['sn1', 'TEST', 'TEST', json1, json2])
    # MyServer.create_set_tko({'sn':'sn2', 'type':'MMM', 'name':'rwesd', 'blocks':'{'rter':'sdfs'}', 'interfaces':'{'rter':'sdfs'}'})
    # MyServer.create_set_tko('sn3%III%Rmn1%{'sdwfsdf':'sadfas'}%{'ASDfgsdf':'sdfgsdf'}')
    # pprint(MyServer.read_set_tko('0'))
    # print MyServer.delete_set_tko('sn3')
