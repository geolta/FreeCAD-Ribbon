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

# This script can be used to generate a default json file.
# You can add any customization that you have in this file.
# For workbenches and toolbars that don't have a customization, for each toolbar, the first command is set to large.
# The goal of this script is to provide a starting point for your own ribbon customization.
# The file "RibbonStructure_default.json" is used by the reset button to replace RibbonStructure.json with "RibbonStructure_default.json".

import FreeCAD as App
import FreeCADGui as Gui
import os

import json

from PySide.QtWidgets import (
    QListWidgetItem,
    QTableWidgetItem,
    QListWidget,
    QTableWidget,
    QSpinBox,
    QWidget,
    QToolBar,
    QComboBox,
    QPushButton,
    QToolButton,
    QTabWidget,
)

ParentPath = os.path.dirname(os.path.dirname(__file__))

# Set the path where you want to save this new Json file
# JsonPath = os.path.dirname(__file__)
JsonPath = ParentPath

# Set the file name. Default is "RibbonStructure_default.json".
# This is the file used to reset the ribbon.
JsonName = "RibbonStructure_default.json"

# Define list of the workbenches, toolbars and commands on class level
List_Workbenches = []
StringList_Toolbars = []
List_Commands = []

# Create lists for the several list in the json file.
List_IgnoredToolbars = [
    "Clipboard",
    "Edit",
    "File",
    "Help",
    "Macro",
    "View",
    "Workbench",
]
List_IconOnlyToolbars = ["Structure", "Individual views"]
List_QuickAccessCommands = [
    "Std_New",
    "Std_Save",
    "Std_Undo",
    "Std_Redo",
    "Std_Refresh",
    "Std_Cut",
    "Std_Copy",
    "Std_Paste",
]
List_IgnoredWorkbenches = [
    "Inspection",
    "OpenSCAD",
    "Points",
    "Reverse Engineering",
    "Robot",
    "Test Framework",
]
# Empty definitions of the Dicts for the ribbon and custom panels
Dict_RibbonCommandPanel = {}
Dict_CustomPanels = {}

# Set the text under/next to button on or off.
ShowText_Small = False
ShowText_Medium = False
ShowText_Large = False

# Add workbenches here that you want to exclude from this script.
skipWorkbenchList = []
# skipWorkbenchList = ["PartDesignWorkbench", "AssemblyWorkbench", "SketcherWorkbench"]

# Add toolbars which must have only small icons:
smallOnlyToolbars = ["Structure", "Individual views"]

# Add here your customized panels (toolbars)
Dict_CustomPanels = {
    "customToolbars": {
        "FemWorkbench": {
            "Loads & boundary conditions": {
                "commands": {
                    "Electromagnetic boundary conditions": "Electromagnetic boundary conditions",
                    "Initial flow velocity condition": "Fluid boundary conditions",
                    "Initial pressure condition": "Fluid boundary conditions",
                    "Flow velocity boundary condition": "Fluid boundary conditions",
                    "Fixed boundary condition": "Mechanical boundary conditions and loads",
                    "Rigid body constraint": "Mechanical boundary conditions and loads",
                    "Displacement boundary condition": "Mechanical boundary conditions and loads",
                    "Contact constraint": "Mechanical boundary conditions and loads",
                    "Tie constraint": "Mechanical boundary conditions and loads",
                    "Spring": "Mechanical boundary conditions and loads",
                    "Force load": "Mechanical boundary conditions and loads",
                    "Pressure load": "Mechanical boundary conditions and loads",
                    "Centrifugal load": "Mechanical boundary conditions and loads",
                    "Gravity load": "Mechanical boundary conditions and loads",
                    "Initial temperature": "Thermal boundary conditions and loads",
                    "Heat flux load": "Thermal boundary conditions and loads",
                    "Temperature boundary condition": "Thermal boundary conditions and loads",
                    "Body heat source": "Thermal boundary conditions and loads",
                }
            }
        },
        "TechDrawWorkbench": {
            "TechDraw Dimensions_custom": {
                "commands": {
                    "Dimension": "TechDraw Dimensions",
                    "Insert Balloon Annotation": "TechDraw Dimensions",
                    "Axonometric length dimension": "TechDraw Dimensions",
                    "Insert Landmark Dimension - EXPERIMENTAL": "TechDraw Dimensions",
                    "Repair Dimension References": "TechDraw Dimensions",
                    "Insert '\u2300' Prefix": "TechDraw Extend Dimensions",
                    "Increase Decimal Places": "TechDraw Extend Dimensions",
                }
            }
        },
    },
}

