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
import math

# Define the translation
translate = App.Qt.translate


def Mbox(
    text,
    title="",
    style=0,
    IconType="Information",
    default="",
    stringList="[,]",
    OnTop: bool = False,
):
    """
    Message Styles:\n
    0 : OK                          (text, title, style)\n
    1 : Yes | No                    (text, title, style)\n
    2 : Ok | Cancel                 (text, title, style)\n
    20 : Inputbox                   (text, title, style, default)\n
    21 : Inputbox with dropdown     (text, title, style, default, stringlist)\n
    Icontype:                       string: NoIcon, Question, Warning, Critical. Default Information
    """
    from PySide.QtWidgets import QMessageBox, QInputDialog
    from PySide.QtCore import Qt
    from PySide import QtWidgets

    Icon = QMessageBox.Information
    if IconType == "NoIcon":
        Icon = QMessageBox.NoIcon
    if IconType == "Question":
        Icon = QMessageBox.Question
    if IconType == "Warning":
        Icon = QMessageBox.Warning
    if IconType == "Critical":
        Icon = QMessageBox.Critical

    if style == 0:
        # Set the messagebox
        msgBox = QMessageBox()
        msgBox.setIcon(Icon)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)

        reply = msgBox.exec_()
        if reply == QMessageBox.Ok:
            return "ok"
    if style == 1:
        # Set the messagebox
        msgBox = QMessageBox()
        msgBox.setIcon(Icon)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        # Set the buttons and default button
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)

        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            return "yes"
        if reply == QMessageBox.No:
            return "no"
    if style == 2:
        # Set the messagebox
        msgBox = QMessageBox()
        msgBox.setIcon(Icon)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        # Set the buttons and default button
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)

        reply = msgBox.exec_()
        if reply == QMessageBox.Ok:
            return "ok"
        if reply == QMessageBox.Cancel:
            return "cancel"
    if style == 20:
        Dialog = QInputDialog()
        reply = Dialog.getText(
            None,
            title,
            text,
            text=default,
        )
        if reply[1]:
            # user clicked OK
            replyText = reply[0]
        else:
            # user clicked Cancel
            replyText = reply[0]  # which will be "" if they clicked Cancel
        return str(replyText)
    if style == 21:
        Dialog = QInputDialog()
        reply = Dialog.getItem(
            None,
            title,
            text,
            stringList,
            0,
            True,
        )
        if reply[1]:
            # user clicked OK
            replyText = reply[0]
        else:
            # user clicked Cancel
            replyText = reply[0]  # which will be "" if they clicked Cancel
        return str(replyText)


def RestartDialog(includeIcons=False):
    """_summary_
        shows a restart dialog
    Returns:
        string: returns 'yes' if restart now is clicked.
        otherwise returns 'no'
    """
    from PySide.QtWidgets import QMessageBox

    # Set the messagebox
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText("You must restart FreeCAD for changes to take effect.")
    msgBox.setWindowTitle("FreeCAD Ribbon")
    # Set the buttons and default button
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.No)
    msgBox.button(QMessageBox.Yes).setText("Restart now")
    msgBox.button(QMessageBox.No).setText("Restart later")
    if includeIcons is True:
        msgBox.button(QMessageBox.No).setIcon(Gui.getIcon("Cancel.svg"))
        msgBox.button(QMessageBox.Yes).setIcon(Gui.getIcon("OK.svg"))

    reply = msgBox.exec_()
    if reply == QMessageBox.Yes:
        return "yes"
    if reply == QMessageBox.No:
        return "no"


def SaveDialog(files, OverWrite: bool = True):
    """
    files must be like:\n
    files = [\n
        ('All Files', '*.*'),\n
        ('Python Files', '*.py'),\n
        ('Text Document', '*.txt')\n
    ]\n
    \n
    OverWrite:\n
    If True, file will be overwritten\n
    If False, only the path+filename will be returned\n
    """
    import tkinter as tk
    from tkinter.filedialog import asksaveasfile
    from tkinter.filedialog import askopenfilename

    # Create the window
    root = tk.Tk()
    # Hide the window
    root.withdraw()

    if OverWrite is True:
        file = asksaveasfile(filetypes=files, defaultextension=files)
        if file is not None:
            return file.name
    if OverWrite is False:
        file = askopenfilename(filetypes=files, defaultextension=files)
        if file is not None:
            return file


