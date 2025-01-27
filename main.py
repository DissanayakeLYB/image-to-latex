import cv2
import pytesseract
from flask import Flask, request, jsonify

# Set the path to Tesseract executable file 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # For Windows

# Image preprocessing
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

# Extract text using OCR
def extract_text(image):
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

# Clean extracted text
def clean_text(text):
    cleaned_text = text.replace('\n', ' ').strip()
    return cleaned_text

# Convert text to LaTeX
def convert_to_latex(text):
    latex_code = f"\\[ {text} \\]"
    return latex_code

def output(image_path):
    preprocessed_image = preprocess_image(image_path)
    text = extract_text(preprocessed_image)
    cleaned_text = clean_text(text)
    latex_code = convert_to_latex(cleaned_text)

    print("Extracted Text:", cleaned_text)
    print("LaTeX Code:", latex_code)

if __name__ == '__main__':
    image_path = "test_image.png" 
    output(image_path)
    