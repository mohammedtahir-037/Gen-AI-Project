# 🧠 AI-Based Image Captioning and Story Generation System

## 📌 Project Overview
This project is an AI-based system that generates captions and meaningful short stories from input images using deep learning models. It combines computer vision and natural language processing techniques.

---

## 🚀 Features
- Upload an image
- Generate caption using AI
- Generate story based on caption
- Save output to file
- Works offline (no API)

---

## 🛠️ Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- Pillow (PIL)
- Tkinter (GUI)
- Matplotlib

---

## 💻 Software Requirements

Make sure the following software is installed:

### 🖥️ 1. Python
- Version: **3.8 – 3.10 recommended**

---

### 🧪 2. Anaconda (Optional but Recommended)
- For environment management

---

### 🧑‍💻 3. Code Editor
- Visual Studio Code (recommended)
- OR PyCharm

---

### 🌐 4. Git (Optional)
- For version control and GitHub upload

---

### 📦 5. Required Python Libraries

Install using:
pip install torch torchvision transformers pillow matplotlib

## 🤖 Models Used

### 1. Image Captioning
- BLIP (Bootstrapping Language-Image Pre-training)
- Pre-trained model: `Salesforce/blip-image-captioning-base`
- Fine-tuned on custom dataset (optional)

### 2. Story Generation
- FLAN-T5 (Instruction-tuned language model)
- Used for generating short meaningful stories

---

## 🏗️ System Architecture


Image → BLIP Model → Caption → FLAN-T5 → Story → GUI Display → Save Output


---

## 📂 Project Structure


image_story_ai/
│
├── data/
│ ├── images/
│ └── cleaned_captions.txt
│
├── output/
│ └── stories.txt
│
├── train.py
├── generate_and_save
├── caption.py
├── story.py
├── app.py
├── plot_graph.py
└── README.md


---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/your-username/image_story_ai.git

cd image_story_ai


### 2. Create environment (optional)

conda create -n blip_env python=3.10
conda activate blip_env


### 3. Install dependencies

pip install torch torchvision transformers pillow matplotlib


---

## ▶️ Run the Application

### Tkinter App:

python app.py


### Streamlit (optional):

streamlit run app.py


---

## 🧪 Training the Model


python train.py


### Generate Training Graph

python plot_graph.py


---

## 📊 Output

- Caption and story are displayed in the GUI
- Saved in:

output/stories.txt


---

## ⚠️ Challenges Faced

- Repetition in generated text
- Prompt echo issues ("Rules" appearing)
- Caption inaccuracies
- Model hallucination

---

## ✅ Solutions

- Simplified prompts
- Post-processing to remove repetition
- Filtering unwanted text
- Added fallback logic

---

## 🎯 Applications

- Assistive technology
- Content creation
- Image understanding systems
- AI storytelling

---

## 🚀 Future Enhancements

- Improve caption accuracy
- Add multiple story styles (fantasy, emotional)
- Use advanced models (Mistral, LLaMA)
- Web-based interface

---

## 💬 Conclusion

This project demonstrates how AI models can bridge the gap between visual understanding and natural language generation. It successfully generates captions and meaningful stories from images using offline models.

---

## 👩‍💻 Author
Hemalatha Reddy

---

## ⭐ If you like this project
Give it a star ⭐ on GitHub!
