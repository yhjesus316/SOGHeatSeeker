import cv2
import threading
import time
import logging
from datetime import datetime

logger = logging.getLogger("SOGHeatSeeker.webcam")

class WebcamRecorder:
    def __init__(self, config):
        self.config = config
        self.recording_active = False
        
    def start(self):
        logger.info("Starting webcam recording")
        self.recording_active = True
        self.record_thread = threading.Thread(target=self.record)
        self.record_thread.daemon = True
        self.record_thread.start()
        
    def stop(self):
        logger.info("Stopping webcam recording")
        self.recording_active = False
        
    def record(self):
        cap = cv2.VideoCapture(self.config.get("camera_index", 0))
        if not cap.isOpened():
            logger.error("Could not open camera")
            return
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording_{timestamp}.mp4"
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
        
        logger.info(f"Recording started: {filename}")
        start_time = time.time()
        
        try:
            while self.recording_active and time.time() - start_time < self.config.get("duration", 3600):
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                else:
                    logger.error("Could not read frame")
                    break
        finally:
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            
        logger.info(f"Recording completed: {filename}")