# Add here your customized workbenches to include.
CustomJson_Workbenches = {
    "workbenches": {
        "PartDesignWorkbench": {
            "toolbars": {
                "Part Design Helper": {
                    "order": [
                        "Create datum",
                        "Create datum",
                        "Create body",
                        "Check Geometry",
                        "Create a sub-object(s) shape binder",
                        "Create a clone",
                        "Validate sketch...",
                    ],
                    "commands": {
                        "PartDesign_CompSketches": {
                            "size": "large",
                            "text": "Create datum",
                            "icon": "",
                        },
                        "PartDesign_Body": {
                            "size": "small",
                            "text": "Create body",
                            "icon": "PartDesign_Body",
                        },
                        "Sketcher_ValidateSketch": {
                            "size": "small",
                            "text": "Validate sketch",
                            "icon": "Sketcher_ValidateSketch",
                        },
                        "Part_CheckGeometry": {
                            "size": "small",
                            "text": "Check Geometry",
                            "icon": "Part_CheckGeometry",
                        },
                        "PartDesign_SubShapeBinder": {
                            "size": "small",
                            "text": "Create a sub-object(s) shape binder",
                            "icon": "PartDesign_SubShapeBinder",
                        },
                        "PartDesign_Clone": {
                            "size": "small",
                            "text": "Create a clone",
                            "icon": "PartDesign_Clone",
                        },
                        "PartDesign_CompDatums": {
                            "size": "large",
                            "text": "Create datum",
                            "icon": "",
                        },
                    },
                },
                "Part Design Modeling": {
                    "order": [
                        "Pad",
                        "Revolution",
                        "Pocket",
                        "Hole",
                        "Groove",
                        "Create an additive primitive",
                        "Create a subtractive primitive",
                        "Additive loft",
                        "Additive pipe",
                        "Additive helix",
                        "Subtractive loft",
                        "Subtractive pipe",
                        "Subtractive helix",
                        "Boolean operation",
                    ],
                    "commands": {
                        "PartDesign_Pad": {
                            "size": "large",
                            "text": "Pad",
                            "icon": "PartDesign_Pad",
                        },
                        "PartDesign_Revolution": {
                            "size": "large",
                            "text": "Revolution",
                            "icon": "PartDesign_Revolution",
                        },
                        "PartDesign_AdditiveLoft": {
                            "size": "small",
                            "text": "Additive loft",
                            "icon": "PartDesign_AdditiveLoft",
                        },
                        "PartDesign_AdditivePipe": {
                            "size": "small",
                            "text": "Additive pipe",
                            "icon": "PartDesign_AdditivePipe",
                        },
                        "PartDesign_AdditiveHelix": {
                            "size": "small",
                            "text": "Additive helix",
                            "icon": "PartDesign_AdditiveHelix",
                        },
                        "PartDesign_CompPrimitiveAdditive": {
                            "size": "small",
                            "text": "Add a primitive",
                            "icon": "",
                        },
                        "PartDesign_Pocket": {
                            "size": "large",
                            "text": "Pocket",
                            "icon": "PartDesign_Pocket",
                        },
                        "PartDesign_Hole": {
                            "size": "large",
                            "text": "Hole",
                            "icon": "PartDesign_Hole",
                        },
                        "PartDesign_Groove": {
                            "size": "large",
                            "text": "Groove",
                            "icon": "PartDesign_Groove",
                        },
                        "PartDesign_SubtractiveLoft": {
                            "size": "small",
                            "text": "Subtractive loft",
                            "icon": "PartDesign_SubtractiveLoft",
                        },
                        "PartDesign_SubtractivePipe": {
                            "size": "small",
                            "text": "Subtractive pipe",
                            "icon": "PartDesign_SubtractivePipe",
                        },
                        "PartDesign_SubtractiveHelix": {
                            "size": "small",
                            "text": "Subtractive helix",
                            "icon": "PartDesign_SubtractiveHelix",
                        },
                        "PartDesign_CompPrimitiveSubtractive": {
                            "size": "small",
                            "text": "Substract a primitive",
                            "icon": "",
                        },
                        "PartDesign_Boolean": {
                            "size": "small",
                            "text": "Boolean operation",
                            "icon": "PartDesign_Boolean",
                        },
                    },
                },
                "Individual views": {
                    "order": [
                        "Isometric",
                        "Front",
                        "Top",
                        "Right",
                        "Rear",
                        "Bottom",
                        "Left",
                    ],
                    "commands": {
                        "Std_ViewIsometric": {
                            "size": "small",
                            "text": "Isometric",
                            "icon": "view-axonometric",
                        },
                        "Std_ViewFront": {
                            "size": "small",
                            "text": "Front",
                            "icon": "view-front",
                        },
                        "Std_ViewTop": {
                            "size": "small",
                            "text": "Top",
                            "icon": "view-top",
                        },
                        "Std_ViewRight": {
                            "size": "small",
                            "text": "Right",
                            "icon": "view-right",
                        },
                        "Std_ViewRear": {
                            "size": "small",
                            "text": "Rear",
                            "icon": "view-rear",
                        },
                        "Std_ViewBottom": {
                            "size": "small",
                            "text": "Bottom",
                            "icon": "view-bottom",
                        },
                        "Std_ViewLeft": {
                            "size": "small",
                            "text": "Left",
                            "icon": "view-left",
                        },
                    },
                },
                "order": [
                    "Individual views",
                    "Structure",
                    "Part Design Helper",
                    "Part Design Modeling",
                    "Part Design Dressup",
                    "Part Design Patterns",
                    "Create BOM_custom",
                ],
                "Structure": {
                    "order": [
                        "Create part",
                        "Create group",
                        "Link actions",
                        "Create a variable set",
                    ],
                    "commands": {
                        "Std_Part": {
                            "size": "small",
                            "text": "Create part",
                            "icon": "Geofeaturegroup",
                        },
                        "Std_Group": {
                            "size": "small",
                            "text": "Create group",
                            "icon": "folder",
                        },
                        "Std_LinkActions": {
                            "size": "small",
                            "text": "Link actions",
                            "icon": "",
                        },
                        "Std_VarSet": {
                            "size": "small",
                            "text": "Create a variable set",
                            "icon": "VarSet",
                        },
                    },
                },
                "Part Design Dressup": {
                    "order": ["Fillet", "Chamfer", "Draft", "Thickness"],
                    "commands": {
                        "PartDesign_Fillet": {
                            "size": "large",
                            "text": "Fillet",
                            "icon": "PartDesign_Fillet",
                        },
                        "PartDesign_Chamfer": {
                            "size": "large",
                            "text": "Chamfer",
                            "icon": "PartDesign_Chamfer",
                        },
                        "PartDesign_Draft": {
                            "size": "small",
                            "text": "Draft",
                            "icon": "PartDesign_Draft",
                        },
                        "PartDesign_Thickness": {
                            "size": "small",
                            "text": "Thickness",
                            "icon": "PartDesign_Thickness",
                        },
                    },
                },
                "Part Design Patterns": {
                    "order": [
                        "LinearPattern",
                        "Mirrored",
                        "PolarPattern",
                        "Create MultiTransform",
                    ],
                    "commands": {
                        "PartDesign_Mirrored": {
                            "size": "large",
                            "text": "Mirrored",
                            "icon": "PartDesign_Mirrored",
                        },
                        "PartDesign_LinearPattern": {
                            "size": "large",
                            "text": "LinearPattern",
                            "icon": "PartDesign_LinearPattern",
                        },
                        "PartDesign_PolarPattern": {
                            "size": "small",
                            "text": "PolarPattern",
                            "icon": "PartDesign_PolarPattern",
                        },
                        "PartDesign_MultiTransform": {
                            "size": "small",
                            "text": "Create MultiTransform",
                            "icon": "PartDesign_MultiTransform",
                        },
                    },
                },
            }
        },
        "FemWorkbench": {
            "toolbars": {
                "Model": {
                    "order": [
                        "Analysis container",
                        "Material for solid",
                        "Material for fluid",
                        "Nonlinear mechanical material",
                        "Reinforced material (concrete)",
                        "Material editor",
                        "Beam cross section",
                        "Beam rotation",
                        "Shell plate thickness",
                        "Fluid section for 1D flow",
                    ],
                    "commands": {
                        "FEM_Analysis": {
                            "size": "large",
                            "text": "Analysis container",
                            "icon": "FEM_Analysis",
                        }
                    },
                },
                "Electromagnetic boundary conditions": {
                    "order": ["Electromagnetic boundary conditions"],
                    "commands": {
                        "FEM_CompEmConstraints": {
                            "size": "large",
                            "text": "Electromagnetic boundary conditions",
                            "icon": "",
                        }
                    },
                },
                "Fluid boundary conditions": {
                    "order": [
                        "Initial flow velocity condition",
                        "Initial pressure condition",
                        "Flow velocity boundary condition",
                    ],
                    "commands": {
                        "FEM_ConstraintInitialFlowVelocity": {
                            "size": "large",
                            "text": "Initial flow velocity condition",
                            "icon": "FEM_ConstraintInitialFlowVelocity",
                        }
                    },
                },
                "Geometrical analysis features": {
                    "order": [
                        "Plane multi-point constraint",
                        "Section print feature",
                        "Local coordinate system",
                    ],
                    "commands": {
                        "FEM_ConstraintPlaneRotation": {
                            "size": "large",
                            "text": "Plane multi-point constraint",
                            "icon": "FEM_ConstraintPlaneRotation",
                        }
                    },
                },
                "Mechanical boundary conditions and loads": {
                    "order": [
                        "Fixed boundary condition",
                        "Rigid body constraint",
                        "Displacement boundary condition",
                        "Contact constraint",
                        "Tie constraint",
                        "Spring",
                        "Force load",
                        "Pressure load",
                        "Centrifugal load",
                        "Gravity load",
                    ],
                    "commands": {
                        "FEM_ConstraintFixed": {
                            "size": "large",
                            "text": "Fixed boundary condition",
                            "icon": "FEM_ConstraintFixed",
                        }
                    },
                },
                "Thermal boundary conditions and loads": {
                    "order": [
                        "Initial temperature",
                        "Heat flux load",
                        "Temperature boundary condition",
                        "Body heat source",
                    ],
                    "commands": {
                        "FEM_ConstraintInitialTemperature": {
                            "size": "large",
                            "text": "Initial temperature",
                            "icon": "FEM_ConstraintInitialTemperature",
                        },
                        "FEM_ConstraintHeatflux": {
                            "size": "small",
                            "text": "Heat flux load",
                            "icon": "FEM_ConstraintHeatflux",
                        },
                        "FEM_ConstraintTemperature": {
                            "size": "small",
                            "text": "Temperature boundary condition",
                            "icon": "FEM_ConstraintTemperature",
                        },
                        "FEM_ConstraintBodyHeatSource": {
                            "size": "small",
                            "text": "Body heat source",
                            "icon": "FEM_ConstraintBodyHeatSource",
                        },
                    },
                },
                "Mesh": {
                    "order": [
                        "FEM mesh from shape by Netgen",
                        "FEM mesh from shape by Gmsh",
                        "FEM mesh boundary layer",
                        "FEM mesh refinement",
                        "FEM mesh group",
                        "FEM mesh to mesh",
                    ],
                    "commands": {
                        "FEM_MeshNetgenFromShape": {
                            "size": "large",
                            "text": "FEM mesh from shape by Netgen",
                            "icon": "FEM_MeshNetgenFromShape",
                        }
                    },
                },
                "Solve": {
                    "order": [
                        "Solver CalculiX Standard",
                        "Mechanical equations",
                        "Electromagnetic equations",
                        "Flow equation",
                        "Flux equation",
                        "Heat equation",
                        "Solver job control",
                        "Run solver calculations",
                    ],
                    "commands": {
                        "FEM_SolverCalculiXCcxTools": {
                            "size": "large",
                            "text": "Solver CalculiX Standard",
                            "icon": "FEM_SolverStandard",
                        }
                    },
                },
                "Results": {
                    "order": [
                        "Purge results",
                        "Show result",
                        "Apply changes to pipeline",
                        "Post pipeline from result",
                        "Warp filter",
                        "Scalar clip filter",
                        "Function cut filter",
                        "Region clip filter",
                        "Contours filter",
                        "Line clip filter",
                        "Stress linearization plot",
                        "Data at point clip filter",
                        "Filter functions",
                    ],
                    "commands": {
                        "FEM_ResultsPurge": {
                            "size": "large",
                            "text": "Purge results",
                            "icon": "FEM_ResultsPurge",
                        }
                    },
                },
                "Utilities": {
                    "order": [
                        "Clipping plane on face",
                        "Remove all clipping planes",
                        "Open FEM examples",
                    ],
                    "commands": {
                        "FEM_ClippingPlaneAdd": {
                            "size": "large",
                            "text": "Clipping plane on face",
                            "icon": "FEM_ClippingPlaneAdd",
                        }
                    },
                },
                "order": [
                    "Individual views",
                    "Structure",
                    "Model",
                    "Boundaty conditions & loads_custom",
                    "Geometrical analysis features",
                    "Mesh",
                    "Solve",
                    "Results",
                    "Utilities",
                ],
                "Individual views": {
                    "order": [
                        "Isometric",
                        "Front",
                        "Top",
                        "Right",
                        "Rear",
                        "Bottom",
                        "Left",
                    ],
                    "commands": {
                        "Std_ViewIsometric": {
                            "size": "small",
                            "text": "Isometric",
                            "icon": "view-axonometric",
                        },
                        "Std_ViewFront": {
                            "size": "small",
                            "text": "Front",
                            "icon": "view-front",
                        },
                        "Std_ViewTop": {
                            "size": "small",
                            "text": "Top",
                            "icon": "view-top",
                        },
                        "Std_ViewRight": {
                            "size": "small",
                            "text": "Right",
                            "icon": "view-right",
                        },
                        "Std_ViewRear": {
                            "size": "small",
                            "text": "Rear",
                            "icon": "view-rear",
                        },
                        "Std_ViewBottom": {
                            "size": "small",
                            "text": "Bottom",
                            "icon": "view-bottom",
                        },
                        "Std_ViewLeft": {
                            "size": "small",
                            "text": "Left",
                            "icon": "view-left",
                        },
                    },
                },
                "Boundaty conditions & loads_custom": {
                    "order": [
                        "Fixed boundary condition",
                        "Rigid body constraint",
                        "Displacement boundary condition",
                        "Contact constraint",
                        "Tie constraint",
                        "Spring",
                        "Force load",
                        "Pressure load",
                        "Centrifugal load",
                        "Gravity load",
                        "Electromagnetic boundary conditions",
                        "Initial flow velocity condition",
                        "Initial pressure condition",
                        "Flow velocity boundary condition",
                        "Initial temperature",
                        "Heat flux load",
                        "Temperature boundary condition",
                        "Body heat source",
                    ],
                    "commands": {
                        "FEM_CompEmConstraints": {
                            "size": "small",
                            "text": "Electromagnetic boundary conditions",
                            "icon": "",
                        },
                        "FEM_ConstraintInitialFlowVelocity": {
                            "size": "small",
                            "text": "Initial flow velocity condition",
                            "icon": "FEM_ConstraintInitialFlowVelocity",
                        },
                        "FEM_ConstraintInitialPressure": {
                            "size": "small",
                            "text": "Initial pressure condition",
                            "icon": "FEM_ConstraintInitialPressure",
                        },
                        "FEM_ConstraintFlowVelocity": {
                            "size": "small",
                            "text": "Flow velocity boundary condition",
                            "icon": "FEM_ConstraintFlowVelocity",
                        },
                        "FEM_ConstraintFixed": {
                            "size": "large",
                            "text": "Fixed boundary condition",
                            "icon": "FEM_ConstraintFixed",
                        },
                        "FEM_ConstraintRigidBody": {
                            "size": "small",
                            "text": "Rigid body constraint",
                            "icon": "FEM_ConstraintRigidBody",
                        },
                        "FEM_ConstraintDisplacement": {
                            "size": "small",
                            "text": "Displacement boundary condition",
                            "icon": "FEM_ConstraintDisplacement",
                        },
                        "FEM_ConstraintContact": {
                            "size": "small",
                            "text": "Contact constraint",
                            "icon": "FEM_ConstraintContact",
                        },
                        "FEM_ConstraintTie": {
                            "size": "small",
                            "text": "Tie constraint",
                            "icon": "FEM_ConstraintTie",
                        },
                        "FEM_ConstraintSpring": {
                            "size": "small",
                            "text": "Spring",
                            "icon": "FEM_ConstraintSpring",
                        },
                        "FEM_ConstraintForce": {
                            "size": "large",
                            "text": "Force load",
                            "icon": "FEM_ConstraintForce",
                        },
                        "FEM_ConstraintPressure": {
                            "size": "small",
                            "text": "Pressure load",
                            "icon": "FEM_ConstraintPressure",
                        },
                        "FEM_ConstraintCentrif": {
                            "size": "small",
                            "text": "Centrifugal load",
                            "icon": "FEM_ConstraintCentrif",
                        },
                        "FEM_ConstraintSelfWeight": {
                            "size": "small",
                            "text": "Gravity load",
                            "icon": "FEM_ConstraintSelfWeight",
                        },
                        "FEM_ConstraintInitialTemperature": {
                            "size": "small",
                            "text": "Initial temperature",
                            "icon": "FEM_ConstraintInitialTemperature",
                        },
                        "FEM_ConstraintHeatflux": {
                            "size": "small",
                            "text": "Heat flux load",
                            "icon": "FEM_ConstraintHeatflux",
                        },
                        "FEM_ConstraintTemperature": {
                            "size": "small",
                            "text": "Temperature boundary condition",
                            "icon": "FEM_ConstraintTemperature",
                        },
                        "FEM_ConstraintBodyHeatSource": {
                            "size": "small",
                            "text": "Body heat source",
                            "icon": "FEM_ConstraintBodyHeatSource",
                        },
                    },
                },
                "Structure": {
                    "order": [
                        "Create part",
                        "Create group",
                        "Link actions",
                        "Create a variable set",
                    ],
                    "commands": {
                        "Std_Part": {
                            "size": "small",
                            "text": "Create part",
                            "icon": "Geofeaturegroup",
                        },
                        "Std_Group": {
                            "size": "small",
                            "text": "Create group",
                            "icon": "folder",
                        },
                        "Std_LinkActions": {
                            "size": "small",
                            "text": "Link actions",
                            "icon": "",
                        },
                        "Std_VarSet": {
                            "size": "small",
                            "text": "Create a variable set",
                            "icon": "VarSet",
                        },
                    },
                },
            }
        },
        "TechDrawWorkbench": {
            "toolbars": {
                "TechDraw Pages": {
                    "order": [
                        "Insert Default Page",
                        "Insert Page using Template",
                        "Update template fields",
                        "Redraw Page",
                        "Print All Pages",
                    ],
                    "commands": {
                        "TechDraw_PageDefault": {
                            "size": "large",
                            "text": "Insert Default Page",
                            "icon": "actions/TechDraw_PageDefault",
                        }
                    },
                },
                "TechDraw Views": {
                    "order": [
                        "Insert View",
                        "Insert Broken View",
                        "Insert Active View (3D View)",
                        "Insert a simple or complex Section View",
                        "Insert Detail View",
                        "Insert Draft Workbench Object",
                        "Insert Clip Group",
                    ],
                    "commands": {
                        "TechDraw_View": {
                            "size": "large",
                            "text": "Insert View",
                            "icon": "actions/TechDraw_View",
                        }
                    },
                },
                "TechDraw Stacking": {
                    "order": ["Adjust stacking order of views"],
                    "commands": {
                        "TechDraw_StackGroup": {
                            "size": "large",
                            "text": "Adjust stacking order of views",
                            "icon": "",
                        }
                    },
                },
                "TechDraw Dimensions": {
                    "order": [
                        "Dimension",
                        "Insert Balloon Annotation",
                        "Axonometric length dimension",
                        "Insert Landmark Dimension - EXPERIMENTAL",
                        "Repair Dimension References",
                    ],
                    "commands": {
                        "TechDraw_CompDimensionTools": {
                            "size": "large",
                            "text": "Dimension",
                            "icon": "",
                        }
                    },
                },
                "TechDraw Attributes": {
                    "order": [
                        "Select Line Attributes, Cascade Spacing and Delta Distance",
                        "Change Line Attributes",
                        "Extend Line",
                        "Lock/Unlock View",
                        "Position Section View",
                        "Customize Format Label",
                    ],
                    "commands": {
                        "TechDraw_ExtensionSelectLineAttributes": {
                            "size": "large",
                            "text": "Select Line Attributes, Cascade Spacing and Delta Distance",
                            "icon": "TechDraw_ExtensionSelectLineAttributes",
                        }
                    },
                },
                "TechDraw Centerlines": {
                    "order": [
                        "Add Circle Centerlines",
                        "Add Cosmetic Thread Hole Side View",
                        "",
                        "Add Cosmetic Circle",
                        "Add Cosmetic Parallel Line",
                    ],
                    "commands": {
                        "TechDraw_ExtensionCircleCenterLinesGroup": {
                            "size": "large",
                            "text": "Add Circle Centerlines",
                            "icon": "",
                        }
                    },
                },
                "TechDraw Extend Dimensions": {
                    "order": ["Insert '\u2300' Prefix", "Increase Decimal Places"],
                    "commands": {
                        "TechDraw_ExtensionInsertPrefixGroup": {
                            "size": "large",
                            "text": "Insert '\u2300' Prefix",
                            "icon": "",
                        }
                    },
                },
                "TechDraw File Access": {
                    "order": ["Export Page as SVG", "Export Page as DXF"],
                    "commands": {
                        "TechDraw_ExportPageSVG": {
                            "size": "large",
                            "text": "Export Page as SVG",
                            "icon": "actions/TechDraw_ExportPageSVG",
                        }
                    },
                },
                "TechDraw Decoration": {
                    "order": [
                        "Hatch a Face using Image File",
                        "Apply Geometric Hatch to Face",
                        "Turn View Frames On/Off",
                    ],
                    "commands": {
                        "TechDraw_Hatch": {
                            "size": "large",
                            "text": "Hatch a Face using Image File",
                            "icon": "actions/TechDraw_Hatch",
                        }
                    },
                },
                "TechDraw Annotation": {
                    "order": [
                        "Insert Annotation",
                        "Add Leaderline to View",
                        "Insert Rich Text Annotation",
                        "Insert Cosmetic Vertex",
                        "Insert Center Line",
                        "Add Cosmetic Line Through 2 Points",
                        "Add Cosmetic Circle",
                        "Change Appearance of Lines",
                        "Show/Hide Invisible Edges",
                        "Add Welding Information to Leaderline",
                        "Create a Surface Finish Symbol",
                        "Add hole or shaft fit",
                    ],
                    "commands": {
                        "TechDraw_Annotation": {
                            "size": "large",
                            "text": "Insert Annotation",
                            "icon": "actions/TechDraw_Annotation",
                        }
                    },
                },
                "TitleBlock Toolbar": {
                    "order": [
                        "Populate titleblock",
                        "Import data from the FreeCAD source file",
                        "Import data from titleblock",
                    ],
                    "commands": {
                        "FillTitleBlock": {
                            "size": "large",
                            "text": "Populate titleblock",
                            "icon": "FillTitleBlock.svg",
                        }
                    },
                },
                "order": [
                    "Individual views",
                    "Structure",
                    "TechDraw Pages",
                    "TechDraw Views",
                    "TechDraw Dimensions_custom",
                    "TechDraw Stacking",
                    "TechDraw Attributes",
                    "TechDraw Centerlines",
                    "TechDraw File Access",
                    "TechDraw Decoration",
                    "TechDraw Annotation",
                    "TitleBlock Toolbar",
                    "Create BOM_custom",
                ],
                "Individual views": {
                    "order": [
                        "Isometric",
                        "Front",
                        "Top",
                        "Right",
                        "Rear",
                        "Bottom",
                        "Left",
                    ],
                    "commands": {
                        "Std_ViewIsometric": {
                            "size": "small",
                            "text": "Isometric",
                            "icon": "view-axonometric",
                        },
                        "Std_ViewFront": {
                            "size": "small",
                            "text": "Front",
                            "icon": "view-front",
                        },
                        "Std_ViewTop": {
                            "size": "small",
                            "text": "Top",
                            "icon": "view-top",
                        },
                        "Std_ViewRight": {
                            "size": "small",
                            "text": "Right",
                            "icon": "view-right",
                        },
                        "Std_ViewRear": {
                            "size": "small",
                            "text": "Rear",
                            "icon": "view-rear",
                        },
                        "Std_ViewBottom": {
                            "size": "small",
                            "text": "Bottom",
                            "icon": "view-bottom",
                        },
                        "Std_ViewLeft": {
                            "size": "small",
                            "text": "Left",
                            "icon": "view-left",
                        },
                    },
                },
            }
        },
    }
}

