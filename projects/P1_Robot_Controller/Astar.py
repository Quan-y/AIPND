```python
##TODO 13 实现你的算法
def cost(x, y, dest):
    dest_x, dest_y = dest
    return abs(x - dest_x) + abs(y - dest_y)


def print_path(closed, x, y):
    locs = []
    while x is not None and y is not None:
        locs.append((x, y))
        x, y = closed[x][y]
    locs.reverse()
    print(locs)


def search(env_data, loc):
    open_list = [[0, 0, loc[0], loc[1]]]
    closed = [[None for _ in range(columns)] for _ in range(rows)]
    closed[loc[0]][loc[1]] = None, None
    
    while open_list:
        open_list.sort(reverse=True)
        f, g, x, y = open_list.pop()
        for act in valid_actions(env_data, (x, y)):
            delta_x, delta_y = MOVES.get(act, (0, 0))
            dest_x, dest_y = x + delta_x, y + delta_y
            if closed[dest_x][dest_y] is None:
                if (dest_x, dest_y) == loc_map['destination']:
                    closed[dest_x][dest_y] = (x, y)
                    print_path(closed, dest_x, dest_y)
                    return
                else:
                    g += 1
                    f = cost(dest_x, dest_y, loc_map['destination'])
                    open_list.append([f, g, dest_x, dest_y])
                    closed[dest_x][dest_y] = (x, y)
                    
                    
search(env_data, robot_current_loc)
```