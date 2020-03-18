# trying_out_filesAndResource_Management

import sys, math
from itertools import count, islice

file1 = r'C:\users\bryan\Desktop\text.txt'

# writing text files

#f = open(file1, mode='wt', encoding='utf-8')
#text = "hello there!\nI\n h\nave\n the\n hi\ngh gro\nun\nd\n"
#n = f.write(text)

#f.close()
#print("n = ", n)
#print("length text = ", len(text))

# reading text files

#g = open(file1, mode='rt', encoding= 'utf-8')

#print(g.read(32))
#for line in g:
  #print(g.readline())

#g.close()

# appending to text files

#h = open(file1, mode='at', encoding='utf-8')

#b = h.writelines([
             # "this ",
             # "is even1 ",
             # "more text\n",
             # "yay!"])

#h.close()
#print(b)

# file iteration

#def main(filename):
 # f = open(filename, mode='rt', encoding='utf-8')
 # for line in f:
  #  print(line)
   # sys.stdout.write(line)
  #f.close()

#if __name__ == '__main__':
 # main(sys.argv[1])


# managing files with try...finally

#def sequence():
#  seen = set()
#  a=0
#  for n in count(1):
    #yield a
    #seen.add(a)
    #c = a - n
    #if c < 0 or c in seen:
    #  c = a + n
    #a = c


#def write_sequence(num):
  #try:
    #f = open(file1, mode='wt', encoding='utf-8')
    #f.writelines("{0}\n".format(r) for r in islice(sequence(), num + 1))
  #finally:
    #f.close()

#if __name__ == '__main__':
  #write_sequence(int(sys.argv[1]))

# context managers (with-block)

#def read_series(filename):
 # with open(filename, mode='rt', encoding='utf-8') as f:
  #  return [int(line.strip()) for line in f]

#def main():
 # series = read_series(file1)
  #print(series)

#if __name__ == '__main__':
 # main()



# writing binary files
#def write_greyscale(filename, pixels):
#  height = len(pixels)
#  width  = len(pixels[0])

#  with open(filename, 'wb') as bmp:
#    #BMP header
#    bmp.write(b'BM')
#
#    size_bookmark = bmp.tell()
#    bmp.write(b'\x00\x00\x00\x00')
#
#    bmp.write(b'\x00\x00')
#    bmp.write(b'\x00\x00')
#
#    pixel_offset_bookmark = bmp.tell()
#    bmp.write(b'\x00\x00\x00\x00')

#    # image header
#    bmp.write(b'\x28\x00\x00\x00')
#    bmp.write(_int32_to_bytes(width))
#    bmp.write(_int32_to_bytes(height))
#    bmp.write(b'\x01\x00')
#    bmp.write(b'\x08\x00')
#    bmp.write(b'\x00\x00\x00\x00')
#    bmp.write(b'\x00\x00\x00\x00')
#    bmp.write(b'\x00\x00\x00\x00')
#    bmp.write(b'\x00\x00\x00\x00')
#    bmp.write(b'\x00\x00\x00\x00')
#    bmp.write(b'\x00\x00\x00\x00')
#
    # color palette - linear greyscale
 #   for c in range(256):
 #     bmp.write(bytes((c, c, c, 0))) #Blue, Green, Red , zero (alpha?)


    #Pixel data
#    pixel_data_bookmark = bmp.tell()

#    for row in reversed(pixels):
#      row_data = bytes(row)
#      bmp.write(row_data)
#
#      padding = b'\x00' * (4 - (len(row) % 4))
#      bmp.write(padding)

    #End of file
#    eof_bookmark = bmp.tell()

    # fill in file size placeholder
#    bmp.seek(size_bookmark)
#    bmp.write(_int32_to_bytes(eof_bookmark))

    #fill in pixel offset placeholder
#    bmp.seek(pixel_offset_bookmark)
#    bmp.write(_int32_to_bytes(pixel_data_bookmark))

#def _int32_to_bytes(i):
#  return bytes((i & 0xff,
#                i >> 8 & 0xff,
 #               i >> 16 & 0xff,
  #              i >> 24 & 0xff))


#def mandel(real, imag):
 # x = 0
  #y = 0

#  for i in range(1, 257):
#    if x * x + y * y > 10.0:
#      break
#    xt = real + x * x - y * y
#    y  = imag + 2.3876545678 * x * y
 #   x  = xt
 # return int(math.log(i) * 256 / math.log(256)) - 1


#def mandelbrot(size_x, size_y):
 # return [[mandel((1.5 * x / size_x) - 1.0,
  #                (3.0 * y / size_y) - 1.5)
   #        for x in range(size_x)]
    #     for y in range(size_y)]

#pixels = mandelbrot(448 * 2, 256 * 2)
#print(pixels)

#file_name = r'C:\Users\bryan\Desktop\Python\fractals\mandel16.bmp'

#write_greyscale(file_name, pixels)

# bitwise operators - see writing binary values above



# fractal images - see writing binary values above



# reading binary files

#def dimensions(filename):
#  with open(filename, 'rb') as f:
 #   magic = f.read(2)
  #  if magic != b'BM':
   #   raise ValueError("{} is not a BMP file".format(filename))

#    f.seek(18)
#    width_bytes  = f.read(4)
#    height_bytes = f.read(4)

#    return (_bytes_to_int32(width_bytes),
#            _bytes_to_int32(height_bytes))

#def _bytes_to_int32(b):
#  return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)

#print(dimensions(file_name))


# closing with context managers

#IMPORTANT!!!!!!!!!!!!!!!!!!!!!!
from contextlib import closing

class RefrigeratorRaider:

    def open(self):
        print("Open fridge door")

    def take(self, food):
        print("Finding {} .....".format(food))

        if food == 'deep fried pizza':
            raise RuntimeError("Health Warning!")
        print("taking {}".format(food))

    def close(self):
    # Important!! There MUST be a close() method defined in order for the contextlib closing function to work
        print("close fridge door.")


def raid(food):
  # use the with closing as a context manager
  # closes the fridge even if an exception is raised
  # before explicitly closing the door
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        #r.close()

raid("deep fried pizza")
