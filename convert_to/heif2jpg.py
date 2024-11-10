"""
This python script reads the HEIC images (Iphone pictures) and converts it into jpeg format for easier usages in the machine learning frameworks. 
Owner: Suprim Nakarmi
Date created: April, 2024

"""

from PIL import Image
from pillow_heif import register_heif_opener
import time
import os 
import glob 
from concurrent.futures import ThreadPoolExecutor


file_path= "/Users/suprimnakarmi/projects/ocr_reports/dataset/"
dest_path = "/Users/suprimnakarmi/projects/ocr_reports/"


def conversion(file:str, dest_path:str):
    '''
    converts the HEIC images to Jpeg

    params
        file: Complete path of the file (image)
        dest_path: Complete path to saved the coverted images
    '''
    image_name = file.split("/")[-1]
    index_dot = image_name.find(".")
    file_name = image_name[:index_dot]
    try:
        image = Image.open(f"/Users/suprimnakarmi/projects/ocr_reports/dataset/{file_name}.HEIC")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_name}.HEIC' does not exist.")
    except IOError as e: 
        raise IOError(f"An error occurred while trying to open the file '{file_name}.HEIC': {str(e)}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while processing '{file_name}.HEIC: {str(e)}")
    image.save(os.path.join(dest_path,file_name + ".jpg"), format='jpeg')


def heif_to_jpeg(file_path:str, dest_path:str):
    '''
    Use multithreading to write the jpeg file

    params
        file_path: complete path of the source files
        dest_path: Complete path to saved the coverted images
    '''
    all_file_names = glob.glob(file_path + "*.HEIC")
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(conversion,all_file_names,[dest_path] * len(all_file_names))

start_time = time.perf_counter()
register_heif_opener()
heif_to_jpeg(file_path, dest_path)
end_time = time.perf_counter()
time_taken = end_time - start_time
print(f"Time taken for conversion: {time_taken}")


'''
Experimentations:
Image size: 85 
Execution time (without multithreading): 24.43 seconds
Execution time (with multithreading): 10.23 seconds

Concurrent multithreading was used for its automatic allocation of threads to process. 
'''