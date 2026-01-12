import cv2
import threading
import queue
import time
import socket
import logging
from datetime import datetime

logger = logging.getLogger("SOGHeatSeeker.cctv")

class CCTVMonitor:
    def __init__(self, config):
        self.config = config
        self.frame_queue = queue.Queue(maxsize=config.get("buffer_size", 10))
        self.streaming_active = False
        
    def start(self):
        logger.info("Starting CCTV monitoring")
        self.streaming_active = True
        self.capture_thread = threading.Thread(target=self.capture_frames)
        self.capture_thread.daemon = True
        self.capture_thread.start()
        
    def stop(self):
        logger.info("Stopping CCTV monitoring")
        self.streaming_active = False
        
    def capture_frames(self):
        cap = cv2.VideoCapture(self.config.get("camera_index", 0))
        if not cap.isOpened():
            logger.error("Could not open camera")
            return
            
        while self.streaming_active:
            ret, frame = cap.read()
            if ret:
                try:
                    self.frame_queue.put_nowait(frame)
                except queue.Full:
                    # Drop oldest frame if buffer full
                    self.frame_queue.get_nowait()
                    self.frame_queue.put_nowait(frame)
            time.sleep(0.05)  # Prevent high CPU usage
            
        cap.release()
        
    def get_frame(self):
        try:
            return self.frame_queue.get_nowait()
        except queue.Empty:
            return None
