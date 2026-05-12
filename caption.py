from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import random

# Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt").to(device)

    # 🔥 Force randomness EVERY time
    seed = random.randint(0, 10000)
    torch.manual_seed(seed)

    outputs = model.generate(
        **inputs,
        max_length=30,
        do_sample=True,        # ✅ VERY IMPORTANT
        top_k=50,
        top_p=0.9,
        temperature=0.9,
        num_return_sequences=1
    )

    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption