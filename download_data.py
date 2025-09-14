

from roboflow import Roboflow
rf = Roboflow(api_key="fOZILjlQev0ueprArURg")
project = rf.workspace("cctv-vj8gz").project("human-cctv-aljry")
version = project.version(1)
dataset = version.download("yolov8")
                