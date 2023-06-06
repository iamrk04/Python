# thumbnail_maker.py
import time
import os
import threading
from urllib.parse import urlparse
from urllib.request import urlretrieve
import PIL
from PIL import Image
from queue import Queue
from threading import Thread

from logger import get_logger


CURR_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
logger = get_logger(
    __name__,
    log_file_path=os.path.join(CURR_FILE_DIR, "log.txt"),
    format="%(threadName)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

class ThumbnailMakerService(object):
    def __init__(self, home_dir=CURR_FILE_DIR):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.downloaded_bytes = 0
        self.dl_lock = threading.Lock()
    
    # target function for the worker threads
    def download_image(self, url):
        # download each image and save to the input dir 
        logger.info("downloading image at URL " + url)
        img_filename = urlparse(url).path.split('/')[-1]
        dest_path = self.input_dir + os.path.sep + img_filename
        urlretrieve(url, self.input_dir + os.path.sep + img_filename)
        with self.dl_lock:
            self.downloaded_bytes += os.path.getsize(dest_path)

    def download_images(self, img_url_list):
        # validate inputs
        if not img_url_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)
        
        logger.info("beginning image downloads")
        threads = []

        start = time.perf_counter()
        for url in img_url_list:
            # create a thread for each url and put it in ready-to-run state
            t = threading.Thread(target=self.download_image, args=(url,))
            threads.append(t)
            t.start()
        # let main thread wait for all worker threads to finish
        # required because we want all images to be downloaded before we resize them
        for t in threads:
            t.join()
        end = time.perf_counter()

        logger.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self):
        # validate inputs
        if not os.listdir(self.input_dir):
            return
        os.makedirs(self.output_dir, exist_ok=True)

        logger.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        for filename in os.listdir(self.input_dir):
            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                
                # save the resized image to the output dir with a modified file name 
                new_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
        end = time.perf_counter()

        logger.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logger.info("START make_thumbnails")
        start = time.perf_counter()

        self.download_images(img_url_list)
        self.perform_resizing()

        end = time.perf_counter()
        logger.info(f"Total downloaded bytes: {self.downloaded_bytes}")
        logger.info("END make_thumbnails in {} seconds".format(end - start))
    