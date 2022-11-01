import json
import os

import asn1tools
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListView, QAbstractItemView
import MainWindow
import asn_test

asn1 = asn_test.ASN1()
qList = []
selectedItem = 0


def showAlert(content):
    msg_box = QMessageBox(QMessageBox.Critical, '错误！', content)
    msg_box.exec_()


def reset_edt():
    ui.edtASN1.clear()
    ui.edtASN1.setText(
        "Struct DEFINITIONS ::= BEGIN\n\n\nQuestion ::= SEQUENCE {\n        id        INTEGER,\n        question  IA5String\n    }\n\n    Answer ::= SEQUENCE {\n        id        INTEGER,\n        answer    BOOLEAN\n    }\n\n\nEND")
    ui.edtCode.clear()
    ui.edtOpt.clear()
    ui.edtRes.clear()


def compile_ASN1():
    code_X = ui.cbBox.currentText()
    code_X = code_X.lower()

    if ui.btnOpenASN.text() == "Open ASN1 Library":
        ff = ui.edtASN1.toPlainText()
        # print(ff)
        save_to_file('cache.asn', ff)

        try:
            asn1.compile("cache.asn", code_X)
        except Exception as e:
            showAlert('ASN.1结构体编译错误！\n请检查输入的结构体格式！')
            ui.edtRes.setText('Error Info: ' + e.args[0])
        else:
            main_key = asn1.get_mainName()
            ui.edtRes.setText(main_key + " is compiled successfully!")
    else:
        print(qList[selectedItem])

        f = open(qList[selectedItem], encoding='utf-8')
        data = ""
        for line in f:
            data = data + line
        f.close()

        if data.find("BEGIN") == -1:
            data = "Struct DEFINITIONS ::= BEGIN\n" + data + "\nEND"

        save_to_file('cache.asn', data)

        try:
            asn1.compile('cache.asn', code_X)
        except Exception as e:
            showAlert('ASN.1结构体编译错误！\n请检查输入的结构体格式！')
            ui.edtRes.setText('Error Info: ' + str(e.args))
        else:
            main_key = asn1.get_mainName()
            ui.edtRes.setText(main_key + " is compiled successfully!")


def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()


def change_EnCode():
    ui.btnCode.setText("Encode")
    ui.edtCode.clear()


def change_DeCode():
    ui.btnCode.setText("Decode")
    ui.edtCode.clear()


def clickedlist(qModelIndex):
    global selectedItem
    selectedItem = qModelIndex.row()
    print("点击的是：" + str(qModelIndex.row()))


def doubleClicked():
    change_ASN_Lib()
    print(qList[selectedItem])

    f = open(qList[selectedItem], encoding='utf-8')
    data = ""
    for line in f:
        data = data + line
    f.close()

    if data.find("BEGIN") == -1 and (
            data.find("SEQUENCE") != -1 or data.find("OPTIONAL") != -1 or data.find("ENUMERATED") != -1 or
            data.find("INTEGER") != -1 or data.find("BOOLEAN") != -1):
        data = "Struct DEFINITIONS ::= BEGIN\n" + data + "\nEND"
    ui.edtASN1.clear()
    ui.edtASN1.setText(data)


def get_files(path):
    global qList
    qList = []
    for file_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            # print(os.path.join(file_path, file_name))
            qList.append(os.path.join(file_path, file_name))


def change_ASN_Lib():
    global qList
    if ui.btnOpenASN.text() == "Open ASN1 Library":
        ui.btnOpenASN.setText("Close ASN1 Library")

        ui.edtASN1.setGeometry(50, 50, 20, 20)
        ui.gridLayout.removeWidget(ui.edtASN1)

        ui.btnReset.setDisabled(True)

        # 添加 list view
        ui.listView = QListView()
        ui.gridLayout.addWidget(ui.listView, 1, 0, 1, 5)
        slm = QStringListModel()  # 创建mode

        # qList = ['Item 1', 'D:\\PyProject\\asn_decode\\asn_dir\\test.asn', 'Item 3', 'Item 4']  # 添加的数组数据
        get_files("./asn_dir/")

        slm.setStringList(qList)  # 将数据设置到model
        ui.listView.setModel(slm)  # 绑定 listView 和 model
        ui.listView.clicked.connect(clickedlist)  # listview 的点击事件
        ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ui.listView.doubleClicked.connect(doubleClicked)

    else:
        ui.btnOpenASN.setText("Open ASN1 Library")

        ui.listView.setGeometry(50, 50, 20, 20)
        ui.gridLayout.removeWidget(ui.listView)

        ui.btnReset.setEnabled(True)

        # 恢复 edtASN
        ui.edtASN1 = QtWidgets.QTextEdit()
        ui.gridLayout.addWidget(ui.edtASN1, 1, 0, 1, 5)
        reset_edt()


def format_Output(re):
    re = str(re)

    return re


def print_hist(h, strs, cnt):
    # global strs
    # print('{')
    for i in range(cnt):
        strs = strs + '\t'
    strs = strs + '{\n'
    for key in h.keys():  # 当前迭代的字典
        data = h[key]  # 当前key所对应的value赋给data

        if isinstance(data, dict):  # 如果data是一个字典，就递归遍历
            for i in range(cnt):
                strs = strs + '\t'
            strs = strs + "\t'" + str(key) + "': "
            strs = print_hist(data, strs, cnt + 1)

        if not isinstance(data, dict):
            for i in range(cnt + 1):
                strs = strs + '\t'
            if isinstance(data, str):
                strs = strs + "'" + str(key) + "': '" + str(data) + "',\n"
            else:
                strs = strs + "'" + str(key) + "': " + str(data) + ',\n'
            # print(key, data)
    # print('}')
    for i in range(cnt):
        strs = strs + '\t'
    strs = strs + '}\n'
    return strs


def Start_Code():
    txt = ui.edtCode.toPlainText()

    if txt != '':
        txt = txt.replace('\'', "\"").replace("\n", "")

        if ui.rbtDecode.isChecked():
            try:
                re = asn1.decode(txt)  # 解出来是 dict
            except Exception as e:
                showAlert('编码解析错误！\n请检查输入的编码！')
                ui.edtRes.setText('Error Info: ' + str(e.args))
            else:
                # 格式化输出
                strs = ''
                strs = print_hist(re, strs, 0)
                ui.edtOpt.setText(strs)
        else:
            try:
                re = asn1.encode(asn1.get_mainName(), txt)
            except Exception as e:
                showAlert('加密失败！\n请检查输入的数据！')
                ui.edtRes.setText('Error Info: ' + e.args[0])
            else:
                ui.edtOpt.setText(re)


def Init(ui):
    ui.edtASN1.setText(
        "Struct DEFINITIONS ::= BEGIN\n\n\nQuestion ::= SEQUENCE {\n        id        INTEGER,\n        question  IA5String\n    }\n\n    Answer ::= SEQUENCE {\n        id        INTEGER,\n        answer    BOOLEAN\n    }\n\n\nEND")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    mw.setWindowIcon(QIcon('asn1.ico'))
    ui = MainWindow.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()

    Init(ui)

    # click event
    ui.btnReset.clicked.connect(reset_edt)
    ui.btnComp.clicked.connect(compile_ASN1)
    ui.rbtEncode.clicked.connect(change_EnCode)
    ui.rbtDecode.clicked.connect(change_DeCode)
    ui.btnCode.clicked.connect(Start_Code)
    ui.btnOpenASN.clicked.connect(change_ASN_Lib)

    sys.exit(app.exec_())
