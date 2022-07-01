import pyscreeze as ps
import json as jsn
import os


def getControls(readFolder: str):
    # Walk the readFolder and get all the files
    files = []
    for root, dirs, files in os.walk(readFolder):
        files.append(files)
    files = files[:-1]
    files = [file
             for file in files if file.split(".")[1] in ["png", "jpg"]]

    output = {

    }
    for img in files:
        try:
            x = ps.locateCenterOnScreen(f"./{readFolder}/{img}")
            imgName = os.path.basename(img).split(".")[0]
            output.update({imgName: {"x": str(x[0]), "y": str(x[1])}})
        except:
            output.update({imgName: {"x": None, "y": None}})
            print(f"{imgName} not found")
    jsn.dump(output, open(f"{readFolder}/controls.json", "w"))
