from ultralytics import YOLO
from roboflow import Roboflow


#

rf = Roboflow(api_key="fOZILjlQev0ueprArURg")  # paste your key here
project = rf.workspace("cctv-vj8gz").project("human-cctv-aljry")
dataset = project.version(1).download("yolov8")


model = YOLO("yolov8n.pt")  


model.train(
    data=dataset.location + "/data.yaml", 
    epochs=50,       
    imgsz=640,      
    batch=16,       
    workers=2       
)

