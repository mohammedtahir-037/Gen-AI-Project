import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from caption import generate_caption
from story import generate_story
import os

image_path = None

def upload_image():
    global image_path

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if file_path:
        image_path = file_path

        img = Image.open(image_path)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)

        panel.config(image=img)
        panel.image = img

        caption_label.config(text="Click Generate")
        story_label.config(text="")

def generate():
    if image_path is None:
        caption_label.config(text="Upload an image first!")
        return

    image = Image.open(image_path)

    caption = generate_caption(image)
    story = generate_story(caption)

    print("RAW STORY:", story)  # debug

    # 🔥 REMOVE unwanted text (Rules, Write, etc.)
    bad_words = ["rules", "write", "-", "only", "no repetition", "no violence"]

    clean_lines = []
    for line in story.split("\n"):
        if not any(bad in line.lower() for bad in bad_words):
            clean_lines.append(line.strip())

    story = " ".join(clean_lines).strip()

    # 🔥 Remove repetition
    sentences = story.split(".")
    unique = []
    for s in sentences:
        s = s.strip()
        if s and s not in unique:
            unique.append(s)

    story = ". ".join(unique) + "."

    # 🔥 fallback if still bad
    if not story or len(story.split()) < 10:
        story = f"{caption}. The scene looks calm and natural. It is a simple and peaceful moment."

    # ✅ DISPLAY ONLY CLEAN OUTPUT
    caption_label.config(text=f"Caption: {caption}")
    story_label.config(text=f"Story: {story}")

    save_output(caption, story)
        
def save_output(caption, story):
    os.makedirs("output", exist_ok=True)

    with open("output/stories.txt", "a", encoding="utf-8") as f:
        f.write("Caption: " + caption + "\n")
        f.write("Story: " + story + "\n")
        f.write("-" * 50 + "\n")

# GUI
root = tk.Tk()
root.title("AI Image Story Generator")
root.geometry("500x650")

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

panel = tk.Label(root)
panel.pack()

generate_btn = tk.Button(root, text="Generate Caption + Story", command=generate)
generate_btn.pack(pady=10)

caption_label = tk.Label(root, text="", wraplength=450, justify="center", fg="blue")
caption_label.pack(pady=10)

story_label = tk.Label(root, text="", wraplength=450, justify="center", fg="green")
story_label.pack(pady=10)

root.mainloop()