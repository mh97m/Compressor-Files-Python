import multiprocessing as mp
import os
import sys
import tarfile
import lzma
import bz2
import gzip
import zstandard
import time


def compress_directory(dirname, algorithm):
    """Compress a directory using the specified algorithm"""
    if algorithm == "xz":
        arcname = os.path.basename(dirname)
        tarname = dirname + ".tar.xz"
        with tarfile.open(tarname, "w:xz") as tar:
            tar.add(dirname, arcname=arcname)
        return tarname
    elif algorithm == "bzip2":
        arcname = os.path.basename(dirname)
        tarname = dirname + ".tar.bz2"
        with tarfile.open(tarname, "w:bz2") as tar:
            tar.add(dirname, arcname=arcname)
        return tarname
    elif algorithm == "gzip":
        arcname = os.path.basename(dirname)
        tarname = dirname + ".tar.gz"
        with tarfile.open(tarname, "w:gz") as tar:
            tar.add(dirname, arcname=arcname)
        return tarname
    elif algorithm == "zstd":
        arcname = os.path.basename(dirname)
        tarname = dirname + ".tar.zst"
        cctx = zstandard.ZstdCompressor()
        with tarfile.open(tarname, "w") as tar:
            with cctx.stream_writer(tar.fileobj) as zstd_writer:
                tar.add(dirname, arcname=arcname)
        return tarname
    else:
        print("Unsupported compression algorithm:", algorithm)
        return


def main():
    """Main program logic"""
    if len(sys.argv) != 3:
        print("Usage: python compress.py <dirname> <algorithm>")
        return
    dirname = sys.argv[1]
    algorithm = sys.argv[2]
    
    start_time = time.time()  # Start time tracking
    
    # Create a multiprocessing pool with 1 worker for each available CPU core
    pool = mp.Pool(processes=mp.cpu_count())
    
    # Use the multiprocessing pool to asynchronously compress the directory
    result = pool.apply_async(compress_directory, args=(dirname, algorithm))
    
    # Wait for the result to be ready and print a message when done
    result.wait()
    print("Compression completed in {:.2f} seconds".format(time.time() - start_time))  # Print time spent
    

if __name__ == "__main__":
    main()
