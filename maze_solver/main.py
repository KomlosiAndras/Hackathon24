#returns the coordinates of the S and G characters in a given matrix
def locate_S_G(maze):
  start = []
  goal = []
  for i, row in enumerate(maze):
    for j, char in enumerate(row):
      if char == 'S':
        start.extend([i, j])
      elif char == 'G':
        goal.extend([i, j])
      if len(start) > 0 and len(goal) > 0:
        break
  return start, goal

#returns a dictionary containing the directions in which it is 
#possible to move from a given coordinate in a given matrix
def possible_moves(maze, position):
  moves = {
      'L': maze[position[0]][position[1]-1] == '.',
      'R': maze[position[0]][position[1]+1] == '.',
      'U': maze[position[0]-1][position[1]] == '.',
      'D': maze[position[0]+1][position[1]] == '.'
  }
  return moves

#"explores" the surrounding of a given position in a matrix, 
#returns the directions in which is possible to continue exploration, 
#and records from which cell the new ones were dicovered
def explore_surrounding(maze, cursor, exploration):
  moves = possible_moves(maze, cursor)
  available = []
  new_exploration = {}
  if moves['L'] and f'{cursor[0]}-{cursor[1] - 1}' not in exploration:
    new_exploration.update({
      f'{cursor[0]}-{cursor[1] - 1}':cursor
    })
    available.append([cursor[0],cursor[1] - 1])

  if moves['R'] and f'{cursor[0]}-{cursor[1] + 1}' not in exploration:
    new_exploration.update({
      f'{cursor[0]}-{cursor[1] + 1}':cursor
    })
    available.append([cursor[0],cursor[1] + 1])

  if moves['U'] and f'{cursor[0] - 1}-{cursor[1]}' not in exploration:
    new_exploration.update({
      f'{cursor[0]-1}-{cursor[1]}':cursor
    })
    available.append([cursor[0] - 1,cursor[1]])

  if moves['D'] and f'{cursor[0] + 1}-{cursor[1]}' not in exploration:
    new_exploration.update({
      f'{cursor[0] + 1}-{cursor[1]}':cursor
    })
    available.append([cursor[0] + 1,cursor[1]])

  return available, new_exploration

#"explores" a given matrix from the given start point until it finds the given end point
def explore(maze, start, goal):
  to_be_searched = []
  explored = {f'{start[0]}-{start[1]}':start}
  cursor = start
  goal_around = [
    [goal[0],goal[1] - 1],
    [goal[0],goal[1] + 1],
    [goal[0] - 1,goal[1]],
    [goal[0] + 1,goal[1]],
  ]
  e = True
  while e:
    available, new_exploration = explore_surrounding(maze, cursor, explored)
    to_be_searched.extend(available)
    extend_exploration = new_exploration.copy()
    for key in new_exploration.keys():
      if key in explored:
        extend_exploration.pop(key)
    explored.update(extend_exploration)
    cursor = to_be_searched[0]
    to_be_searched.pop(0)
    if cursor in goal_around:
      e = False
      explored.update({
      f'{goal[0]}-{goal[1]}':cursor
    })
  return explored

#from a dictionary containing which cell was discovered from where,
#back traces the shortest possible route and returns the directions as a list
def get_route(exploration, start, goal):
  directions = {'L': (0, 1), 'R': (0, -1), 'D': (-1, 0), 'U': (1, 0)}
  route = []
  cursor = goal
  while cursor != start:
    for key, value in directions.items():
      neighbour = [cursor[0] + value[0], cursor[1] + value[1]]
      nkey = f"{cursor[0] + value[0]}-{cursor[1] + value[1]}"
      ckey = f"{cursor[0]}-{cursor[1]}"

      if nkey in exploration and exploration[ckey] == neighbour:
        route.insert(0, key)
        cursor = neighbour
  return route

#finds a path from S to G in a given matrix and prints it
def solve(maze):
  start, goal = locate_S_G(maze)
  exploration = explore(maze, start, goal)
  route = get_route(exploration, start, goal)
  print("S", *route, "G")

#reading the input file, and storing the matrixes in a dictionary
mazes = {}
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  current_key = ""
  current_maze = []
  for i in lines:
    i = i.rstrip()
    if i.startswith("#"):
      current_maze.append(i.split(" "))
    elif i:
      current_key = i
    else:
      mazes[current_key] = current_maze
      current_key = ""
      current_maze = []
  mazes[current_key] = current_maze

#iterating through the mazes and solving them
for name, maze in mazes.items():
  print(name)
  solve(maze)
  print()
