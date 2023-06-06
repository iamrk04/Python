# thumbnail_maker.py
import time
import os
import multiprocessing
from urllib.parse import urlparse
from urllib.request import urlretrieve
import PIL
from PIL import Image
from queue import Queue
from threading import Thread

from logger import get_logger


CURR_FILE_DIR = os.path.dirname(os.path.abspath(__file__))

class ThumbnailMakerService(object):
    def __init__(self, home_dir=CURR_FILE_DIR):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_list = []
        self.logger = get_logger(
            __name__,
            log_file_path=os.path.join(CURR_FILE_DIR, "log.txt"),
            format="%(threadName)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    
    def download_image(self, dl_queue):
        while not dl_queue.empty():
            try:
                url = dl_queue.get(block=False)
                img_filename = urlparse(url).path.split('/')[-1]
                urlretrieve(url, self.input_dir + os.path.sep + img_filename)
                self.img_list.append(img_filename)
                dl_queue.task_done()
            except Queue.Empty:
                return
    
    # def download_images(self, img_url_list):
    #     # validate inputs
    #     if not img_url_list:
    #         return
    #     os.makedirs(self.input_dir, exist_ok=True)
        
    #     logger.info("beginning image downloads")

    #     start = time.perf_counter()
    #     for url in img_url_list:
    #         img_filename = urlparse(url).path.split('/')[-1]
    #         urlretrieve(url, self.input_dir + os.path.sep + img_filename)
    #         self.img_list.append(img_filename)
    #     end = time.perf_counter()
    #     logger.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))
    #     self.img_list.append(None)
    
    def resize_image(self, filename):
        target_sizes = [32, 64, 200]
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

    # def perform_resizing(self):
    #     os.makedirs(self.output_dir, exist_ok=True)

    #     logger.info("beginning image resizing")
    #     target_sizes = [32, 64, 200]

    #     start = time.perf_counter()
    #     while True:
    #         filename = self.img_queue.get()
    #         if filename is None:
    #             self.img_queue.task_done()
    #             break
    #         orig_img = Image.open(self.input_dir + os.path.sep + filename)
    #         for basewidth in target_sizes:
    #             img = orig_img
    #             # calculate target height of the resized image to maintain the aspect ratio
    #             wpercent = (basewidth / float(img.size[0]))
    #             hsize = int((float(img.size[1]) * float(wpercent)))
    #             # perform resizing
    #             img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                
    #             # save the resized image to the output dir with a modified file name 
    #             new_filename = os.path.splitext(filename)[0] + \
    #                 '_' + str(basewidth) + os.path.splitext(filename)[1]
    #             img.save(self.output_dir + os.path.sep + new_filename)

    #         os.remove(self.input_dir + os.path.sep + filename)
    #         self.img_queue.task_done()
    #     end = time.perf_counter()

    #     # logger.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        self.logger.info("START make_thumbnails")
        pool = multiprocessing.Pool()

        start = time.perf_counter()

        dl_queue = Queue()
        for img_url in img_url_list:
            dl_queue.put(img_url)
        
        max_dl_threads = 4
        for _ in range(max_dl_threads):
            t = Thread(target=self.download_image, args=(dl_queue,))
            t.start()

        dl_queue.join()
        # self.img_list.append(None)
        start_resize = time.perf_counter()
        pool.map(self.resize_image, self.img_list)
        end_resize = time.perf_counter()
        pool.close()
        pool.join()

        end = time.perf_counter()
        self.logger.info("created {} thumbnails in {} seconds".format(len(self.img_list), end_resize - start_resize))
        self.logger.info("END make_thumbnails in {} seconds".format(end - start))
    