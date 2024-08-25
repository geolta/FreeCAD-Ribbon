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
from PySide.QtGui import QColor
import os
import sys

# Define the translation
translate = App.Qt.translate

preferences = App.ParamGet("User parameter:BaseApp/Preferences/Mod/FreeCAD-Ribbon")


class Settings:

    # region -- Functions to read the settings from the FreeCAD Parameters
    # and make sure that a None type result is ""
    def GetStringSetting(settingName: str) -> str:
        result = preferences.GetString(settingName)

        if result.lower() == "none":
            result = ""
        return result

    def GetIntSetting(settingName: str) -> int:
        result = preferences.GetInt(settingName)
        if result == "":
            result = None
        return result

    def GetFloatSetting(settingName: str) -> int:
        result = preferences.GetFloat(settingName)
        if result == "":
            result = None
        return result

    def GetBoolSetting(settingName: str) -> bool:
        result = preferences.GetBool(settingName)
        if str(result).lower() == "none":
            result = False
        return result

    def GetColorSetting(settingName: str) -> object:
        # Create a tuple from the int value of the color
        result = QColor.fromRgba(preferences.GetUnsigned(settingName)).toTuple()

        # correct the order of the tuple and devide them by 255
        result = (result[3] / 255, result[0] / 255, result[1] / 255, result[2] / 255)

        return result

    # endregion

    # region - Functions to write settings to the FreeCAD Parameters
    #
    #
    def SetStringSetting(settingName: str, value: str):
        if value.lower() == "none":
            value = ""
        preferences.SetString(settingName, value)
        return

    def SetBoolSetting(settingName: str, value):
        if str(value).lower() == "true":
            Bool = True
        if str(value).lower() == "none" or str(value).lower() != "true":
            Bool = False
        preferences.SetBool(settingName, Bool)
        return

    def SetIntSetting(settingName: str, value: int):
        if str(value).lower() != "":
            preferences.SetInt(settingName, value)
        return

    # endregion


# Define the resources
ICON_LOCATION = os.path.dirname(__file__) + "/Resources/icons/"
STYLESHEET_LOCATION = os.path.dirname(__file__) + "/Resources/stylesheets/"
UI_LOCATION = os.path.dirname(__file__) + "/Resources/ui/"

# Define the icon sizes
if Settings.GetIntSetting("IconSize_Small") is not None or Settings.GetIntSetting("IconSize_Small") > 0:
    ICON_SIZE_SMALL = Settings.GetIntSetting("IconSize_Small")
else:
    ICON_SIZE_SMALL = int(24)

if Settings.GetIntSetting("IconSize_Medium") is not None or Settings.GetIntSetting("IconSize_Medium") > 0:
    ICON_SIZE_MEDIUM = Settings.GetIntSetting("IconSize_Medium")
else:
    ICON_SIZE_MEDIUM = int(44)

if Settings.GetIntSetting("IconSize_Large") is not None or Settings.GetIntSetting("IconSize_Large") > 0:
    ICON_SIZE_LARGE = Settings.GetIntSetting("IconSize_Large")
else:
    ICON_SIZE_LARGE = int(64)


# Backup parameters
if Settings.GetBoolSetting("BackupEnabled") is True:
    ENABLE_BACKUP = Settings.GetBoolSetting("BackupEnabled")
else:
    ENABLE_BACKUP = bool(True)
if Settings.GetStringSetting("BackupFolder") != "":
    BACKUP_LOCATION = Settings.GetStringSetting("BackupFolder")
else:
    BACKUP_LOCATION = os.path.dirname(__file__) + "/Backups"

# Additional parameter
HELP_ADRESS = str("https://wiki.freecad.org/Main_Page")

# Ribbon settings
if Settings.GetBoolSetting("AutoHideRibbon") is True:
    AUTOHIDE_RIBBON = Settings.GetBoolSetting("AutoHideRibbon")
else:
    AUTOHIDE_RIBBON = bool(False)
if Settings.GetStringSetting("Stylesheet") != "":
    STYLESHEET = Settings.GetStringSetting("Stylesheet")
else:
    STYLESHEET = os.path.join(STYLESHEET_LOCATION, "base.qss")

if Settings.GetBoolSetting("ShowIconText_Small") is True:
    SHOW_ICON_TEXT_SMALL = Settings.GetBoolSetting("ShowIconText_Small")
else:
    SHOW_ICON_TEXT_SMALL = bool(False)

if Settings.GetBoolSetting("ShowIconText_Medium") is True:
    SHOW_ICON_TEXT_MEDIUM = Settings.GetBoolSetting("ShowIconText_Medium")
else:
    SHOW_ICON_TEXT_MEDIUM = bool(False)

if Settings.GetBoolSetting("ShowIconText_Large") is True:
    SHOW_ICON_TEXT_LARGE = Settings.GetBoolSetting("ShowIconText_Large")
else:
    SHOW_ICON_TEXT_LARGE = bool(False)
