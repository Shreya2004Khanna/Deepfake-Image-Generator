import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model
import os

#Initialize face detector and analysis model
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(640, 640))  # Better detection with larger size

#Load source and target images
src_img = cv2.imread("sat.jpg")
tgt_img = cv2.imread("target_face.png")

if src_img is None or tgt_img is None:
    print("One or both images not found.")
    exit()

#Detect faces
src_faces = app.get(src_img)
tgt_faces = app.get(tgt_img)

if not src_faces or not tgt_faces:
    print("No face detected in one or both images.")
    exit()

#Load the Swapper model
swapper = get_model("inswapper_128.onnx", root=".", download=False, providers=["CPUExecutionProvider"])

#Perform face swap with blending
src_face = src_faces[0]
result_img = tgt_img.copy()

for target_face in tgt_faces:
    result_img = swapper.get(result_img, target_face, src_face, paste_back=True)

#Save result
cv2.imwrite("deepfake_result.png", result_img)
print("Face swap complete. Saved as 'deepfake_result.png'")

