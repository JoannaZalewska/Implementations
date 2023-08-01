from queue import Queue

maze = [[1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1]]

start = (1, 1)
end = (4, 1)


def find_path(maze, start, end):
    """
    Finds the way out from a maze.
    :param maze: 2D matrix with the representation of the maze. 0 is a free cell, 1 is a wall.
    :param start: A two-element tuple with coordinates of the start cell.
    :param end: A two-element tuple with coordinates of the end cell.
    :return: The message if path was found or not.
    """
    queue = Queue()
    queue.put(start)
    visited = [start]
    previous_cells = [None]
    while queue.qsize() != 0:
        current_cell = queue.get()
        if current_cell == end:
            visited.append(current_cell)
            path, length_of_path = get_path(visited, previous_cells)
            return f'The way out was found! The path is {path} and has length {length_of_path}.'
        x = current_cell[1]
        y = current_cell[0]
        left = x - 1
        right = x + 1
        top = y - 1
        bottom = y + 1
        if (left >= 0) and (maze[y][left] == 0) and ((y, left) not in visited):
            queue.put((y, left))
            visited.append((y, left))
            previous_cells.append((y, x))
        if (right < len(maze[0])) and (maze[y][right] == 0) and ((y, right) not in visited):
            queue.put((y, right))
            visited.append((y, right))
            previous_cells.append((y, x))
        if (top >= 0) and (maze[top][x] == 0) and ((top, x) not in visited):
            queue.put((top, x))
            visited.append((top, x))
            previous_cells.append((y, x))
        if (bottom < len(maze)) and (maze[bottom][x] == 0) and ((bottom, x) not in visited):
            queue.put((bottom, x))
            visited.append((bottom, x))
            previous_cells.append((y, x))
    return "There is no way out"


def get_path(visited, previous_cells):
    """
    Gets path from start to end of the maze.
    :param visited: An array with visited cells.
    :param previous_cells: An array with previous cells.
    """
    current_cell = visited[-1]
    path = [current_cell]
    cell_before_current = previous_cells[-1]
    while cell_before_current is not None:
        where_in_visited = visited.index(cell_before_current)
        current_cell = visited[where_in_visited]
        cell_before_current = previous_cells[where_in_visited]
        path.append(current_cell)
    path.reverse()
    return path, len(path)


print(find_path(maze, start, end))
