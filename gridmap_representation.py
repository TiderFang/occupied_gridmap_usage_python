# /usr/bin/python
# grid map consists of limited numbers of cells. 
# cells could contains the following infomation:
## 1. postion infomation. Using cartation or poly
## 2. neighbors's infomation such as position
## 3. properties of the cells such as occupied or not occupied, colors,etc.

# In grap map ,the cells is called node; the neighbors are called edges.

## so we could say grid map is the set of nodes and edges, one good way of representing grid map is using array. 
## in python we could use the list.

### 1.create square grid map whose cells only contain postion info using cartesian coordinate
### cells represented as ：[x,y] ---this is the cartesian form of position, we could get the postion in list using x and y.
### grid map represented as :[[x0,y0],[x1,y1],...] 
# code
####
map_resolution = 1 # meters
map_heigth = 100   #meters
map_length = 100   #meters
colum_num  = map_heigth/map_resolution
row_num    = map_length/map_resolution
gridmap = []
for x in range(colum_num):
  for y in range(row_num):
    gridmap.append([x,y])
