import cv2
import pytesseract

# Ensure you have Tesseract-OCR installed and specify its path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to enhance text visibility
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Use Tesseract to extract text
    text = pytesseract.image_to_string(thresh, lang='eng')
    
    return text

# Provide the path to your image
image_path = "path_to_book_spine_image.jpg"
extracted_text = extract_text_from_image(image_path)

# Display the extracted text
print("Extracted Text:\n", extracted_text)

# You can later process 'extracted_text' to separate the title and author
