from multiprocessing import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import time


queue = Queue()

m = BaseManager(address=('127.0.0.1',5656),authkey=b'123123')

m.connect()

m.register('get_queue')
q = m.get_queue()


m.register('get_task')
task = m.get_task()

while True:
    time.sleep(1)
    if(len(task) < 10):
        print('process done')
        task.append('process 3')
    else:
        print('process waiting')



# m.shutdown_server()





# if __name__ == "__main__":


    # print(s.debug_info())

    # m.start()