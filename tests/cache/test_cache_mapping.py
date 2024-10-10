from unittest import TestCase

from app.cache import Mapping
from app.file import File
from app.replacement_policy import FIFO, LRU, Random


class TestCacheMapping(TestCase):
	def test_one(self: 'TestCacheMapping') -> None:
		"cache_simulator 256 4 1 R 1 bin_100.bin"
		address = File.read_bin_file('address/bin_100.bin')
		result = Mapping(256, 4, 1, Random).mapping(address)

		self.assertEqual(result, (92, 8, 8, 0, 0))

	def test_two(self: 'TestCacheMapping') -> None:
		"cache_simulator 128 2 4 R 1 bin_1000.bin"
		address = File.read_bin_file('address/bin_1000.bin')
		result = Mapping(128, 2, 4, Random).mapping(address)

		self.assertEqual(result, (864, 136, 136, 0, 0))

	def test_seven(self: 'TestCacheMapping') -> None:
		"cache_simulator 2 1 8 L 1 bin_100.bin"
		address = File.read_bin_file('address/bin_100.bin')
		result = Mapping(2, 1, 8, LRU).mapping(address)

		self.assertEqual(result, (46, 54, 16, 36, 2))

	def test_eight(self: 'TestCacheMapping') -> None:
		"cache_simulator 2 1 8 F 1 bin_100.bin"
		address = File.read_bin_file('address/bin_100.bin')
		result = Mapping(2, 1, 8, FIFO).mapping(address)

		self.assertEqual(result, (43, 57, 16, 39, 2))

	def test_ten(self: 'TestCacheMapping') -> None:
		"cache_simulator 1 4 32 L 1 vortex.in.sem.persons.bin"
		address = File.read_bin_file('address/vortex.in.sem.persons.bin')
		result = Mapping(1, 4, 32, LRU).mapping(address)

		self.assertEqual(result, (107450, 79226, 32, 79194, 0))

	def test_eleven(self: 'TestCacheMapping') -> None:
		"cache_simulator 1 4 32 F 1 vortex.in.sem.persons.bin"
		address = File.read_bin_file('address/vortex.in.sem.persons.bin')
		result = Mapping(1, 4, 32, FIFO).mapping(address)

		self.assertEqual(result, (103226, 83450, 32, 83418, 0))