# a list to store replaced toolbars
List_IgnoredToolbars_internal = []


def main():
    CreateLists()
    CreateJson()
    WriteJson()


def CreateJson():
    # Add your custom workbenches
    if CustomJson_Workbenches != "" or CustomJson_Workbenches is not None:
        for Workbench in CustomJson_Workbenches["workbenches"]:
            skipWorkbenchList.append(Workbench)
        Dict_RibbonCommandPanel.update(CustomJson_Workbenches)

    # Go throug the workbenches
    for WorkbenchItem in List_Workbenches:
        WorkBenchName = WorkbenchItem[0]

        # Exclude the workbenches that you want to exclude
        WorkbenchToBeSkipped = False
        for WorkbenchToSkip in skipWorkbenchList:
            if WorkbenchToSkip == WorkBenchName:
                WorkbenchToBeSkipped = True
        # Exclude the workbenches that will be ignored in the RibbonBar
        for WorkbenchToSkip in List_IgnoredWorkbenches:
            if WorkbenchToSkip == WorkBenchName:
                WorkbenchToBeSkipped = True

        if WorkbenchToBeSkipped is False:
            # Activate the workbench. Otherwise, .listToolbars() returns empty
            Gui.activateWorkbench(WorkBenchName)
            # Get the toolbars of this workbench
            wbToolbars = Gui.getWorkbench(WorkBenchName).getToolbarItems()
            CustomCommands = Dict_ReturnCustomToolbars(WorkBenchName)
            wbToolbars.update(CustomCommands)
            CustomPanelCommands = Dict_AddCustomToolbarsToWorkbench(WorkBenchName)
            wbToolbars.update(CustomPanelCommands)

            # Go through the toolbars
            for key, value in wbToolbars.items():
                Toolbar = key

                # Exclude the toolbars that will be ignored in the RibbonBar
                ToolbarToBeSkipped = False
                for ignoredToolbar in List_IgnoredToolbars:
                    if ignoredToolbar == key:
                        ToolbarToBeSkipped = True
                # Exclude the toolbars that must have only small icons
                for ToolbarToSkip in smallOnlyToolbars:
                    if ToolbarToSkip == key:
                        ToolbarToBeSkipped = True

                if ToolbarToBeSkipped is False:
                    # create a empty size string
                    Size = "small"
                    # Defien empty strings for the command name and icon name
                    CommandName = ""
                    IconName = ""

                    for i2 in range(len(value)):
                        CommandName = value[i2]
                        Command = Gui.Command.get(CommandName)
                        if Command is not None:
                            IconName = Command.getInfo()["pixmap"]
                            MenuName = Command.getInfo()["menuText"].replace("&", "")

                            # Create an empty list for orders
                            Order = []
                            for i3 in range(len(value)):
                                CommandOrder = Gui.Command.get(value[i3])
                                if CommandOrder is not None:
                                    MenuNameOrder = CommandOrder.getInfo()[
                                        "menuText"
                                    ].replace("&", "")
                                    Order.append(MenuNameOrder)

                            # Set the first command to large
                            if i2 == 0:
                                Size = "large"

                                add_keys_nested_dict(
                                    Dict_RibbonCommandPanel,
                                    [
                                        "workbenches",
                                        WorkBenchName,
                                        "toolbars",
                                        Toolbar,
                                        "order",
                                    ],
                                )
                                add_keys_nested_dict(
                                    Dict_RibbonCommandPanel,
                                    [
                                        "workbenches",
                                        WorkBenchName,
                                        "toolbars",
                                        Toolbar,
                                        "commands",
                                        CommandName,
                                    ],
                                )

                                Dict_RibbonCommandPanel["workbenches"][WorkBenchName][
                                    "toolbars"
                                ][Toolbar]["order"] = Order
                                Dict_RibbonCommandPanel["workbenches"][WorkBenchName][
                                    "toolbars"
                                ][Toolbar]["commands"][CommandName] = {
                                    "size": Size,
                                    "text": MenuName,
                                    "icon": IconName,
                                }
                            if i2 > 0:
                                Size = "small"

                            i2 = i2 + 1
    return


