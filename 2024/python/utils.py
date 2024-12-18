import time
import numpy as np

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result

    return timed


def read_matrix_from_file(filename: str, to_numpy: bool = False, to_int: bool = False): 
    with open(filename, 'r') as f: 
        if to_int: 
            inp = [list(map(int, i.strip())) for i in f.readlines()]
            #inp = [int(n) for n in f.readline().split()]   
        else: 
            inp = [list(i.strip()) for i in f.readlines()]
            
        if to_numpy: 
            inp = np.array(inp)
    return inp

class FancyMatrix: 
    def __init__(self, wh: list[list]): 
        self.wh = wh
    
    def __repr__(self): 
        new_line = '\n'
        return f"{new_line.join(''.join(row) for row in self.wh)}"
        
    def __getitem__(self, row) -> list:
        return self.wh[row]
      
    def __len__(self): 
        return len(self.wh)
    
    def find_unique_val(self, val) -> tuple:
        for row in range(len(self.wh)):
            for col in range(len(self.wh[0])): 
                if self.wh[row][col] == val:
                    return (row, col)