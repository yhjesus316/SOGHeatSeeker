import json
import logging
from pathlib import Path

logger = logging.getLogger("SOGHeatSeeker.utils")

def load_config(path):
    """Load configuration from JSON file"""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load config: {str(e)}")
        return {}

def save_config(config, path):
    """Save configuration to JSON file"""
    try:
        with open(path, 'w') as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save config: {str(e)}")

def create_default_config():
    """Create default configuration"""
    return {
        "camera_index": 0,
        "buffer_size": 10,
        "duration": 3600,  # 1 hour
        "recording_interval": 7200,  # 2 hours
        "output_dir": "./recordings",
        "webhook_url": "https://discordapp.com/api/webhooks/1460351994152620083/gGxWHnn5haxx9kb6jdcYVo-XlzJ13EvcgbVaHOsgutRe_n7E3OERfITFBZJ724gd8hPE"
    }
