import unittest
import io
import time

from tempfile import TemporaryDirectory
from unittest.mock import patch

from decorators import benchmark, log

class TestDecorators(unittest.TestCase):
    def setUp(self):
        self.tempdir = TemporaryDirectory()

    def tearDown(self) -> None:
        self.tempdir.cleanup()
        return super().tearDown()

    @patch('sys.stdout', new_callable=io.StringIO)
    def testLog(self, mock_stdout):
        @log
        def add(a, b):
            return a + b

        add(1, b=2)

        mock_stdout.seek(0)
        written = mock_stdout.read()
        self.assertEqual(written, "running: add args: (1,) kwargs: {'b': 2}\n")


    def testLogWithFile(self):
        file_name = self.tempdir.name + "/log.txt"
        @log(file_name=file_name)
        def add(a, b):
            return a + b

        add(1, b=2)

        with open(file_name) as f:
            written = f.read()
            self.assertEqual(written, "running: add args: (1,) kwargs: {'b': 2}\n")


    @patch('sys.stdout', new_callable=io.StringIO)
    def testBenchmark(self, mock_stdout):
        @benchmark()
        def add(a, b):
            time.sleep(2)
            return a + b

        add(1, b=2)

        mock_stdout.seek(0)
        written = mock_stdout.read()
        self.assertEqual(written, "benchmark: add duration: 2.0\n")


    def testBenchmarkWithFile(self):
        file_name = self.tempdir.name + "/benchmark.txt"

        @benchmark(file_name=file_name)
        def add(a, b):
            time.sleep(2)
            return a + b

        add(1, b=2)

        with open(file_name) as f:
            written = f.read()
            self.assertEqual(written, "benchmark: add duration: 2.0\n")
