# ***********************************************************************
# *                                                                     *
# * Copyright (c) 2019 Hakan Seven <hakanseven12@gmail.com>             *
# *                                                                     *
# * This program is free software; you can redistribute it and/or modify*
# * it under the terms of the GNU Lesser General Public License (LGPL)  *
# * as published by the Free Software Foundation; either version 3 of   *
# * the License, or (at your option) any later version.                 *
# * for detail see the LICENCE text file.                               *
# *                                                                     *
# * This program is distributed in the hope that it will be useful,     *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of      *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the       *
# * GNU Library General Public License for more details.                *
# *                                                                     *
# * You should have received a copy of the GNU Library General Public   *
# * License along with this program; if not, write to the Free Software *
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307*
# * USA                                                                 *
# *                                                                     *
# ***********************************************************************
import FreeCAD as App
import FreeCADGui as Gui
import os
from inspect import getsourcefile
from PySide.QtGui import QPalette, QIcon
from PySide.QtWidgets import QListWidgetItem, QDialogButtonBox
from PySide.QtCore import SIGNAL, Qt
import sys

# Get the resources
pathIcons = os.path.dirname(__file__) + "/Resources/icons/"
pathStylSheets = os.path.dirname(__file__) + "/Resources/stylesheets/"
pathUI = os.path.dirname(__file__) + "/Resources/ui/"
sys.path.append(pathIcons)
sys.path.append(pathStylSheets)
sys.path.append(pathUI)

# import graphical created Ui. (With QtDesigner or QtCreator)
import Settings_ui as Settings_ui

# Define the translation
translate = App.Qt.translate


class LoadDialog(Settings_ui.Ui_Form):
    def __init__(self):
        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadDialog, self).__init__()

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "Settings.ui"))

        # self.form.setWindowIcon(QIcon(os.path.join(PATH_TB_ICONS, "SetColumns.svg")))

        # Make sure that the dialog stays on top
        self.form.setWindowFlags(Qt.WindowStaysOnTopHint)


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
