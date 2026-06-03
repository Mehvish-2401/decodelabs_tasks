
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
import os
import time
from langdetect import detect

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

def preprocess_image(image):
    """Improve image quality for OCR."""
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    image = image.filter(ImageFilter.SHARPEN)
    return image

def extract_text(image_path):
    """Extract text from image."""
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return None

    print(f"\nProcessing: {image_path}")

    start_time = time.time()

    image = Image.open(image_path)
    processed = preprocess_image(image)

    text = pytesseract.image_to_string(processed).strip()

    data = pytesseract.image_to_data(
        processed,
        output_type=pytesseract.Output.DICT
    )

    confidences = [
        int(c)
        for c in data['conf']
        if str(c).isdigit() and int(c) != -1
    ]

    avg_confidence = (
        round(sum(confidences) / len(confidences), 2)
        if confidences else 0
    )

    processing_time = round(time.time() - start_time, 2)

    return text, avg_confidence, processing_time

def detect_language(text):
    """Detect language."""
    try:
        return detect(text)
    except:
        return "unknown"

def save_output(image_path, text, confidence,
                language, word_count, processing_time):

    base_name = os.path.splitext(image_path)[0]
    output_path = f"{base_name}_output.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("OCR TEXT EXTRACTION REPORT\n")
        f.write("=" * 40 + "\n")
        f.write(f"Source Image   : {image_path}\n")
        f.write(f"Language       : {language}\n")
        f.write(f"Confidence     : {confidence}%\n")
        f.write(f"Word Count     : {word_count}\n")
        f.write(f"Processing Time: {processing_time} sec\n")
        f.write("-" * 40 + "\n")
        f.write(text)

    print(f"\nOutput saved to: {output_path}")

print("=" * 45)
print(" SMART OCR TEXT EXTRACTOR ")
print("=" * 45)

while True:

    image_path = input(
        "\nEnter image filename (e.g. sample_image.png): "
    ).strip()

    result = extract_text(image_path)

    if result is None:
        print("Skipping this image.")
    else:

        text, confidence, processing_time = result

        word_count = len(text.split())
        language = detect_language(text)

        print("\nDetected Text:")
        print("-" * 45)
        print(text if text else "No text detected.")
        print("-" * 45)

        print("\nSCAN SUMMARY")
        print("=" * 45)
        print(f"Word Count      : {word_count}")
        print(f"Confidence      : {confidence}%")
        print(f"Language        : {language}")
        print(f"Processing Time : {processing_time} sec")

        save_output(
            image_path,
            text,
            confidence,
            language,
            word_count,
            processing_time
        )

    again = input("\nScan another image? (y/n): ").strip().lower()

    if again != "y":
        print("\nThank you for using Smart OCR Text Extractor!")
        break

