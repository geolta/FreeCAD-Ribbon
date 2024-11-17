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

from PySide.QtCore import Qt, QTimer
from PySide.QtWidgets import QToolButton, QToolBar, QDockWidget, QWidget, QSizePolicy
from PySide.QtGui import QIcon

from pyqtribbon import RibbonBar

import FreeCAD as App
import FreeCADGui as Gui


mw = Gui.getMainWindow()
path = os.path.dirname(__file__) + "/Resources/icons/"
timer = QTimer()


class ModernMenu(RibbonBar):
    """
    Create ModernMenu QWidget.
    """

    ribbonStructure = None

    wbNameMapping = {}
    isWbLoaded = {}

    def __init__(self):
        """
        Constructor
        """

        # use icon size from FreeCAD preferences
        iconSize: int = App.ParamGet(
            "User parameter:BaseApp/Preferences/General"
        ).GetInt("ToolbarIconSize", 24)

        super().__init__(title="", iconSize=iconSize)

        self.connectSignals()

        # read ribbon structure from JSON file
        with open(
            os.path.join(os.path.dirname(__file__), "RibbonStructure.json"), "r"
        ) as file:
            ModernMenu.ribbonStructure = json.load(file)

        self.createModernMenu()
        self.onUserChangedWorkbench()

    def connectSignals(self):
        self.tabBar().currentChanged.connect(self.onUserChangedWorkbench)
        mw.workbenchActivated.connect(self.onWbActivated)

    def disconnectSignals(self):
        self.tabBar().currentChanged.disconnect(self.onUserChangedWorkbench)
        mw.workbenchActivated.disconnect(self.onWbActivated)

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

            name = workbench.MenuText
            self.wbNameMapping[name] = workbenchName
            self.isWbLoaded[name] = False

            self.addCategory(name)
            # set tab icon
            self.tabBar().setTabIcon(len(self.categories()) - 1, QIcon(workbench.Icon))

        # application icon
        self.setApplicationIcon(Gui.getIcon("freecad"))

    def onUserChangedWorkbench(self):
        """
        Import selected workbench toolbars to ModernMenu section.
        """

        index = self.tabBar().currentIndex()
        tabName = self.tabBar().tabText(index)
        category = self.currentCategory()

        # activate selected workbench
        tabName = tabName.replace("&", "")
        Gui.activateWorkbench(self.wbNameMapping[tabName])
        self.onWbActivated()

    def onWbActivated(self):
        # switch tab if necessary
        self.updateCurrentTab()

        # hide normal toolbars
        self.hideClassicToolbars()

        # ensure that workbench is already loaded
        workbench = Gui.activeWorkbench()
        if not hasattr(workbench, "__Workbench__"):
            # XXX for debugging purposes
            print(f"wb {workbench.MenuText} not loaded")

            # wait for 0.1s hoping that after that time the workbench is loaded
            timer.timeout.connect(self.onWbActivated)
            timer.setSingleShot(True)
            timer.start(100)

            return

        # create panels
        self.buildPanels()

    def buildPanels(self):
        workbench = Gui.activeWorkbench()
        tabName = self.tabBar().tabText(self.tabBar().currentIndex()).replace("&", "")
        if self.isWbLoaded[tabName]:
            return

        for toolbar in workbench.listToolbars():
            if toolbar in ModernMenu.ribbonStructure["ignoredToolbars"]:
                continue

            panel = self.currentCategory().addPanel(
                toolbar.replace(tabName + " ", "").capitalize()
            )

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

                # try to get alternative text from ribbonStructure
                try:
                    text = ModernMenu.ribbonStructure["toolbars"][toolbar]["commands"][action.data()]["text"]
                    # the text would be overwritten again when the state of the action changes
                    # (e.g. when getting enabled / disabled), therefore the action itself
                    # is manipulated.
                    action.setText(text)
                except KeyError:
                    text = action.text()

                # try to get alternative icon from ribbonStructure
                try:
                    icon = ModernMenu.ribbonStructure["toolbars"][toolbar]["commands"][action.data()]["icon"]
                    action.setIcon(QIcon(os.path.join(path, icon)))
                except KeyError:
                    icon = action.icon()

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

        self.isWbLoaded[tabName] = True

    def updateCurrentTab(self):
        currentWbIndex = self.tabBar().indexOf(Gui.activeWorkbench().MenuText)
        currentTabIndex = self.tabBar().currentIndex()

        if currentWbIndex != currentTabIndex:
            self.disconnectSignals()
            self.tabBar().setCurrentIndex(currentWbIndex)
            self.connectSignals()

    def hideClassicToolbars(self):
        for toolbar in mw.findChildren(QToolBar):
            if toolbar.objectName() not in [
                "",
                "draft_status_scale_widget",
                "draft_snap_widget",
            ]:
                toolbar.hide()


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
