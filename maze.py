from collections import deque

maze_with_exit = [
                 [0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1 ,0, 1, 0, 1, 0, 1, 1],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1, 1, 0],
                 [0, 1, 0, 1, 0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 1, 0],
                 [1, 1, 1, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0]]

start = (0, 2)
end = (7, 0)

maze_without_exit = [
                    [0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [0, 1 ,0, 1, 0, 1, 0, 1, 1],
                    [0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 0],
                    [0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [1, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 1, 0]]

maze_without_loops = [
                    [0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [0, 1 ,0, 1, 0, 1, 0, 1, 1],
                    [0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [1, 1, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 1, 1, 0]]


def find_path(maze, start, end):
    """
    Finds the way out from a maze.
    :param maze: 2D matrix with the representation of the maze. 0 is a free cell, 1 is a wall.
    :param start: A two-element tuple with coordinates of the start cell.
    :param end: A two-element tuple with coordinates of the end cell.
    :return: The message if path was found or not.
    """
    queue = deque()
    queue.append(start)
    maze_width = len(maze[0])
    maze_height = len(maze)
    # Visited is a 2D matrix with the same size as the maze has. Initialy we have a value 0 in every cell.
    # When we add a cell to the queue we also set the value of that cell in the visited to the value of coorditates of the cell from where we arrived to this cell when we went the shortest way.
    visited = [[0 for column in range(maze_width)] for row in range(maze_height)]
    while len(queue) != 0:
        current_cell = queue.popleft()
        if current_cell == end:
            path = get_path(visited, start, end)
            return f'The way out was found! The path is {path} and has length {len(path)}.'
        y, x = current_cell
        left = x - 1
        right = x + 1
        top = y - 1
        bottom = y + 1
        if (left >= 0) and (maze[y][left] == 0) and (visited[y][left] == 0):
            queue.append((y, left))
            visited[y][left] = (y, x)
        if (right < maze_width) and (maze[y][right] == 0) and (visited[y][right] == 0):
            queue.append((y, right))
            visited[y][right] = (y, x)
        if (top >= 0) and (maze[top][x] == 0) and (visited[top][x] == 0):
            queue.append((top, x))
            visited[top][x] = (y, x)
        if (bottom < maze_height) and (maze[bottom][x] == 0) and (visited[bottom][x] == 0):
            queue.append((bottom, x))
            visited[bottom][x] = (y, x)
    return 'There is no way out'


def get_path(visited, start, end):
    """
    Gets path from start to end of the maze.
    :param visited: An array with visited cells.
    :param start: A two-element tuple with coordinates of the start cell.
    :param end: A two-element tuple with coordinates of the start cell.
    """
    path = []
    current_cell = end
    while current_cell != start:
        path.append(current_cell)
        y, x = current_cell
        current_cell = visited[y][x]
    path.reverse()
    return path


if __name__ == '__main__':
    print('The maze with exit')
    print(find_path(maze_with_exit, start, end))
    print('The maze without exist:')
    print(find_path(maze_without_exit, start, end))
    print('The maze with exit but without loops:')
    print(find_path(maze_without_loops, (0, 0), end))