def CreateLists():
    # Create a list of all workbenches with their icon
    List_Workbenches.clear()
    Workbenches = Gui.listWorkbenches()
    for WorkBenchName in Workbenches:
        if str(WorkBenchName) != "":
            if str(WorkBenchName) != "NoneWorkbench" or WorkBenchName is not None:
                Icon = None
                IconName = str(Gui.getWorkbench(WorkBenchName).Icon)
                if IconName != "":
                    Icon = Gui.getIcon(IconName)
                WorkbenchTitle = Gui.getWorkbench(WorkBenchName).MenuText
                List_Workbenches.append([str(WorkBenchName), Icon, WorkbenchTitle])

    # Create a list of all toolbars
    StringList_Toolbars.clear()
    # Store the current active workbench
    ActiveWB = Gui.activeWorkbench().name()
    # Go through the list of workbenches
    for workbench in List_Workbenches:
        # Activate the workbench. Otherwise, .listToolbars() returns empty
        Gui.activateWorkbench(workbench[0])
        # Get the toolbars of this workbench
        wbToolbars = Gui.getWorkbench(workbench[0]).listToolbars()
        # Go through the toolbars
        for Toolbar in wbToolbars:
            # Go through the list of toolbars. If already present, skip it.
            # Otherwise add it the the list.
            IsInList = False
            for i in range(len(StringList_Toolbars)):
                if Toolbar == StringList_Toolbars[i][0]:
                    IsInList = True

            if IsInList is False:
                StringList_Toolbars.append([Toolbar, workbench[2]])
    CustomToolbars = List_ReturnCustomToolbars()
    for Customtoolbar in CustomToolbars:
        StringList_Toolbars.append(Customtoolbar)
    # re-activate the workbench that was stored.
    Gui.activateWorkbench(ActiveWB)

    # Create a list of all commands with their icon
    List_Commands.clear()
    # Create a list of command names
    CommandNames = []
    for i in range(len(List_Workbenches)):
        WorkBench = Gui.getWorkbench(List_Workbenches[i][0])
        ToolbarItems = WorkBench.getToolbarItems()
        for key, value in ToolbarItems.items():
            for j in range(len(value)):
                Item = [value[j], List_Workbenches[i][0]]
                # if CommandNames.__contains__(Item) is False:
                IsInList = False
                for k in range(len(CommandNames)):
                    if CommandNames[k][0] == value[j]:
                        IsInList = True
                if IsInList is False:
                    CommandNames.append(Item)

    # Go through the list
    for CommandName in CommandNames:
        # get the command with this name
        command = Gui.Command.get(CommandName[0])
        WorkBenchName = CommandName[1]
        if command is not None:
            # get the icon for this command
            if command.getInfo()["pixmap"] != "":
                Icon = Gui.getIcon(command.getInfo()["pixmap"])
            else:
                Icon = None
            MenuName = command.getInfo()["menuText"].replace("&", "")
            List_Commands.append([CommandName[0], Icon, MenuName, WorkBenchName])
    # add also custom commands
    Toolbars = List_ReturnCustomToolbars()
    for Toolbar in Toolbars:
        WorkbenchTitle = Toolbar[1]
        for WorkBench in List_Workbenches:
            if WorkbenchTitle == WorkBench[2]:
                WorkBenchName = WorkBench[0]
                for CustomCommand in Toolbar[2]:
                    command = Gui.Command.get(CustomCommand)
                    if command.getInfo()["pixmap"] != "":
                        Icon = Gui.getIcon(command.getInfo()["pixmap"])
                    else:
                        Icon = None
                    MenuName = command.getInfo()["menuText"].replace("&", "")
                    List_Commands.append([CustomCommand, Icon, MenuName, WorkBenchName])
    # endregion ----------------------------------------------------------------------

    return


