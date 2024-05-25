def locate_S_G(maze):
  start = []
  goal = []
  for i, row in enumerate(maze):
    for j, char in enumerate(row):
      if char == 'S':
        start.extend([i, j])
      elif char == 'G':
        goal.extend([i, j])
      if len(start)>0 and len(goal)>0:
        break
  return start, goal

def possible_moves(maze, position):
  moves = {
      'L': maze[position[0]][position[1]-1] == '.',
      'R': maze[position[0]][position[1]+1] == '.',
      'U': maze[position[0]-1][position[1]] == '.',
      'D': maze[position[0]+1][position[1]] == '.'
  }
  return moves

def explore_surrounding(maze, cursor, exploration):
  moves = possible_moves(maze, cursor)
  available = []
  new_exploration = {}
  if moves['L'] and f'{cursor[0]}-{cursor[1]-1}' not in exploration:
    new_exploration.update({
      f'{cursor[0]}-{cursor[1]-1}':cursor
    })
    available.append([cursor[0],cursor[1]-1])

  if moves['R'] and f'{cursor[0]}-{cursor[1]+1}' not in exploration:
    new_exploration.update({
      f'{cursor[0]}-{cursor[1]+1}':cursor
    })
    available.append([cursor[0],cursor[1]+1])

  if moves['U'] and f'{cursor[0]-1}-{cursor[1]}' not in exploration:
    new_exploration.update({
      f'{cursor[0]-1}-{cursor[1]}':cursor
    })
    available.append([cursor[0]-1,cursor[1]])

  if moves['D'] and f'{cursor[0]+1}-{cursor[1]}' not in exploration:
    new_exploration.update({
      f'{cursor[0]+1}-{cursor[1]}':cursor
    })
    available.append([cursor[0]+1,cursor[1]])

  return available, new_exploration

def explore(maze, start, goal):
  to_be_searched = []
  explored = {f'{start[0]}-{start[1]}':start}
  cursor = start
  goal_around = [
    [goal[0],goal[1]-1],
    [goal[0],goal[1]+1],
    [goal[0]-1,goal[1]],
    [goal[0]+1,goal[1]],
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

def get_route(exploration, start, goal):
  directions = {'L': (0, 1), 'R': (0, -1), 'D': (-1, 0), 'U': (1, 0)}
  route = []
  cursor = goal
  while cursor != start:
    for key, value in directions.items():
      neighbour = [cursor[0]+value[0], cursor[1]+value[1]]
      nkey = f"{cursor[0]+value[0]}-{cursor[1]+value[1]}"
      ckey = f"{cursor[0]}-{cursor[1]}"

      if nkey in exploration and exploration[ckey] == neighbour:
        route.insert(0,key)
        cursor = neighbour
  return route

def solve(maze):
  start, goal = locate_S_G(maze)
  exploration = explore(maze, start, goal)
  route = get_route(exploration, start, goal)
  print("S", *route, "G", "\n")

with open('./input.txt', 'r') as f:
  lines = f.readlines()
  maze = []
  for i in lines:
    i = i.rstrip()
    if i.startswith("#"):
      maze.append(i.split(" "))
    elif i == "":
        solve(maze)
        maze = []
    else:
      print(i)
  if maze != []:
    solve(maze)
    maze = []