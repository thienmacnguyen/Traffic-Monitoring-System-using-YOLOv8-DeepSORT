from PIL import Image 
import pytesseract
import re
import os
import cv2


muy = 0.8
g = 9.8
def extract_speed(text):
    """
    This function extracts speed from an OCR text string, handling recognition errors such as '0km/h' or '0km/h'. 
    It returns: int (number of km/h) or None if not found.
    """
    if not text:
        return None

    text = re.sub(r'\bO(?=km/h)', '0', text)  # 'Okm/h' → '0km/h'
    text = re.sub(r'\bQ(?=km/h)', '0', text)  # 'Qkm/h' → '0km/h'
    text = re.sub(r'\bB(?=km/h)', '8', text)  # 'Bkm/h' → '8km/h'

    text = re.sub(r'(\d)\s+km/h', r'\1km/h', text)
    match = re.search(r'\b(\d{1,3})km/h\b', text)
    if match:
        return int(match.group(1))
    else:
        return None
def get_speed(frame):
    xmin, ymin, xmax, ymax = 11, 1701, 2549, 1920
    roi = frame[ymin:ymax, xmin:xmax]
    pil_img = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    text = pytesseract.image_to_string(pil_img)
    speed = extract_speed(text)
    # print(f'Text of frame :{text},  Speed : {speed}')
    return speed

def safe_distance_estimation(frame):
    speed = get_speed(frame)
    safe_distance = speed**2/(2*muy*g)
    return speed, safe_distance
    
    
