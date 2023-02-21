
# Compress Files

This Code Compress files of directory that you gave in arguments.


## Algorithms

* gzip
* bzip2
* xz
* zstd


## Performance

This code wrote with process threading together for fastest run that ever can make...

In this code, the main bottleneck is the I/O operations of reading and writing files, which is why multiprocessing is used.


## Usage

#### Note

python3 is prefix for execute python files in linux.

py is prefix for execute python files in windows.

### Compression

```bashe
python3 compress.py /path/to/directory gzip
```
```bashe
python3 compress.py /path/to/directory bzip2
```
```bashe
python3 compress.py /path/to/directory xz
```
```bashe
python3 compress.py /path/to/directory zstd
```


### Compare

gzip is a good general-purpose compression algorithm that is widely used for compressing text-based files like HTML, CSS, and JavaScript. However, for other types of files, there may be more efficient compression algorithms that can produce smaller compressed file sizes.

Some other popular compression algorithms include:

* bzip2: a compression algorithm that is generally slower than gzip, but can produce smaller compressed file sizes for certain types of data, such as text-based files with long repetitive patterns.

* xz: a compression algorithm that is slower than both gzip and bzip2, but can produce even smaller compressed file sizes for certain types of data.

* zstd: a relatively new compression algorithm that is designed to be very fast while still achieving good compression ratios. It can be a good choice for large files that need to be compressed quickly.

-Compress-Compress files-bzip2: a compression algorithm-gzip: a compression algorithm-xz: a compression algorithm-zst: a compression algorithm