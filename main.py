
coulmns = [2,2]
rows = [2,2]
black = '⬛️'
ant_color = '🟩'
white = '⬜️'
ant = [0,0,'up',{'white':['up','right','down','left'],'black':['up','left','down','right']},white]
Grid ={
-2:{-2:white,-1:white,0:white,1:white,2:white},
-1:{-2:white,-1:white,0:white,1:white,2:white},
0:{-2:white,-1:white,0:white,1:white,2:white},
1:{-2:white,-1:white,0:white,1:white,2:white},
2:{-2:white,-1:white,0:white,1:white,2:white},
}

def add_row(startorend0or1:int):
  global Grid,coulmns,black,white,rows,ant
  rows[startorend0or1]
  Grid[rows[startorend0or1]] = {}
  for var in coulmns:
    Grid[len(list(Grid))-1][rows[startorend0or1]]
def add_coulmn():
  global Grid,coulmns,black,white,rows,ant
  coulmns += 1
  for var in Grid:
    var.append(white)
def move_ant():
  global map,coulmns,black,white,rows,ant,ant_color
  if Grid[ant[0]][ant[1]] == white:
    ant[2] = ant[3]['white'][ant[3]['white'].index(ant[2])+1]
    Grid[ant[1]][ant[2]] == black
    ant[4]=black
  elif Grid[ant[0]][ant[1]] == black:
    ant[2] = ant[3]['black'][ant[3]['black'].index(ant[2])+1]
    Grid[ant[1]][ant[2]] == white
    ant[4]=white
  else:
    return 'There was an error'
  if ant[2] == 'up':
    ant[1] = ant[1]-1 
    Grid[ant[0]][ant[1]] = ant_color
    Grid[ant[0]][ant[1]+1] = ant[4]
  if ant[2] == 'down':
    ant[1] = ant[1]+1 
    Grid[ant[0]][ant[1]] = ant_color
    Grid[ant[0]][ant[1]-1] = ant[4]
  if ant[2] == 'left':
    ant[0] = ant[0]-1 
    Grid[ant[0]][ant[1]] = ant_color
    Grid[ant[0]+1][ant[1]] = ant[4]
  if ant[2] == 'right':
    ant[0] = ant[1]+1 
    Grid[ant[0]][ant[1]] = ant_color
    Grid[ant[0]-1][ant[1]] = ant[4]
      
        
        
    
  