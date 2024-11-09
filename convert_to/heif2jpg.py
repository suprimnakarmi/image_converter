from PIL import Image
from pillow_heif import register_heif_opener
import time
import os 
import glob 
from concurrent.futures import ThreadPoolExecutor


file_path= "/Users/suprimnakarmi/projects/ocr_reports/dataset/"
all_file_names = glob.glob(file_path + "*.HEIC")
start_time = time.perf_counter()
register_heif_opener()

def heif_to_jpeg(file):
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
    image.save(os.path.join("/Users/suprimnakarmi/projects/ocr_reports/",file_name + ".jpg"), format='jpeg')


with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(heif_to_jpeg,all_file_names)

end_time = time.perf_counter()
time_taken = end_time - start_time
print(f"Time taken for conversion: {time_taken}")