def WriteJson():
    # Create a resulting dict
    resultingDict = {}
    # add the various lists to the resulting dict.
    resultingDict["ignoredToolbars"] = List_IgnoredToolbars
    resultingDict["iconOnlyToolbars"] = List_IconOnlyToolbars
    resultingDict["quickAccessCommands"] = List_QuickAccessCommands
    resultingDict["ignoredWorkbenches"] = List_IgnoredWorkbenches
    resultingDict.update(Dict_CustomPanels)
    # Add the show text property to the dict
    resultingDict["showTextSmall"] = ShowText_Small
    resultingDict["showTextMedium"] = ShowText_Medium
    resultingDict["showTextLarge"] = ShowText_Large

    # RibbonTabs
    # Get the Ribbon dictionary
    resultingDict.update(Dict_RibbonCommandPanel)

    # get the path for the Json file
    JsonFile = os.path.join(JsonPath, JsonName)

    # Writing to sample.json
    with open(JsonFile, "w") as outfile:
        json.dump(resultingDict, outfile, indent=4)

    outfile.close()
    return


def add_keys_nested_dict(dict, keys):
    for key in keys:
        if key not in dict:
            dict[key] = {}
        dict = dict[key]
    try:
        dict.setdefault(keys[-1], 1)
    except Exception:
        pass
    return


