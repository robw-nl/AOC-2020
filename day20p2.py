#  Rotations: 4x90* + 1xH + + 4x90* 1xV flip = all possible positions
class tile(object):
    def __init__(self, grid = False):
        self.tile_id = grid[0]
        self.tile = grid[1:]
        self.len = len(self.tile) if self.tile != 0 else 0
        tile_8 = []
        
    def rotate(self, rotation = 'r'): 
        x = list(zip(*self.tile[::-1])) if rotation == 'r' else list(zip(*self.tile))[::-1]
        self.tile = [''.join(b) for b in x]
    
    def flip(self, rotation):
        self.tile = [b[::-1] for b in self.tile] if rotation == 'v' else [b for b in self.tile[::-1]]

    @property
    def tile8(self):
        b=self.tile[1:9] # b is 8x8-tile       
        l = [c[1:9] for c in b] # l = elke line in tile
        return l
    
    @property
    def south(self):
        return self.tile[-1] if self.tile else []
    
    @property
    def north(self):
        return self.tile[0] if self.tile else []
    
    @property
    def west(self):
        x = []
        x += [[i][0][0] for i in self.tile]
        x = ''.join(x)
        return x if self.tile else []
    
    @property
    def east(self):
        x = []
        x += [[i][0][-1] for i in self.tile]
        x = ''.join(x)
        return x if self.tile else []

def shift(g, n = 1):
    return g[-n:] + g[:-n]

def swap(g):
    g[0], g[1] = g[1], g[0]
    return g

def add_e_col(puz, dim):
    a = ['East']*dim
    puz.append(a)
    return puz

def add_w_col(puz, dim):
    a = ['West']*dim
    puz.insert(0, a)
    return puz

def match_e(tile1, tile2):
    for _ in range(2):
        for _ in range(4):
            if tile1.east == tile2.west:
                return True
            tile2.rotate()
        tile2.flip('v')
    return tile1.east == tile2.west

def match_w(tile1, tile2):
    for _ in range(2):
        for _ in range(4):
            if tile1.west == tile2.east:
                return True
            tile2.rotate()
        tile2.flip('v')
    return tile1.west == tile2.east

def assm_w(puzz, grid, dim):
    shift_row = shift_col = i = 0
    while len(grid) != 0 and i != len(grid):
        if shift_row == dim:
            shift_row = shift_col = 0
        if not match_w(puzz[shift_col][shift_row], grid[0]):
            grid = shift(grid, len(grid)-1)
            i += 1
            continue 
        if puzz[0][shift_row] != 'West' and shift_row == 0:
            puzz = add_w_col(puzz, dim)
            shift_col = +1

        puzz[0][0+shift_row] =  grid[0]      
        del grid[0]
        shift_row += 1
        i = 0            
    return puzz, grid


def assm_e(puzz, grid, dim):
    shift_row = shift_col = i = 0
    while i != len(grid) and len(grid) != 0:
        if shift_row == dim:
            shift_row = 0
            shift_col += 1   
        if not match_e(puzz[shift_col][shift_row], grid[0]):
            grid = shift(grid, len(grid)-1)
            i += 1
            continue
        if puzz[0][shift_row] != 'East' and shift_row == 0:
            puzz = add_e_col(puzz, dim)

        puzz[-1][shift_row] = grid[0]
        del grid[0]
        shift_row += 1
        i = 0 
    return puzz, grid
    
def match_z(tile1, tile2, first_time = False):
    for _ in range(2):
        for _ in range(4):
            if tile1.south == tile2.north:
                return True
            if first_time:
                for _ in range(2):
                    for _ in range(4):
                        if tile1.south == tile2.north:
                            return True
                    tile1.rotate()
                tile1.flip('v')
            tile2.rotate()
        tile2.flip('v')
    return tile1.south == tile2.north

