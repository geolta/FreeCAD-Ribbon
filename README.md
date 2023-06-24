## FreeCAD Ribbon UI

A draft to implement a proper Ribbon UI for FreeCAD, based on the work of [HakanSeven](https://github.com/HakanSeven12/Modern-UI) and the [PyQtRibbon library](https://github.com/haiiliin/pyqtribbon).

![Screenshots of FreeCAD with the Ribbon UI](Screenshot.png)

This is not finished or intended for production use, but rather to look at where the limitations of this approach, implementing it as an external Python addon, lie.

## Installation
Download this repository, extract the folder and copy it to the `Mod` folder of your FreeCAD installation.

## Uninstallation
1. Remove the folder of this in the `Mod` folder of your FreeCAD installation
1. Restart FreeCAD.
1. When you restarted you don't see any toolbar.
1. Create a macro.
1. Paste this code in to macro.
    ```
    from PySide2 import QtCore, QtGui, QtWidgets
    mw = FreeCADGui.getMainWindow()
    mw.menuBar().show()

    WBList = FreeCADGui.listWorkbenches()
    for WB in WBList:
        FreeCADGui.activateWorkbench(WB)
        for tb in mw.findChildren(QtWidgets.QToolBar):
            tb.show()
    ```
1. Execute the macro
1. Restart FreeCAD.

## Settings

Since this addon is more like a draft, there is no real preferences page, but the following settings can be set manually under `Tools / Edit Parameters...` and the path `BaseApp/RibbonUI`:
- `ShowText` (bool) whether to display tool text for small buttons
- `Enabled` (string) comma-separated list of workbenches that shall be displayed as tabs

The way the tools / commands are displayed in the tabs is determined by `RibbonStructure.json`. There you can change the order of the tools in the tool groups and set the size of it. Until now, there are only a few entries for the Sketcher Workbench and the measurement tools, feel free to improve this :)

## Discussion
Feel free to discuss this addon on the [FreeCAD Forum](XXX). This is also the place where I discuss the limitations of this approach as a Python Addon.

## Known Issues
- When working in the PartDesign workbench, the automatic switching to the Sketcher workbench and back doesn't work, you have to do it manually.
- The workbench that should be loaded on startup is ignored, it will always start with the Arch workbench and you have to switch manually.

## License
GPL v3.0 (see [LICENSE](LICENSE))