def List_ReturnCustomToolbars():
    # Get the main window of FreeCAD
    mw = Gui.getMainWindow()
    Toolbars = []

    List_Workbenches = Gui.listWorkbenches().copy()
    for WorkBenchName in List_Workbenches:
        WorkbenchTitle = Gui.getWorkbench(WorkBenchName).MenuText
        if str(WorkBenchName) != "" or WorkBenchName is not None:
            if str(WorkBenchName) != "NoneWorkbench":
                CustomToolbars: list = App.ParamGet(
                    "User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar"
                ).GetGroups()

                for Group in CustomToolbars:
                    Parameter = App.ParamGet(
                        "User parameter:BaseApp/Workbench/"
                        + WorkBenchName
                        + "/Toolbar/"
                        + Group
                    )
                    Name = Parameter.GetString("Name")

                    ListCommands = []
                    # get list of all buttons in toolbar
                    TB = mw.findChildren(QToolBar, Name)
                    allButtons: list = TB[0].findChildren(QToolButton)
                    for button in allButtons:
                        if button.text() == "":
                            continue

                        action = button.defaultAction()
                        if action is not None:
                            Command = action.objectName()
                            ListCommands.append(Command)

                    Toolbars.append([Name, WorkbenchTitle, ListCommands])

    return Toolbars


