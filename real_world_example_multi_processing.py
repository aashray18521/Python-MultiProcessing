import concurrent.futures
import time
from PIL import Image, ImageFilter
from torch import multiprocessing


img_names = [
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
    "https://images.unsplash.com/photo-1532009324734-20a7a5813719",
    "https://images.unsplash.com/photo-1524429656589-6633a470097c",
    "https://images.unsplash.com/photo-1530224264768-7ff8c1789d79",
    "https://images.unsplash.com/photo-1564135624576-c5c88640f235",
    "https://images.unsplash.com/photo-1541698444083-023c97d3f4b6",
    "https://images.unsplash.com/photo-1522364723953-452d3431c267",
    # "https://images.unsplash.com/photo-1513938709626-033611b8cc03",
    # "https://images.unsplash.com/photo-1507143550189-fed454f93097",
    "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e",
    "https://images.unsplash.com/photo-1504198453319-5ce911bafcde",
    "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99",
    "https://images.unsplash.com/photo-1516972810927-80185027ca84",
    "https://images.unsplash.com/photo-1550439062-609e1531270e",
    "https://images.unsplash.com/photo-1549692520-acc6669e2f0c",
]

start = time.perf_counter()

size = (1200, 1200)

img_names = [img.split("/")[-1] + ".jpg" for img in img_names]
print(img_names)


def process_img(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f"processed/{img_name}")
    print(f"{img_name} was processed...")


if __name__ == "__main__":
    multiprocessing.freeze_support()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_img, img_names)


end = time.perf_counter()

print(f"Time taken : {round(end-start, 3)} second(s)")
