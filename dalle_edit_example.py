from dotenv import load_dotenv
import os
from openai import OpenAI
from PIL import Image
import requests

# Load environment variables from .env file
load_dotenv()


# Get API Key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not set in environment variables.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Your existing code...
image_dir = os.path.join(os.curdir, "images")
os.makedirs(image_dir, exist_ok=True)

input_image_filepath = os.path.join(os.curdir, "img.png")
if not os.path.isfile(input_image_filepath):
    raise FileNotFoundError(f"No se encontró la imagen en {input_image_filepath}")

input_img = Image.open(input_image_filepath)
width, height = input_img.size
if width != height or width != 1024:
    input_img = input_img.resize((1024, 1024))
    input_image_filepath = os.path.join(os.curdir, "resized_img.png")
    input_img.save(input_image_filepath)

mask = Image.new("RGBA", (1024, 1024), (0, 0, 0, 255))
for x in range(1024):
    for y in range(512, 1024):
        mask.putpixel((x, y), (0, 0, 0, 0))

mask_filepath = os.path.join(image_dir, "mask.png")
mask.save(mask_filepath)

with open("./prompts/prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read().strip()

edit_response = client.images.edit(
    image=open(input_image_filepath, "rb"),
    mask=open(mask_filepath, "rb"),
    prompt=prompt,
    n=1,
    size="1024x1024",
    response_format="url"
)

edited_image_url = edit_response.data[0].url
edited_image_path = os.path.join(image_dir, "edited_image.png")

image_data = requests.get(edited_image_url).content
with open(edited_image_path, "wb") as f:
    f.write(image_data)

print("Imagen generada guardada en:", edited_image_path)
Image.open(edited_image_path).show()