def Dict_ReturnCustomToolbars(WorkBenchName):
    # Get the main window of FreeCAD
    mw = Gui.getMainWindow()
    Toolbars = {}

    if str(WorkBenchName) != "" or WorkBenchName is not None:
        if str(WorkBenchName) != "NoneWorkbench":
            CustomToolbars: list = App.ParamGet(
                "User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar"
            ).GetGroups()

            for Group in CustomToolbars:
                Parameter = App.ParamGet(
                    "User parameter:BaseApp/Workbench/"
                    + WorkBenchName
                    + "/Toolbar/"
                    + Group
                )
                Name = Parameter.GetString("Name")

                if Name != "":
                    ListCommands = []
                    # get list of all buttons in toolbar
                    TB = mw.findChildren(QToolBar, Name)
                    allButtons: list = TB[0].findChildren(QToolButton)
                    for button in allButtons:
                        if button.text() == "":
                            continue
                        action = button.defaultAction()
                        Command = action.objectName()
                        ListCommands.append(Command)

                        Toolbars[Name] = ListCommands

    return Toolbars


def Dict_AddCustomToolbarsToWorkbench(WorkBenchName):
    Toolbars = {}

    try:
        for CustomToolbar in Dict_CustomPanels["customToolbars"][WorkBenchName]:
            ListCommands = []
            Commands = Dict_CustomPanels["customToolbars"][WorkBenchName][
                CustomToolbar
            ]["commands"]

            for key, value in Commands.items():
                for i in range(len(List_Commands)):
                    if List_Commands[i][2] == key:
                        Command = List_Commands[i][0]
                        ListCommands.append(Command)

                if List_IgnoredToolbars_internal.__contains__(value) is False:
                    List_IgnoredToolbars_internal.append(value)

            Toolbars[CustomToolbar] = ListCommands
    except Exception:
        pass

    return Toolbars


main()
