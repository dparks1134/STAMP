# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metadataTableDlg.ui'
#
# Created: Tue Jun 14 10:46:20 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MetadataTableDlg(object):
    def setupUi(self, MetadataTableDlg):
        MetadataTableDlg.setObjectName(_fromUtf8("MetadataTableDlg"))
        MetadataTableDlg.resize(604, 308)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MetadataTableDlg.setWindowIcon(icon)
        MetadataTableDlg.setFloating(True)
        MetadataTableDlg.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.tbMetadataAddAll = QtGui.QToolButton(self.dockWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/filter_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbMetadataAddAll.setIcon(icon1)
        self.tbMetadataAddAll.setIconSize(QtCore.QSize(24, 24))
        self.tbMetadataAddAll.setObjectName(_fromUtf8("tbMetadataAddAll"))
        self.horizontalLayout_12.addWidget(self.tbMetadataAddAll)
        self.tbMetadataRemoveAll = QtGui.QToolButton(self.dockWidgetContents)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/filter_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbMetadataRemoveAll.setIcon(icon2)
        self.tbMetadataRemoveAll.setIconSize(QtCore.QSize(24, 24))
        self.tbMetadataRemoveAll.setObjectName(_fromUtf8("tbMetadataRemoveAll"))
        self.horizontalLayout_12.addWidget(self.tbMetadataRemoveAll)
        spacerItem = QtGui.QSpacerItem(12, 1, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.label_70 = QtGui.QLabel(self.dockWidgetContents)
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.horizontalLayout_12.addWidget(self.label_70)
        self.cboMetadataAddRemove = QtGui.QComboBox(self.dockWidgetContents)
        self.cboMetadataAddRemove.setObjectName(_fromUtf8("cboMetadataAddRemove"))
        self.cboMetadataAddRemove.addItem(_fromUtf8(""))
        self.cboMetadataAddRemove.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.cboMetadataAddRemove)
        self.label_72 = QtGui.QLabel(self.dockWidgetContents)
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.horizontalLayout_12.addWidget(self.label_72)
        self.cboMetadataField = QtGui.QComboBox(self.dockWidgetContents)
        self.cboMetadataField.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cboMetadataField.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.cboMetadataField.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.cboMetadataField.setObjectName(_fromUtf8("cboMetadataField"))
        self.horizontalLayout_12.addWidget(self.cboMetadataField)
        self.cboMetadataRelationship = QtGui.QComboBox(self.dockWidgetContents)
        self.cboMetadataRelationship.setObjectName(_fromUtf8("cboMetadataRelationship"))
        self.cboMetadataRelationship.addItem(_fromUtf8(""))
        self.cboMetadataRelationship.addItem(_fromUtf8(""))
        self.cboMetadataRelationship.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.cboMetadataRelationship)
        self.cboMetadataValue = QtGui.QComboBox(self.dockWidgetContents)
        self.cboMetadataValue.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cboMetadataValue.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.cboMetadataValue.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.cboMetadataValue.setObjectName(_fromUtf8("cboMetadataValue"))
        self.horizontalLayout_12.addWidget(self.cboMetadataValue)
        self.tbMetadataFilter = QtGui.QToolButton(self.dockWidgetContents)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/filter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbMetadataFilter.setIcon(icon3)
        self.tbMetadataFilter.setIconSize(QtCore.QSize(24, 24))
        self.tbMetadataFilter.setObjectName(_fromUtf8("tbMetadataFilter"))
        self.horizontalLayout_12.addWidget(self.tbMetadataFilter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.tableMetadata = QtGui.QTableWidget(self.dockWidgetContents)
        self.tableMetadata.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableMetadata.setAlternatingRowColors(True)
        self.tableMetadata.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableMetadata.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableMetadata.setShowGrid(True)
        self.tableMetadata.setRowCount(5)
        self.tableMetadata.setColumnCount(5)
        self.tableMetadata.setObjectName(_fromUtf8("tableMetadata"))
        self.tableMetadata.setColumnCount(5)
        self.tableMetadata.setRowCount(5)
        self.tableMetadata.horizontalHeader().setVisible(False)
        self.tableMetadata.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableMetadata)
        MetadataTableDlg.setWidget(self.dockWidgetContents)

        self.retranslateUi(MetadataTableDlg)
        self.cboMetadataRelationship.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MetadataTableDlg)

    def retranslateUi(self, MetadataTableDlg):
        MetadataTableDlg.setWindowTitle(QtGui.QApplication.translate("MetadataTableDlg", "Metadata table", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataAddAll.setToolTip(QtGui.QApplication.translate("MetadataTableDlg", "Set all samples as active", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataAddAll.setStatusTip(QtGui.QApplication.translate("MetadataTableDlg", "Set all samples as active", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataAddAll.setText(QtGui.QApplication.translate("MetadataTableDlg", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataRemoveAll.setToolTip(QtGui.QApplication.translate("MetadataTableDlg", "Remove all samples from active set", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataRemoveAll.setStatusTip(QtGui.QApplication.translate("MetadataTableDlg", "Remove all samples from active set", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataRemoveAll.setText(QtGui.QApplication.translate("MetadataTableDlg", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_70.setText(QtGui.QApplication.translate("MetadataTableDlg", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboMetadataAddRemove.setItemText(0, QtGui.QApplication.translate("MetadataTableDlg", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cboMetadataAddRemove.setItemText(1, QtGui.QApplication.translate("MetadataTableDlg", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_72.setText(QtGui.QApplication.translate("MetadataTableDlg", "all samples where", None, QtGui.QApplication.UnicodeUTF8))
        self.cboMetadataRelationship.setItemText(0, QtGui.QApplication.translate("MetadataTableDlg", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.cboMetadataRelationship.setItemText(1, QtGui.QApplication.translate("MetadataTableDlg", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.cboMetadataRelationship.setItemText(2, QtGui.QApplication.translate("MetadataTableDlg", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataFilter.setToolTip(QtGui.QApplication.translate("MetadataTableDlg", "Apply filtering criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataFilter.setStatusTip(QtGui.QApplication.translate("MetadataTableDlg", "Apply filtering criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMetadataFilter.setText(QtGui.QApplication.translate("MetadataTableDlg", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMetadata.setSortingEnabled(True)

import STAMP_rc