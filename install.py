import torch
from PIL import Image
from transformers import AutoProcessor, CLIPVisionModelWithProjection

# Hier haal je het model op
processor = AutoProcessor.from_pretrained("./models/clip", local_files_only=True)

# Hier haal je de encoder op
encoder = CLIPVisionModelWithProjection.from_pretrained("./models/clip", local_files_only=True)

# Hier zet je het model in evaluatie modus. Hierdoor kan je de weights niet veranderen als je een foto erin zet
encoder.eval()

image = Image.open("test_photos/profile_pic.jpeg").convert("RGB")   # Waarschijnlijk was die al RGB
inputs = processor(images=image, return_tensors="pt")

with torch.inference_mode():
    features = encoder(**inputs).image_embeds

print("Vorm:", features.shape)
print("Eerste 10 features:", features[0, :10])