import readchar
import os
import random

def main():
    pass

pos_x = 0
pos_y = 1
my_position = [3, 1]
map_width = 20
map_height = 15
num_map_objects = 10
map_objects = []
tail_length = 0
tail = []
end_game = False
while len(map_objects) <= num_map_objects:
    new_position = [random.randint(0, map_width-1), random.randint(0, map_height-1)]
    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)
while not end_game:
    os.system("cls")
    print("-"*(map_width*3) + "--")
    for y in range(map_height):
        print("|",end="")
        for x in range(map_width):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if map_object[pos_x] == x and map_object[pos_y] == y:
                    char_to_draw = "*"
                    object_in_cell = map_object
            for tail_position in tail:
                if tail_position[pos_x] == x and tail_position[pos_y] == y:
                    char_to_draw = "@"
                    tail_in_cell = tail_position
            if y == my_position[pos_y] and x == my_position[pos_x]:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                if tail_in_cell:
                    print("Has Muerto!!")
                    end_game = True
            print(" {} ".format(char_to_draw),end="")
        print("|")
    print("-"*(map_width*3) + "--")
    # print("Cola: {}".format(tail))
    direction = readchar.readchar().decode()
    tail.insert(0,my_position.copy())
    tail = tail[:tail_length]
    if direction == "w":
        my_position[pos_y] -= 1
        if my_position[pos_y] < 0:
            my_position[pos_y] = map_height - 1
    elif direction == "s":
        my_position[pos_y] += 1
        if my_position[pos_y] > map_height - 1:
            my_position[pos_y] = 0
    elif direction == "a":
        my_position[pos_x] -= 1
        if my_position[pos_x] < 0:
            my_position[pos_x] = map_width - 1
    elif direction == "d":
        my_position[pos_x] += 1
        if my_position[pos_x] > map_width - 1:
            my_position[pos_x] = 0
    elif direction == "q":
        end_game = True