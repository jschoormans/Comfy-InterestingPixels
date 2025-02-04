import io
from dotenv import load_dotenv
from torchvision.transforms import ToPILImage
import logging
import requests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env
load_dotenv()

class Slider:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image1": ("IMAGE", {}),
                "image2": ("IMAGE", {}),
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_url"
    CATEGORY = "ImageSlider"
    OUTPUT_NODE = True
    


    def convert_tensor_to_image(self, tensor):
        # Assumes tensor is a torch.Tensor; otherwise, returns input as is.
        try:
            # Handle 4D tensor (batch, height, width, channels) by taking first image
            if len(tensor.shape) == 4:
                tensor = tensor[0]
            # Convert from HWC to CHW format expected by ToPILImage
            tensor = tensor.permute(2, 0, 1)
            to_pil = ToPILImage()
            image = to_pil(tensor.cpu().detach())
            return image
        except Exception as e:
            logger.error("Conversion failed: %s", e)
            return tensor



    def upload_via_gcf(self, image):
        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Endpoint URL for Google Cloud Function
        url = "https://us-central1-redecorely.cloudfunctions.net/upload-interesting-pixels"

        # Send POST request with the image file
        files = {'image': ('image.png', img_byte_arr.getvalue(), 'image/png')}
        response = requests.post(url, files=files)

        if response.status_code != 200:
            logger.error("Upload failed with status code: %s", response.status_code)
            raise Exception(f"Upload failed: {response.text}")

        return response.json()['url']
    



    def generate_url(self, image1, image2):
        logger.info("Uploading images to S3")
        # Convert images if they are tensors
        image1 = self.convert_tensor_to_image(image1)
        image2 = self.convert_tensor_to_image(image2)
        url1 = self.upload_via_gcf(image1)
        url2 = self.upload_via_gcf(image2)
        # Create a clickable link (if supported by the UI)
        full_url = f'https://image-slider.interestingpixels.com?url1={url1}&url2={url2}'
        logger.info("Generated URL: %s", full_url)
        return {"ui": {"text": full_url}, "result": (full_url,)}


NODE_CLASS_MAPPINGS = {
    "slider": Slider
}

NODE_DISPLAY_NAMES_MAPPINGS = {
    "slider": "Image Slider Generation (new)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAMES_MAPPINGS']
