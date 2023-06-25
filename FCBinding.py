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

import os
import json

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QToolButton, QToolBar, QDockWidget, QWidget, QSizePolicy
from pyqtribbon import RibbonBar

import FreeCAD as App
import FreeCADGui as Gui


mw = Gui.getMainWindow()
path = os.path.dirname(__file__) + "/Resources/icons/"


class ModernMenu(RibbonBar):
    """
    Create ModernMenu QWidget.
    """

    ribbonStructure = None

    actions = {}
    Enabled = {}

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

        self.tabBar().currentChanged.connect(self.selectWorkbench)

        # read ribbon structure from JSON file
        with open(
            os.path.join(os.path.dirname(__file__), "RibbonStructure.json"), "r"
        ) as file:
            ModernMenu.ribbonStructure = json.load(file)

        self.createModernMenu()
        self.selectWorkbench()

    def createModernMenu(self):
        """
        Create menu tabs.
        """

        # add quick access buttons
        for commandName in ModernMenu.ribbonStructure["quickAccessCommands"]:
            button = QToolButton()
            action = Gui.Command.get(commandName).getAction()
            # XXX for debugging purposes
            if len(action) == 0:
                print(f"{commandName} has no action")
            elif len(action) > 1:
                print(f"{commandName} has more than one action")

            button.setDefaultAction(action[0])
            self.addQuickAccessButton(button)

        # add category for each workbench
        for workbenchName, workbench in Gui.listWorkbenches().items():
            if (
                workbenchName == ""
                or workbench.MenuText
                in ModernMenu.ribbonStructure["ignoredWorkbenches"]
            ):
                continue

            Name = workbench.MenuText
            self.actions[Name] = workbenchName
            self.Enabled[Name] = False

            self.addCategory(Name)

        # application icon
        self.setApplicationIcon(Gui.getIcon("freecad"))

    def selectWorkbench(self):
        """
        Import selected workbench toolbars to ModernMenu section.
        """

        index = self.tabBar().currentIndex()
        tabName = self.tabBar().tabText(index)
        category = self.currentCategory()

        # Activate selected workbench
        tabName = tabName.replace("&", "")
        Gui.activateWorkbench(self.actions[tabName])
        workbench = Gui.activeWorkbench()

        # hide normal toolbars
        for tbb in mw.findChildren(QToolBar):
            if tbb.objectName() not in [
                "",
                "draft_status_scale_widget",
                "draft_snap_widget",
            ]:
                tbb.hide()

        if self.Enabled[tabName]:
            return
        if not hasattr(workbench, "__Workbench__"):
            return

        for toolbar in workbench.listToolbars():
            if toolbar in ModernMenu.ribbonStructure["ignoredToolbars"]:
                continue

            panel = category.addPanel(toolbar.replace(tabName + " ", "").capitalize())

            # get list of all buttons in toolbar
            TB = mw.findChildren(QToolBar, toolbar)
            allButtons = TB[0].findChildren(QToolButton)

            # order buttons like defined in ribbonStructure
            if (
                toolbar in ModernMenu.ribbonStructure["toolbars"]
                and "order" in ModernMenu.ribbonStructure["toolbars"][toolbar]
            ):
                positionsList = ModernMenu.ribbonStructure["toolbars"][toolbar]["order"]

                # XXX check that positionsList consists of strings only

                def sortButtons(button):
                    if button.text() == "":
                        return -1

                    position = None
                    try:
                        position = positionsList.index(button.defaultAction().data())
                    except ValueError:
                        position = 999999

                    return position

                allButtons.sort(key=sortButtons)

            # add buttons to panel
            for button in allButtons:
                if button.text() == "":
                    continue
                action = button.defaultAction()

                # whether to show text of the button
                showText = (
                    ModernMenu.ribbonStructure["showText"]
                    and not toolbar in ModernMenu.ribbonStructure["iconOnlyToolbars"]
                )

                # get button size from ribbonStructure
                try:
                    buttonSize = ModernMenu.ribbonStructure["toolbars"][toolbar]["commands"][action.data()]["size"]
                except KeyError:
                    buttonSize = "small"  # small as default

                if buttonSize == "small":
                    btn = panel.addSmallButton(
                        action.text(),
                        action.icon(),
                        alignment=Qt.AlignLeft,
                        showText=showText,
                    )
                elif buttonSize == "medium":
                    btn = panel.addMediumButton(
                        action.text(),
                        action.icon(),
                        alignment=Qt.AlignLeft,
                    )  # medium will always have text
                elif buttonSize == "large":
                    btn = panel.addLargeButton(
                        action.text(), action.icon()
                    )  # large will always have text and are aligned in center
                else:
                    raise NotImplementedError(
                        "Given button size not implemented, only small, medium and large are available."
                    )

                btn.setDefaultAction(action)
                # add dropdown menu if necessary
                if button.menu() is not None:
                    btn.setMenu(button.menu())
                    btn.setPopupMode(QToolButton.InstantPopup)

        self.Enabled[tabName] = True


class run:
    """
    Activate Modern UI.
    """

    def __init__(self, name):
        """
        Constructor
        """
        disable = 0
        if name != "NoneWorkbench":
            # Disable connection after activation
            mw = Gui.getMainWindow()
            mw.workbenchActivated.disconnect(run)
            if disable:
                return

            ribbon = ModernMenu()
            # mw.setMenuBar(ribbon)

            ribbonDock = QDockWidget()
            ribbonDock.setTitleBarWidget(QWidget())
            ribbonDock.setMinimumHeight(0)
            sp = ribbonDock.sizePolicy()
            sp.setVerticalPolicy(QSizePolicy.Ignored)
            ribbonDock.setWidget(ribbon)
            mw.addDockWidget(Qt.TopDockWidgetArea, ribbonDock)
