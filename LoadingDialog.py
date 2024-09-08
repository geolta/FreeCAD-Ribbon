# *************************************************************************************
# *   MIT License                                                                     *
# *                                                                                   *
# *   Copyright (c) 2024 Paul Ebbers                                                  *
# *                                                                                   *
# *   Permission is hereby granted, free of charge, to any person obtaining a copy    *
# *   of this software and associated documentation files (the "Software"), to deal   *
# *   in the Software without restriction, including without limitation the rights    *
# *   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       *
# *   copies of the Software, and to permit persons to whom the Software is           *
# *   furnished to do so, subject to the following conditions:                        *
# *                                                                                   *
# *   The above copyright notice and this permission notice shall be included in all  *
# *   copies or substantial portions of the Software.                                 *
# *                                                                                   *
# *   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      *
# *   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        *
# *   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     *
# *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          *
# *   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   *
# *   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   *
# *   SOFTWARE.                                                                       *
# *                                                                                   *
# *************************************************************************************/
import FreeCAD as App
import FreeCADGui as Gui
import os

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QProgressBar,
)
from PySide6.QtCore import Qt, SIGNAL
import sys
import Parameters_Ribbon
import LoadDesign_Ribbon

# Get the resources
pathUI = Parameters_Ribbon.UI_LOCATION
sys.path.append(pathUI)


# import graphical created Ui. (With QtDesigner or QtCreator)
import LoadingDialog_ui as LoadingDialog_ui

# Define the translation
translate = App.Qt.translate


class LoadingDialog(LoadingDialog_ui.Ui_LoadingwokrbenchesLoadingDialog):
    No_WorkBenches = 0

    def __init__(self):
        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadingDialog, self).__init__()

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "LoadingDialog.ui"))

        QProgressBar(self.form.progressBar).setValue(0)

        return

    def LoadWorkBenches(self):
        List_Workbenches = Gui.listWorkbenches()

        for WorkBenchName in List_Workbenches:
            if str(WorkBenchName) != "" or WorkBenchName is not None:
                if str(WorkBenchName) != "NoneWorkbench":
                    Gui.activateWorkbench(WorkBenchName)
                    currentValue = QProgressBar(self.form.progressBar).value
                    NewValue = currentValue + 1

                    QProgressBar(self.form.progressBar).setValue(NewValue)

        LoadDesign_Ribbon.main()
        self.form.close()
        return


def main():
    # Get the form
    Dialog = LoadingDialog.form
    # Show the form
    Dialog.show()

    return
