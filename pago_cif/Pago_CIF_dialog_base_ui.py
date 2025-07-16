# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pago_CIF_dialog_base.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from qgsmaplayercombobox import QgsMapLayerComboBox

class PagoCIFDialog(object):
    def setupUi(self, PagoCIFDialogBase):
        if not PagoCIFDialogBase.objectName():
        PagoCIFDialogBase.setObjectName(u"PagoCIFDialogBase")
        PagoCIFDialogBase.resize(433, 594)
        PagoCIFDialogBase.setMinimumSize(QSize(433, 331))
        self.groupBox = QGroupBox(PagoCIFDialogBase)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 411, 151))  
        self.cBDepartamento = QComboBox
        self.cBDepartamento.setObjectName(u"cBDepartamento")
        self.lbPNIS = QLabel
        self.lbPNIS.setObjectName(u"lbPNIS")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.lbPNIS.setFont(font)
        self.lbPDET = QLabel
        self.lbPDET.setObjectName(u"lbPDET")
        self.lbPDET.setFont(font)
        self.label = QLabel
        self.label.setObjectName(u"label")
        self.label_3 = QLabel
        self.label_3.setObjectName(u"label_3")
        self.lERegion = QLineEdit
        self.lERegion.setObjectName(u"lERegion")
        self.lERegion.setReadOnly(True)
        self.cBMunicipio = QComboBox(self.gridLayoutWidget)
        self.cBMunicipio.setObjectName(u"cBMunicipio")
        self.groupBox_2 = QGroupBox(PagoCIFDialogBase)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 180, 411, 191))    
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.cBAreaBosque = QCheckBox
        self.cBAreaBosque.setObjectName(u"cBAreaBosque")
        self.label_6 = QLabel
        self.label_6.setObjectName(u"label_6")
        self.label_10 = QLabel(
        self.label_10.setObjectName(u"label_10")
        self.label_11 = QLabel
        self.label_11.setObjectName(u"label_11")
        self.mMCbPlantacion = QgsMapLayerComboBox
        self.mMCbPlantacion.setObjectName(u"mMCbPlantacion")
        self.cBEspecie = QComboBox
        self.cBEspecie.setObjectName(u"cBEspecie")
        self.dSPDensidad = QSpinBox
        self.dSPDensidad.setObjectName(u"dSPDensidad")
        self.dSPDensidad.setCursor(QCursor(Qt.UpArrowCursor))
        self.dSPDensidad.setMinimum(50)
        self.dSPDensidad.setMaximum(1000000000)
        self.dSPDensidad.setValue(50)
        self.cBEtapa = QComboBox
        self.cBEtapa.addItem("")
        self.cBEtapa.addItem("")
        self.cBEtapa.addItem("")
        self.cBEtapa.addItem("")
        self.cBEtapa.addItem("")
        self.cBEtapa.setObjectName(u"cBEtapa")
        self.groupBox_3 = QGroupBox(PagoCIFDialogBase)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 380, 411, 91))
        self.lbUniPlantacion = QLabel
        self.lbUniPlantacion.setObjectName(u"lbUniPlantacion")
        self.lbUniPlantacion.setEnabled(True)
        self.lbUniBosque = QLabel
        self.lbUniBosque.setObjectName(u"lbUniBosque")
        self.lbUniBosque.setEnabled(True)
        self.lEAreaPlantacion = QLineEdit
        self.lEAreaPlantacion.setObjectName(u"lEAreaPlantacion")
        self.lEAreaPlantacion.setEnabled(True)
        self.lEAreaPlantacion.setReadOnly(True)
        self.lEAreaBosque = QLineEdit
        self.lEAreaBosque.setObjectName(u"lEAreaBosque")
        self.lEAreaBosque.setEnabled(True)
        self.lEAreaBosque.setReadOnly(True)
        self.lEAreaBosque.setClearButtonEnabled(False)
        self.lbAreaPlantacion = QLabel
        self.lbAreaPlantacion.setObjectName(u"lbAreaPlantacion")
        self.lbAreaBosque = QLabel
        self.lbAreaBosque.setObjectName(u"lbAreaBosque")
        self.grBResultado = QGroupBox
        self.grBResultado.setObjectName(u"grBResultado")
        self.lePagoCif = QLineEdit(self.grBResultado)
        self.lePagoCif.setObjectName(u"lePagoCif")
        self.lePagoCif.setGeometry(QRect(89, 20, 261, 20))
        self.lePagoCif.setReadOnly(True)
        self.lePagoCif.setClearButtonEnabled(False)
        self.label_12 = QLabel(self.grBResultado)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 15, 51, 29))
        self.pBCalcular = QPushButton
        self.pBCalcular.setObjectName(u"pBCalcular")
        self.pBLimpiar = QPushButton
        self.pBLimpiar.setObjectName(u"pBLimpiar")
        self.pBAyuda = QPushButton(PagoCIFDialogBase)
        self.pBAyuda.setObjectName(u"pBAyuda")
        self.pBAyuda.setGeometry(QRect(350, 0, 75, 23))
        self.retranslateUi(PagoCIFDialogBase)
        QMetaObject.connectSlotsByName(PagoCIFDialogBase)
    # setupUi

    def retranslateUi(self, PagoCIFDialogBase):
        PagoCIFDialogBase.setWindowTitle(QCoreApplication.translate("PagoCIFDialogBase", u"Pago CIF", None))
        self.groupBox.setTitle(QCoreApplication.translate("PagoCIFDialogBase", u"Informaci\u00f3n Territorial", None))
        self.label_2.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Municipio", None))
        self.lbPNIS.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Es PNIS", None))
        self.lbPDET.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Es PDET", None))
        self.label.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Departamento", None))
        self.label_3.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Regi\u00f3n", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PagoCIFDialogBase", u"Datos de coberturas", None))
        self.label_4.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Capa de plantaci\u00f3n", None))
        self.cBAreaBosque.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Cacular \u00e1rea de bosque", None))
        self.label_6.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Especie", None))
        self.label_10.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Densidad", None))
        self.label_11.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Etapa", None))
        self.cBEtapa.setItemText(0, QCoreApplication.translate("PagoCIFDialogBase", u"Establecimiento", None))
        self.cBEtapa.setItemText(1, QCoreApplication.translate("PagoCIFDialogBase", u"Mantenimiento 1", None))
        self.cBEtapa.setItemText(2, QCoreApplication.translate("PagoCIFDialogBase", u"Mantenimiento 2", None))
        self.cBEtapa.setItemText(3, QCoreApplication.translate("PagoCIFDialogBase", u"Mantenimiento 3", None))
        self.cBEtapa.setItemText(4, QCoreApplication.translate("PagoCIFDialogBase", u"Mantenimiento 4", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("PagoCIFDialogBase", u"\u00c1reas", None))
        self.lbUniPlantacion.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Hect\u00e1reas", None))
        self.lbUniBosque.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Hect\u00e1reas", None))
        self.lbAreaPlantacion.setText(QCoreApplication.translate("PagoCIFDialogBase", u"\u00c1rea plantaci\u00f3n", None))
        self.lbAreaBosque.setText(QCoreApplication.translate("PagoCIFDialogBase", u"\u00c1rea bosque", None))
        self.grBResultado.setTitle(QCoreApplication.translate("PagoCIFDialogBase", u"Resultado", None))
        self.label_12.setText(QCoreApplication.translate("PagoCIFDialogBase", u"PagoCIF", None))
        self.pBCalcular.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Calcular", None))
        self.pBLimpiar.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Limpiar", None))
        self.pBAyuda.setText(QCoreApplication.translate("PagoCIFDialogBase", u"Ver ayuda", None))
    # retranslateUi

