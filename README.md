# 🔁 Deepfake Face Swapper using InsightFace

This project is a simple face-swapping tool powered by [InsightFace](https://github.com/deepinsight/insightface). It detects faces in two images and swaps the source face onto the target image.

---

## 📸 Example Use Case

Swap a celebrity face onto another person's body, or just experiment with facial transformations using static images.

---

## 📁 Folder Structure

deepfake_generator/ ├── generator.py # Main face-swapping script ├── sat.jpg # Source face image ├── target_face.png # Target image where face is swapped └── README.md # Project documentation

yaml


---

## 📦 Requirements

Make sure you have Python 3.8+ installed.

Install the dependencies:

```bash
pip install insightface opencv-python
You might also need onnxruntime if not already installed:

bash

pip install onnxruntime

🚀 How to Run
Clone the repository (or navigate to the folder):

Make sure sat.jpg and target_face.png exist in the same folder.

Run the script:

bash

python generator.py
After successful execution, the output image will be displayed or saved (you can add saving logic if needed).

⚠️ Notes
This script uses the buffalo_l model from InsightFace which works well on CPU.

Make sure both images contain clear, front-facing faces for the best result.

For custom images, replace sat.jpg and target_face.png with your own.

📄 License
This project is for educational and research purposes only. Use responsibly.
