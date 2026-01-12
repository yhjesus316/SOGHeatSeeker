import unittest
from unittest.mock import patch, MagicMock
import tempfile
import os
import sys

# Add source directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from sog_heatseeker.core import main

class TestCore(unittest.TestCase):
    @patch('sog_heatseeker.core.cctv_monitor.run')
    @patch('sog_heatseeker.core.webcam_recorder.run')
    @patch('sog_heatseeker.core.utils.load_config')
    def test_main_cctv_mode(self, mock_load_config, mock_webcam, mock_cctv):
        # Mock config
        mock_load_config.return_value = {}
        
        # Call main with cctv mode
        with patch('sys.argv', ['sog_heatseeker', '--mode', 'cctv']):
            main()
            
        # Verify cctv monitor was called
        mock_cctv.assert_called_once()
        mock_webcam.assert_not_called()
        
    @patch('sog_heatseeker.core.cctv_monitor.run')
    @patch('sog_heatseeker.core.webcam_recorder.run')
    @patch('sog_heatseeker.core.utils.load_config')
    def test_main_webcam_mode(self, mock_load_config, mock_webcam, mock_cctv):
        # Mock config
        mock_load_config.return_value = {}
        
        # Call main with webcam mode
        with patch('sys.argv', ['sog_heatseeker', '--mode', 'webcam']):
            main()
            
        # Verify webcam recorder was called
        mock_webcam.assert_called_once()
        mock_cctv.assert_not_called()
        
    @patch('sog_heatseeker.core.cctv_monitor.run')
    @patch('sog_heatseeker.core.webcam_recorder.run')
    @patch('sog_heatseeker.core.utils.load_config')
    def test_main_monitor_mode(self, mock_load_config, mock_webcam, mock_cctv):
        # Mock config
        mock_load_config.return_value = {}
        
        # Call main with default mode
        with patch('sys.argv', ['sog_heatseeker']):
            main()
            
        # Verify default monitor mode was called
        mock_cctv.assert_called_once()
        mock_webcam.assert_not_called()

if __name__ == '__main__':
    unittest.main()
