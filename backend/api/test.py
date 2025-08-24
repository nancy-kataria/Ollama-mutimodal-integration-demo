from transformers import pipeline
from dotenv import load_dotenv
import os
import torch

class ImageTextToTextGenerator:
    def __init__(self, model_path):
        self.model_path=model_path
        self.pipe=None

    def load_model(self):
        
        try:
            self.pipe = pipeline(
                "image-text-to-text",
                model=self.model_path,
                device="cpu",
                torch_dtype=torch.bfloat16,
            )
            print("Model loaded successfully.")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            self.pipe = None
            return False

    def generate(self, messages):
        output = self.pipe(text=messages, max_new_tokens=200)
        print(output[0]["generated_text"][-1]["content"])


if __name__ == "__main__":
    load_dotenv()
    MODEL_PATH = os.getenv("LITE_RT_MODEL_PATH")
    Model = ImageTextToTextGenerator(MODEL_PATH)

    if Model.load_model():
        message_1 = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": os.getenv("PHOTO_PATH")},
                    {"type": "text", "text": "What animal is on the candy?"}
                ]
            }
        ]

        message_2 = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What should you do if you are in a car crash on a highway?"}
                ]
            }
        ]

        Model.generate(message_1)
        Model.generate(message_2)
    else:
        print("Model failed to load. Exiting.")
