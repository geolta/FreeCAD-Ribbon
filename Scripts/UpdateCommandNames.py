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

# This script can be used to update "RibbonStructure.json" with modified command text from CommandList.json.


import FreeCAD as App
import FreeCADGui as Gui
import os
import json

ParentPath = os.path.dirname(os.path.dirname(__file__))

# Set the path where you want to save this new Json file
# JsonPath = os.path.dirname(__file__)
JsonPath = ParentPath

# Set the file name. Default is "CommandList.json".
# This is the file used to reset the ribbon.
JsonName = "RibbonStructure_update.json"

# Define list of the workbenches, toolbars and commands on class level
List_Workbenches = []
Dict_Commands = {}
Dict_RibbonCommandPanel = {}


def main():
    ReadJson()
    ReadCommands()
    UpdateCommands()
    WriteJson()


def ReadJson():
    """Read the Json file and fill the lists and set settings"""
    # Open the JsonFile and load the data
    JsonFile = open(os.path.join(JsonPath, "RibbonStructure.json"))
    data = json.load(JsonFile)

    # Get the dict with the customized date for the buttons
    try:
        Dict_RibbonCommandPanel["workbenches"] = data["workbenches"]
    except Exception as e:
        print(e)
        pass

    JsonFile.close()
    return


def ReadCommands():
    """Read the Json file and fill the lists and set settings"""
    # Open the JsonFile and load the data
    JsonFile = open(os.path.join(JsonPath, "CommandList.json"))
    data = json.load(JsonFile)

    # Get the dict with the customized date for the buttons
    try:
        Dict_Commands.update(data)
    except Exception as e:
        print(e)
        pass

    JsonFile.close()
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


def UpdateCommands():
    for WorkBench in Dict_RibbonCommandPanel["workbenches"]:
        for ToolBar in Dict_RibbonCommandPanel["workbenches"][WorkBench]["toolbars"]:
            if ToolBar != "order":
                for Command in Dict_RibbonCommandPanel["workbenches"][WorkBench]["toolbars"][ToolBar]["commands"]:
                    for key, value in Dict_Commands.items():
                        if Command == key:
                            if value[2] != "" and value[2] != "...":
                                Dict_RibbonCommandPanel["workbenches"][WorkBench]["toolbars"][ToolBar]["commands"][
                                    Command
                                ]["text"] = value[2]


def WriteJson():
    # Open the JsonFile and load the data
    JsonFile = open(os.path.join(JsonPath, "RibbonStructure.json"))
    data = json.load(JsonFile)

    # RibbonTabs
    # Get the Ribbon dictionary
    data.update(Dict_RibbonCommandPanel)

    # get the path for the Json file
    JsonFile = os.path.join(JsonPath, JsonName)

    # Writing to sample.json
    with open(JsonFile, "w") as outfile:
        json.dump(data, outfile, indent=4)

    outfile.close()
    return


main()
