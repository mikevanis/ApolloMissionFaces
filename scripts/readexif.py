from pexif import JpegFile
import sys

usage = """Usage: readexif.py filename.jpg"""

if len(sys.argv) != 2:
	print >> sys.stderr, usage
	sys.exit(1)

try:
	ef = JpegFile.fromFile(sys.argv[1])
	ef.dump()
except IOError:
	type, value, traceback = sys.exc_info()
	print >> sys.stderr, "Can't open file ", value
except JpegFile.InvalidFile:
	type, value, traceback = sys.exc_info()
	print >> sys.stderr, "Can't open file ", value
