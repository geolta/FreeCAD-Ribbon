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

from PySide.QtGui import QIcon, QPixmap, QShowEvent
from PySide.QtWidgets import QProgressBar, QWidget
from PySide.QtCore import (
    Qt,
    SIGNAL,
    QThread,
    Signal,
    QObject,
    QRunnable,
    Slot,
    QThreadPool,
    QEvent,
    QTimer,
)
import sys
import Parameters_Ribbon
import LoadDesign_Ribbon
import time

# Get the resources
pathUI = Parameters_Ribbon.UI_LOCATION
sys.path.append(pathUI)

# Define a timer
timer = QTimer()


# import graphical created Ui. (With QtDesigner or QtCreator)
import LoadingDialog_ui as LoadingDialog_ui

# Define the translation
translate = App.Qt.translate


class LoadingDialog(LoadingDialog_ui.Ui_Form):
    List_Workbenches = []

    def __init__(self):
        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadingDialog, self).__init__()

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "LoadingDialog.ui"))

        # Get the style from the main window and use it for this form
        mw = Gui.getMainWindow()
        palette = mw.palette()
        self.form.setPalette(palette)
        Style = mw.style()
        self.form.setStyle(Style)

        self.form.setStyleSheet(Parameters_Ribbon.STYLESHEET)

        self.form.progressBar.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # set the progressbar to zero
        self.form.progressBar.setValue(0)

        self.List_Workbenches = Gui.listWorkbenches()

        Maximum = 0
        for WorkBenchName in self.List_Workbenches:
            if str(WorkBenchName) != "" or WorkBenchName is not None:
                if str(WorkBenchName) != "NoneWorkbench":
                    Maximum = Maximum + 1
        self.form.progressBar.setMaximum(Maximum)

        return

    def reportProgress(self, n):
        self.form.progressBar.setValue(n)

    # Worker


def main():
    # Get the form
    Dialog = LoadingDialog()
    # Show the form
    Dialog.form.show()
    # Dialog.runLongTask()

    return
