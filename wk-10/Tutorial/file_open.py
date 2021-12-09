open(
    "error.txt",    # can be absolute or relative, including drive letter
    mode='r',       # 'r' read, 'w' write (overwrite), 'x' create file,
                    # 'a' append, 'b' binary mode (bytes), 't' text mode (default), '+' read/write
    buffering=-1,   # '-1' default single line, '0' no buffering (in binary mode), '1' line buffering (text mode)
                    # '>1' size of fixed size chunk buffer
    encoding=None,  # text mode only, error handler to be used. Default is strict (given by none)
                    # raises a ValueError exception
    errors=None,
    newline=None,
    closefd=True,
    opener=None
)


