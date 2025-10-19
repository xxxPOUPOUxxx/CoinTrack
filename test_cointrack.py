# test_cointrack.py
"""
Tests for CoinTrack module.
"""

import unittest
from cointrack import CoinTrack

class TestCoinTrack(unittest.TestCase):
    """Test cases for CoinTrack class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinTrack()
        self.assertIsInstance(instance, CoinTrack)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinTrack()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
