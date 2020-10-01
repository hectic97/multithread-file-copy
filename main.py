import threading
import sys
import time

start_time=time.time()

def multithread_copy(path,cp_path,log):
    thr=threading.Thread(target=file_copy,args=(path,cp_path,log))
    thr.start()

def file_copy(path,cp_path,log):
    src = open(path,'rb')
    dest = open(cp_path,'wb')
    log.write('{:<6.2f}Start copying {} to {}\n'.format(round(time.time()-start_time,2),path,cp_path))
    line = src.read(10000) 
    while line != b'':
        dest.write(line)
        line = src.read(10000)
    log.write('{:<6.2f}{} is copied completely\n'.format(round(time.time()-start_time,2),cp_path))
    src.close()
    dest.close()
    

def main():
    log = open('log.txt','a')
    while True:
        path=input('Input the file name: ')
        if path == 'exit':
            log.close()
            sys.exit()
        cp_path=input('Input the new name: ')
        print('')
        if cp_path == 'exit':
            log.close()
            sys.exit()
        multithread_copy(path,cp_path,log)

if __name__ == '__main__':
    main()
    

