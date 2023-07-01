import zlib
import base64
data = open("compressionDemo.txt", 'r').read()

# Convert txt to bytes
bytesData = bytes(data, 'utf-8')
compressed_data = zlib.compress(bytesData, 9)

#  Encode compressed data

encoded_data = base64.b64encode(compressed_data)


decoded_data = encoded_data.decode('utf-8')

compressedFile = open('compressed.txt', 'w')
compressedFile.write(decoded_data)


#  Decompressed data
decompressed_data = zlib.decompress(base64.b64decode(encoded_data))

print(decompressed_data)
