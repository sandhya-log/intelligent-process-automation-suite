# from PIL import Image
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# def extract_text_from_file(file_path: str) -> str:
#     """
#     Extract text from an image file using Tesseract OCR.
#     """
#     try:
#         image = Image.open(file_path)
#         text = pytesseract.image_to_string(image)
#         return text.strip()
#     except Exception as e:
#         return f"OCR failed: {str(e)}"
from PIL import Image
import pytesseract


def extract_text_from_file(file_path: str) -> str:
    try:
        image = Image.open(file_path)

        # Convert to grayscale (improves OCR)
        gray_image = image.convert("L")

        text = pytesseract.image_to_string(gray_image)
        return text.strip()

    except Exception as e:
        return f"OCR failed: {str(e)}"
