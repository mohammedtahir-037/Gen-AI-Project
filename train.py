import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from torch.utils.data import Dataset, DataLoader
import os

# =========================
# Load Pretrained Model
# =========================
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# =========================
# Custom Dataset
# =========================
class ImageCaptionDataset(Dataset):
    def __init__(self, image_folder, caption_file):
        self.image_folder = image_folder
        self.data = []

        with open(caption_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",", 1)
                if len(parts) != 2:
                    continue

                img, caption = parts
                img_path = os.path.join(image_folder, img)

                # Skip missing images
                if os.path.exists(img_path):
                    self.data.append((img, caption))
        
        print(f"✅ Loaded {len(self.data)} valid samples")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name, caption = self.data[idx]
        image_path = os.path.join(self.image_folder, img_name)

        try:
            image = Image.open(image_path).convert("RGB")
        except:
            # fallback in case of corrupt image
            image = Image.new("RGB", (224, 224))

        inputs = processor(
            image,
            caption,
            return_tensors="pt",
            padding="max_length",     # ✅ FIXED
            truncation=True,          # ✅ FIXED
            max_length=50
        )

        return {
            "pixel_values": inputs["pixel_values"].squeeze(0),
            "input_ids": inputs["input_ids"].squeeze(0),
            "attention_mask": inputs["attention_mask"].squeeze(0)
        }

# =========================
# Load Dataset
# =========================
dataset = ImageCaptionDataset("data/images", "data/cleaned_captions.txt")

loader = DataLoader(
    dataset,
    batch_size=4,        # increase if RAM allows
    shuffle=True
)

# =========================
# Training Setup
# =========================
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

# =========================
# Training Loop
# =========================
EPOCHS = 3

for epoch in range(EPOCHS):
    model.train()
    total_loss = 0

    for batch_idx, batch in enumerate(loader):
        pixel_values = batch["pixel_values"].to(device)
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        outputs = model(
            pixel_values=pixel_values,
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=input_ids
        )

        loss = outputs.loss

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        total_loss += loss.item()

        # Print progress
        if batch_idx % 10 == 0:
            print(f"Epoch {epoch+1} | Batch {batch_idx} | Loss: {loss.item():.4f}")

    print(f"✅ Epoch {epoch+1} Completed | Total Loss: {total_loss:.4f}")

# =========================
# Save Model
# =========================
model.save_pretrained("model")
processor.save_pretrained("model")

print("🎉 Training completed successfully!")
print("📁 Model saved in /model folder")