def GetLetterFromNumber(number: int, UCase: bool = True):
    # from openpyxl.utils import get_column_letter

    # Letter = get_column_letter(number)

    # # If UCase is true, convert to upper case
    # if UCase is True:
    #     Letter = Letter.upper()

    """Number to Excel-style column name, e.g., 1 = A, 26 = Z, 27 = AA, 703 = AAA."""
    Letter = ""
    while number > 0:
        number, r = divmod(number - 1, 26)
        Letter = chr(r + ord("A")) + Letter
    return Letter


def GetNumberFromLetter(Letter):
    # from openpyxl.utils import column_index_from_string

    # Number = column_index_from_string(Letter)

    """Excel-style column name to number, e.g., A = 1, Z = 26, AA = 27, AAA = 703."""
    number = 0
    for c in Letter:
        number = number * 26 + 1 + ord(c) - ord("A")
    return number


def ColorConvertor(ColorRGB: [], Alpha: float = 1) -> ():
    """
    A single function to convert colors to rgba colors as a tuple of float from 0-1
    ColorRGB:   [255,255,255]
    Alpha:      0-1
    """
    from matplotlib import colors as mcolors

    ColorRed = ColorRGB[0] / 255
    colorGreen = ColorRGB[1] / 255
    colorBlue = ColorRGB[2] / 255

    color = (ColorRed, colorGreen, colorBlue)

    result = mcolors.to_rgba(color, Alpha)

    return result


def OpenFile(FileName: str):
    """
    Filename = full path with filename as string
    """
    import subprocess
    import os
    import platform

    try:
        if os.path.exists(FileName):
            if platform.system() == "Darwin":  # macOS
                subprocess.call(("open", FileName))
            elif platform.system() == "Windows":  # Windows
                os.startfile(FileName)
            else:  # linux variants
                print(FileName)
                try:
                    subprocess.check_output(["xdg-open", FileName.strip()])
                except subprocess.CalledProcessError:
                    Print(
                        f"An error occured when opening {FileName}!\n"
                        + "This can happen when running FreeCAD as an AppImage.\n"
                        + "Please install FreeCAD directly.",
                        "Error",
                    )
        else:
            print(f"Error: {FileName} does not exist.")
    except Exception as e:
        raise e


def Print(Input: str, Type: str = ""):
    """_summary_

    Args:
        Input (str): Text to print.\n
        Type (str, optional): Type of message. (enter Warning, Error or Log). Defaults to "".
    """
    import FreeCAD as App

    if Type == "Warning":
        App.Console.PrintWarning(Input + "\n")
    elif Type == "Error":
        App.Console.PrintError(Input + "\n")
    elif Type == "Log":
        App.Console.PrintLog(Input + "\n")
    else:
        App.Console.PrintMessage(Input + "\n")


def LightOrDark(rgbColor=[0, 128, 255, 255]):
    """_summary_
    reference: https://alienryderflex.com/hsp.html
    Args:
        rgbColor (list, optional): RGB color. Defaults to [0, 128, 255, 255].\n
        note: The alpha value is added for completeness, but us ignored in the equation.

    Returns:
        string: "light or dark"
    """
    [r, g, b, a] = rgbColor
    hsp = math.sqrt(0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))
    if hsp > 127.5:
        return "light"
    else:
        return "dark"


def GetFileDialog(Filter="", parent=None, DefaultPath="", SaveAs: bool = True) -> str:
    """
    Set filter like:
    "Images (*.png *.xpm .jpg);;Text files (.txt);;XML files (*.xml)"
    SaveAs:\n
        If True,  as SaveAs dialog will open and the file will be overwritten\n
        If False, an OpenFile dialog will be open and the file will be opened.\n
    """
    from PySide.QtWidgets import QFileDialog

    file = ""
    if SaveAs is False:
        file = QFileDialog.getOpenFileName(
            parent=parent, caption="Select a file", dir=DefaultPath, filter=Filter
        )[0]
    if SaveAs is True:
        file = QFileDialog.getSaveFileName(
            parent=parent, caption="Select a file", dir=DefaultPath, filter=Filter
        )[0]
    return file


def GetFolder(parent=None, DefaultPath="") -> str:
    from PySide.QtWidgets import QFileDialog

    Directory = ""
    Directory = QFileDialog.getExistingDirectory(
        parent=parent, caption="Select Folder", dir=DefaultPath
    )

    return Directory
