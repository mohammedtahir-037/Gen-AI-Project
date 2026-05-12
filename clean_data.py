# clean_data.py

cleaned = {}

with open("data/captions.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",", 1)
        if len(parts) != 2:
            continue

        img, caption = parts
        caption = caption.replace('"', '').replace(" .", ".").replace(" ,", ",")

        # keep first caption only (simple method)
        if img not in cleaned:
            cleaned[img] = caption

with open("cleaned_captions.txt", "w") as f:
    for img, cap in cleaned.items():
        f.write(f"{img},{cap}\n")

print("✅ Cleaned dataset ready")