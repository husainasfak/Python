import zlib
import base64


def compress(inputFile, outputFile):
    data = open(inputFile, 'r').read()
    bytesData = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(bytesData, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressedFile = open(outputFile, 'w')
    compressedFile.write(decoded_data)


def decompress(inputfile, outfile):
    file_content = open(inputfile, 'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8 ')
    file = open(outfile, 'w')
    file.write(decoded_data)
    file.close()
