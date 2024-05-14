# Amare Diotte
# 342 Python & Data Processing
# Corey Schafer: Python Tutorial: File Objects - Reading and Writing to Files
# Link to video: https://www.youtube.com/watch?v=Uh2ebFW8OYM

# path is needed if your file isn't in the same directory like this one:
# when nothing is specified, default is to open for reading
# w - write, a - append, read and right - r+
# f = open('test.txt', 'r')

# print(f.name)

# must close file when you are done to prevent memory leaks or errors
# f.close()

# context manager
# works with file within the block and automatically closes file at the end
# also closes files if there are any errors or exceptions (best practice to use them)
with open('test.txt', 'r') as f:
    # this is the whole document
   # f_contents = f.read()
   # print(f_contents)

    # this reads line by line
    # f_contents = f.readline()
    # includes end line characters
    #print(f_contents)
    # does not include
    #f_contents = f.readlines()
    # print(f_contents, end='')
    
    # most efficient = iterating line by line:
    # for line in f:
        # print(f_contents, end='')
    size_to_read = 10
    f_contents = f.read(size_to_read)
    # when you hit the end of the file, f. read returns an empty string
    while len(f_contents) > 0:
        print(f_contents, end='')
        # advance to next line
        f_contents = f.read(size_to_read)

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    # resets document to start
    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)
    

# writing to a file, needs to use w
with open('test2.txt', 'w') as rf:
    # if file doesnt exist, it will be created
    # if it does, it will be ovewritten (use a to append)
    rf.write('Test')
    # write will overwrite in this case
    rf.seek(0)
    rf.write("overwrite test")
    rf.seek(1)
    rf.write('V')

# open file to read
with open('test.txt', 'r') as rf:
    # open file to write
    with open('test_copy.txt', 'w') as wf:
        # copy from one file to the other
        for line in rf:
            wf.write(line)

# using binary mode to copy pictures
with open('frog.jpg', 'rb') as rp:
    with open('frog_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rp_chunk = rp.read(chunk_size)
        while len(rp_chunk) > 0:
            wf.write(rp_chunk)
            rp_chunk = rp.read(chunk_size)

# can access the variable afterwards, but the file is closed:
print(f.closed)

# will get an error if you try to access data:
# print(f.read())
# will get ValueError: I/O operation on closed file.