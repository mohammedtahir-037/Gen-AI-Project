from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


def generate_story(caption):
    caption = caption.strip().lower()

    # ✅ VERY SIMPLE PROMPT (NO RULES AT ALL)
    prompt = f"Describe this image in 3 sentences: {caption}"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)

    outputs = model.generate(
    **inputs,
    max_new_tokens=80,
    do_sample=True,     # 🔥 add this
    temperature=0.8,
    top_p=0.9
)

    story = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # 🔥 HARD REMOVE RULES IF ANY
    if "rules" in story.lower():
        story = ""

    # 🔥 fallback if bad
    if not story or len(story.split()) < 10:
        return (
            f"{caption.capitalize()} is shown in a natural setting. "
            f"The scene looks calm and peaceful. "
            f"It captures a simple moment."
        )

    return story