def match_n(tile1, tile2, first_time = False):
    for _ in range(2):
        for _ in range(4):
            if tile1.north == tile2.south:
                return True
            if first_time:
                for _ in range(2):
                    for _ in range(4):
                        if tile1.north == tile2.south:
                            return True
                    tile1.rotate()
                tile1.flip('v')
            tile2.rotate()
        tile2.flip('v')
    return tile1.north == tile2.south

def assm_s(puzz, grid, dim): 
    c = i = 0
    while len(puzz[0]) != dim and i <= len(grid):
        if not match_z(puzz[0][-1], grid[0], len(puzz[0])==1):
            grid = shift(grid, len(grid)-1)
            i += 1
            continue
        if puzz[0][-1].south == grid[0].north:
            puzz[0].append(grid[0])
            
        del grid[0]
        i = 0
    return puzz, grid
 
def assm_n(grid, dim): 
    c = i = 0
    puzz = [[grid[0]]]
    del grid[0]
    
    while len(puzz[0]) != dim and i <= len(grid):
        if not match_n(puzz[0][0], grid[0], len(puzz[0])==1):
            grid = shift(grid, len(grid)-1)
            i += 1
            continue
        if puzz[0][0].north == grid[0].south:
            puzz[0].insert(0, grid[0])
            
        del grid[0]
        i = 0
    return puzz, grid

def find_monsters(grid):
    '''
    01234567890123456789-----------------------------------}
                      # -----------------------------------}
    #    ##    ##    ###-----------------------------------}
     #  #  #  #  #  #   -----------------------------------}
    '''
    hlen = len(grid[0])-19 # -20 as the sea monster is 20 long
    vlen = len(grid)-2 # -3 as the sea monster is height 3
    found = end=0
    t=[]
    for line in grid:
        t.append(line)
        if len(t) == 3:
            # scan for monster here with my very own slider
            for c, _ in enumerate(range(hlen)):
                if  (   t[0][18+c] == '#' and 
                        t[1][0+c]  == '#' and t[1][5+c]  == '#' and t[1][6+c]  == '#' and t[1][11+c] == '#' and 
                        t[1][12+c] == '#' and t[1][17+c] == '#' and t[1][18+c] == '#' and t[1][19+c] == '#' and 
                        t[2][1+c]  == '#' and t[2][4+c]  == '#' and t[2][7+c]  == '#' and t[2][10+c] == '#' and
                        t[2][13+c] == '#' and t[2][16+c]
                    ):
                    found+=1
            t.pop(0) # remove first line
        end += 1 # end it counter
        if end == vlen: # break before end of grid
            return found

def make_puzz8(puzz):
    puzz8 = []
    string=''
    for i in range(12):
        for j in range(8):
            for k in range(12):
                q = puzz[k][i]
                string+=q.tile8[j]
            puzz8.append(string)
            string = ''
    return puzz8

def main():
    lines = open('day20p2.txt').read().split('\n\n')
    grid = [line.split() for line in lines] # make the grid
    grid = [x for x in grid if x] # remove empty items
    grid = [tile(i) for i in grid]

    dim = (int(len(grid) ** 0.5)) # grid dimension

    puzz, grid = assm_n(grid, dim)
    puzz, grid = assm_s(puzz, grid, dim)
    puzz, grid = assm_e(puzz, grid, dim)
    puzz, grid = assm_w(puzz, grid, dim)

    puzz8 = make_puzz8(puzz)
    monsters=0
    for _ in range(2):
        for _ in range(4):
            monsters += find_monsters(puzz8)
            if monsters > 0:
                break
            x = list(zip(*puzz8[::-1])) # rotate
            puzz8 = [''.join(b) for b in x]
        puzz8 = [b[::-1] for b in puzz8] # flip

    sea_roughness = sum(str(i).count('#') for i in puzz8) - 26*15
    print('\nNr. of monsters = ', monsters, 'sea_roughness = ', sea_roughness, '\n')

if __name__ == '__main__':   
        main()