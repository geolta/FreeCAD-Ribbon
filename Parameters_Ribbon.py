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
if Settings.GetBoolSetting("AutoHideRibbon") is True:
    AUTOHIDE_RIBBON = Settings.GetBoolSetting("AutoHideRibbon")
else:
    AUTOHIDE_RIBBON = bool(False)
if Settings.GetStringSetting("Stylesheet") != "":
    STYLESHEET = Settings.GetStringSetting("Stylesheet")
else:
    STYLESHEET = os.path.join(STYLESHEET_LOCATION, "base.qss")