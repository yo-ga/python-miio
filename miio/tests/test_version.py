from unittest import TestCase
from .. import version

class TestVersion(TestCase):
    
    def test_version(self):
        assert version.__version__