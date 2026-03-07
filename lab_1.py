from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # downloads model on first run

source = r"0"  # change to image, video, or 0 for webcam

if source.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
    model.predict(source=source, conf=0.35, show=True, save=True)
else:
    model.track(source=source, tracker="bytetrack.yaml", conf=0.35, show=True, save=True)

print("Done. Check runs/ folder.")