# Geoguessr_encoder
This is a personal project where google streetview input data will be used to train a encoder what country the picture is taken in


## Dataset
- OSV-5M (train.csv): https://huggingface.co/datasets/osv5m/osv5m/blob/main/train.csv
- Place it at `datasets/train.csv` (the `datasets/` folder is not tracked by git).

## Model
- CLIP (ViT-B/32), loaded via Hugging Face `transformers`: https://huggingface.co/openai/clip-vit-base-patch32
- Place the files in `models/clip/` (the `models/` folder is not tracked by git).
