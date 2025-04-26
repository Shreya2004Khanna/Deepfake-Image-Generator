
# Deepfake Face Swapper (InsightFace)

A simple face-swapping tool using [InsightFace](https://github.com/deepinsight/insightface).  
Detects faces in a source and target image, then replaces the target face with the source.

## 🔧 Requirements

Install dependencies (also add these to your root `requirements.txt`):

--bash
pip install insightface opencv-python


📂 File Structure
bash

deepfake_generator/
├── generator.py         # Face-swap script
├── sat.jpg              # Sample source image
├── target_face.png      # Sample target image
└── README.md            # This file


🚀 Usage
Place your source and target images in this folder (default names: sat.jpg, target_face.png).

Run the script:
bash
python generator.py

The swapped result will be saved as deepfake_result.png in the same folder.


🧠 Model
Uses the buffalo_l model pack from InsightFace for face detection and embeddings.

CPU only (no GPU needed).



✏️ Notes
Best results with clear, frontal faces.

If you rename your input images, update the filenames in generator.py.

Enjoy your face-swap! 🚀
