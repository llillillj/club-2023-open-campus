import cv2
import os
from tqdm import tqdm
current_path = os.path.dirname(os.path.abspath(__file__))
def convert_to_grayscale(image_path):
    print(image_path)
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(image_path, gray_image)

def convert_folder_images_to_grayscale(folder_path):
    file_list = os.listdir(os.path.join(current_path, folder_path))
    for file in tqdm(file_list):
        file_path = os.path.join(folder_path, file)
        convert_to_grayscale(file_path)
