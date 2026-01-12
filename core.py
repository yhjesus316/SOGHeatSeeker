#!/usr/bin/env python3
import argparse
import logging
from pathlib import Path
import sys
from . import cctv_monitor, webcam_recorder, utils

def setup_logging(level=logging.INFO):
    """Configure logging"""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def main():
    parser = argparse.ArgumentParser(description="SOGHeatSeeker - Surveillance Toolkit")
    parser.add_argument("--mode", choices=["cctv", "webcam", "monitor"], 
                       default="monitor", help="Operation mode")
    parser.add_argument("--config", type=str, help="Configuration file path")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    
    # Load configuration
    config = utils.load_config(args.config) if args.config else {}
    
    # Run selected mode
    if args.mode == "cctv":
        cctv_monitor.run(config)
    elif args.mode == "webcam":
        webcam_recorder.run(config)
    else:
        # Default monitor mode
        monitor.run(config)

if __name__ == "__main__":
    main()
