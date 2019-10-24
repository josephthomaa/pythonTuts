import multiprocessing

def spawn(num):
    print('Spawned # {}'.format(num))

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join()