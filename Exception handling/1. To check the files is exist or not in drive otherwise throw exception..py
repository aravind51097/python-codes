def file():
    try:
        fp=open('filethere.txt','r')
        fp.read()
    except IOError:
        print('file not found')
        print('please enter valid file name')
file=file()
