import pygame
import sys
from resources.helper_functions import *
import random 
import time

















""" Mendotory Functions """ 



def connect_component(component):
    """
    This function connects components with each other in the linked list. 
    """


    # Generating ID
    id = ''
    position = (0,0)
    if component == 'bulb':
        id = 1
        while "B" + str(id) in circuit:
            id+=1
        id = 'B'+str(id)
        position = (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70))
    elif component == "fan":
        id = 1
        while "F" + str(id) in circuit:
            id +=1
        id = "F" + str(id)
        position = (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70))
    elif component == "battery":
        id = 1
        while "PS" + str(id) in circuit:
            id += 1
        id = "PS" + str(id)
        position = (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70))
    elif component == "switch":
        id = "switch"
        position = (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70))    




    # Finding Initial Component Connected Node
    start = None # The first node (previous)

    for i in circuit:

        if circuit[i][2] == None:
            if i[0] == 'B' or i[0] == "F" or i[0] == "P":
                if circuit[i][1][0]+140 == position[0] and circuit[i][1][1] == position[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], id)
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
            if i[0] == 'L' and (abs(circuit[i][1][0]-circuit[i][1][2]) > 10 or abs(circuit[i][1][1]-circuit[i][1][3]) > 10):
                if circuit[i][1][2] == position[0] and circuit[i][1][3] == position[1]+70:
                    circuit[i] = (circuit[i][0], circuit[i][1], id)
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
        elif type(circuit[i][2]) == str:
            if i[0] == 'B' or i[0] == "F" or i[0] == "P":
                if circuit[i][1][0]+140 == position[0] and circuit[i][1][1] == position[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2], id))
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
            if i[0] == 'L' and (abs(circuit[i][1][0]-circuit[i][1][2]) > 10 or abs(circuit[i][1][1]-circuit[i][1][3]) > 10):
                if circuit[i][1][2] == position[0] and circuit[i][1][3] == position[1]+70:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2], id))
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
        elif type(circuit[i][2]) == tuple:
            if i[0] == 'B' or i[0] == "F" or i[0] == "P":
                if circuit[i][1][0]+140 == position[0] and circuit[i][1][1] == position[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2][0], circuit[i][2][1], id))
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
            if i[0] == 'L' and (abs(circuit[i][1][0]-circuit[i][1][2]) > 10 or abs(circuit[i][1][1]-circuit[i][1][3]) > 10):
                if circuit[i][1][2] == position[0] and circuit[i][1][3] == position[1]+70:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2][0], circuit[i][2][1], id))
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue



    end = None # The last node (next)
    for i in circuit:
        if circuit[i][0] == None:
            if i[0] == 'B' or i[0] == "F" or i[0] == 'P':
                if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]:
                    circuit[i] = (id, circuit[i][1], circuit[i][2])
                    if end == None:
                        end = i
                    elif type(end) == str:
                        end = (end, i)
                    elif type(end) == tuple and len(end) == 2:
                        end = (end[0], end[1], i)
                    continue
            if i[0] == 'L':
                if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]+70:
                    circuit[i] = (id, circuit[i][1], circuit[i][2])
                    if end == None:
                        end = i
                    elif type(end) == str:
                        end = (end, i)
                    elif type(end) == tuple and len(end) == 2:
                        end = (end[0], end[1], i)
                    continue
        if type(circuit[i][0]) == str:
            if i[0] == 'B' or i[0] == "F" or i[0] == 'P':
                if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]:
                    circuit[i] = ((circuit[i][0], id), circuit[i][1], circuit[i][2])
                    if end == None:
                        end = i
                    elif type(end) == str:
                        end = (end, i)
                    elif type(end) == tuple and len(end) == 2:
                        end = (end[0], end[1], i)
                    continue
            if i[0] == 'L':
                if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]+70:
                    circuit[i] = ((circuit[i][0], id), circuit[i][1], circuit[i][2])
                    if end == None:
                        end = i
                    elif type(end) == str:
                        end = (end, i)
                    elif type(end) == tuple and len(end) == 2:
                        end = (end[0], end[1], i)
                    continue
        if type(circuit[i][0]) == tuple:
            if i[0] == 'B' or i[0] == "F" or i[0] == 'P':
                if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]:
                    circuit[i] = ((circuit[i][0][0], circuit[i][0][1], id), circuit[i][1], circuit[i][2])
                    if end == None:
                        end = i
                    elif type(end) == str:
                        end = (end, i)
                    elif type(end) == tuple and len(end) == 2:
                        end = (end[0], end[1], i)
                    continue
            if i[0] == 'L':
                if circuit[i][1][0] == position[0]+140 and circuit[i][1][1] == position[1]+70:
                    circuit[i] = ((circuit[i][0][0], circuit[i][0][1], id), circuit[i][1], circuit[i][2])
                    if end == None:
                        end = i
                    elif type(end) == str:
                        end = (end, i)
                    elif type(end) == tuple and len(end) == 2:
                        end = (end[0], end[1], i)
                    continue
        



        if id == "switch":
            if i[0] == "L":
                if circuit[i][1][0] == position[0] and circuit[i][1][1] == position[1]+210:
                    circuit[i] = (id, circuit[i][1], circuit[i][2])
                    end = i
                    break
        
    img_address = ""
    if component == "bulb":
        img_address = 'resources/images/off_180_b_img.png'
    elif component == "fan":
        img_address = 'resources/images/off_180_f_img.png'
    elif component == "battery":
        img_address = 'resources/images/on_0_ps_img.png'
    elif component == "switch":
        img_address = "resources/images/switch.png"

    form_connection(circuit, id, start, (position[0], position[1], img_address), end)
    component = ""








def is_hovering(rect_tuple, mouse_pos):
    """
    This function highlights the rect the mouse is hovering on. 
    """
    x0 = rect_tuple[0][0]
    y0 = rect_tuple[0][1]
    x1 = rect_tuple[1][0]
    y1 = rect_tuple[1][1]

    if mouse_pos[0] >= x0 and mouse_pos[1] >= y0 and mouse_pos[0] <= x1 and mouse_pos[1] <= y1:
        return True
    return False






def is_clicked(rect_tuple, mouse_pos, mouse): # from ((x,y),(x,y))
    """
    This function returns a boolean value for a particular mouse position indicating whether the rect to be clicked
    is clicked or not.
    """
    x0 = rect_tuple[0][0]
    y0 = rect_tuple[0][1]
    x1 = rect_tuple[1][0]
    y1 = rect_tuple[1][1]

    if mouse[0] and mouse_pos[0] >= x0 and mouse_pos[1] >= y0 and mouse_pos[0] <= x1 and mouse_pos[1] <= y1:
        return True
    return False
        

def near_DIVISION_multiple(DIVISION, number):
    """
    This function returns the nearest block clicked in the grid for the wires to be made. 
    """
    a = number
    if a%DIVISION >= DIVISION//2:
        while a%DIVISION != 0:
            a+=1
        return a
    else:
        while a%DIVISION != 0:
            a-=1
        return a
    

def remove_animation(linked_list):
    animated = []
    for i in linked_list:
        if i[:2] == "ON":
            animated.append(i)
    for i in animated:
        del linked_list[i]



def display_circuit_from_linked_list(linked_list): 
    """
    This function stores whatever is being dragged on the screen from the menu bar. 
    """
    for i in linked_list:
        if type(linked_list[i][1]) != dict:
            if i[0] == 'L':

                pygame.draw.line(window, WIRE_COLOR, 
                    [linked_list[i][1][0], linked_list[i][1][1]], 
                    [linked_list[i][1][2], linked_list[i][1][3]], 5)

            elif linked_list[i][1] != None:

                img = pygame.image.load(linked_list[i][1][2])
                scaled_img = pygame.transform.scale(img, (140,140))
                window.blit(scaled_img, (linked_list[i][1][0], linked_list[i][1][1]))
        else:
            display_circuit_from_linked_list(linked_list[i][1])
        

        if i[:3] == "ONF":
            if circuit[i][1][2] == 'resources/images/on_180_f_img/1.png':
                circuit[i] = (None, (circuit[i][1][0], circuit[i][1][1], 'resources/images/on_180_f_img/2.png') , None)
            elif circuit[i][1][2] == 'resources/images/on_180_f_img/2.png':
                circuit[i] = (None, (circuit[i][1][0], circuit[i][1][1], 'resources/images/on_180_f_img/1.png') , None)





def draw_grid(DIVISION): # draws grid.
    temp325 = 1
    while DIVISION*temp325 <= WINDOW_WIDTH:
        pygame.draw.line(window, GRID_COLOR, 
                [DIVISION*temp325, 0], 
                [DIVISION*temp325, WINDOW_HEIGHT], 5)
        pygame.draw.line(window, GRID_COLOR, 
                [0, DIVISION*temp325], 
                [WINDOW_WIDTH, DIVISION*temp325], 5)
        temp325 += 1



def connect_wire():
    # connects wires in the dictionary
    id = 1
    while "L" + str(id) in circuit:
        id+=1
    id = 'L'+str(id)
    

    # For Tail
    start = None
    for i in circuit:
        if circuit[i][2] == None:
            if i[0] == 'B' or i[0] == 'F' or i[0] == 'P':
                if circuit[i][1][0]+140 == init_mouse_pos[0] and circuit[i][1][1]+70 == init_mouse_pos[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], id)

                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)

                    continue
            if i[0] == 'L':
                if circuit[i][1][2] == init_mouse_pos[0] and circuit[i][1][3] == init_mouse_pos[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], id)
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
        

        if type(circuit[i][2]) == str:
            if i[0] == 'B' or i[0] == 'F' or i[0] == 'P':
                if circuit[i][1][0]+140 == init_mouse_pos[0] and circuit[i][1][1]+70 == init_mouse_pos[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2], id))  
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
            if i[0] == 'L':
                if circuit[i][1][2] == init_mouse_pos[0] and circuit[i][1][3] == init_mouse_pos[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2], id))  
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
        if type(circuit[i][2]) == tuple:
            if i[0] == 'B' or i[0] == 'F' or i[0] == 'P':
                if circuit[i][1][0]+140 == init_mouse_pos[0] and circuit[i][1][1]+70 == init_mouse_pos[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2][0], circuit[i][2][1], id))
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
            if i[0] == 'L':
                if circuit[i][1][2] == init_mouse_pos[0] and circuit[i][1][3] == init_mouse_pos[1]:
                    circuit[i] = (circuit[i][0], circuit[i][1], (circuit[i][2][0], circuit[i][2][1], id))
                    if start == None:
                        start = i
                    elif type(start) == str:
                        start = (start, i)
                    elif type(start) == tuple and len(start) == 2:
                        start = (start[0], start[1], i)
                    continue
        
        

    # For Head
    end = None
    for i in circuit:
        if circuit[i][0] == None:
            if i[0] == 'B' or i[0] == 'F' or i[0] == 'P':
                if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1]+70 == line_ending_point[1]:
                    circuit[i] = (id, circuit[i][1], circuit[i][2])
                    end = i
                    
            if i[0] == 'L':
                if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1] == line_ending_point[1]:
                    circuit[i] = (id, circuit[i][1], circuit[i][2])
                    end = i
                     
        if type(circuit[i][0]) == str and id != circuit[i][0]:
            if i[0] == 'B' or i[0] == 'F' or i[0] == 'P':
                if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1]+70 == line_ending_point[1]:
                    circuit[i] = ((circuit[i][0], id), circuit[i][1], circuit[i][2])
                    end = i
                     
            if i[0] == 'L':
                if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1] == line_ending_point[1]:
                    circuit[i] = ((circuit[i][0], id), circuit[i][1], circuit[i][2])
                    end = i
                     
        if type(circuit[i][0]) == tuple and id not in circuit[i][0]:
            if i[0] == 'B' or i[0] == 'F' or i[0] == 'P':
                if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1]+70 == line_ending_point[1]:
                    circuit[i] = ((circuit[i][0][0], circuit[i][0][1], id), circuit[i][1], circuit[i][2])
                    end = i
                     
            if i[0] == 'L':
                if circuit[i][1][0] == line_ending_point[0] and circuit[i][1][1] == line_ending_point[1]:
                    circuit[i] = ((circuit[i][0][0], circuit[i][0][1], id), circuit[i][1], circuit[i][2])
                    end = i
                     
    
    form_connection(circuit, id, start, (init_mouse_pos[0], init_mouse_pos[1], line_ending_point[0], line_ending_point[1]), end)


def complete_circuit(circuit):
    if "PS1" in circuit:
        start = circuit["PS1"][2]
        while start != "PS1" and start != None:
            start = circuit[start][2]
        if start == "PS1":
            return True
        return False
    return False

def counter(lst):
    count = 0
    for _ in lst:
        if _ != None:
            count += 1
    return count

# def normal_circuit(circuit, comp, electrons_coordinates):
#     if comp[:2] == "PS":
#         if cycle_num == 1:
#             electrons_coordinates = (circuit[comp][1][0]+70, circuit[comp][1][1]+70)
#             cycle_num += 1
#         if electrons_coordinates[0]+elec_speed < circuit[comp][1][0]+130:
#             electrons_coordinates = (electrons_coordinates[0]+elec_speed, electrons_coordinates[1])
#         else:
#             if type(circuit[comp][2]) != tuple:
#                 comp = circuit[comp][2]
#                 cycle_num = 1
#             # else:
#             #     old_comp = comp
#             #     comp = []
#             #     for i in circuit[old_comp][2]:
#             #         comp.append(i)
#             #     cycle_num = 1
#     else:
#         if comp[0] =="L":
#             if cycle_num == 1:
#                 electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1])
#                 cycle_num += 1
#             if circuit[comp][1][0] == circuit[comp][1][2]:
#                 if circuit[comp][1][3] - electrons_coordinates[1] > 0:
#                     electrons_coordinates = (electrons_coordinates[0], electrons_coordinates[1]+elec_speed)
#                 elif electrons_coordinates[1] - circuit[comp][1][3] > 0:
#                     electrons_coordinates = (electrons_coordinates[0], electrons_coordinates[1]-elec_speed)
#                 else:
#                     if type(circuit[comp][2]) != tuple:
#                         comp = circuit[comp][2]
#                         cycle_num = 1
#                     # else:
#                     #     old_comp = comp
#                     #     comp = []
#                     #     for i in circuit[old_comp][2]:
#                     #         comp.append(i)
#                     #     cycle_num = 1
#             else:
#                 if circuit[comp][1][2] - electrons_coordinates[0] > 0:
#                     electrons_coordinates = (electrons_coordinates[0]+elec_speed, electrons_coordinates[1])
#                 elif electrons_coordinates[0] - circuit[comp][1][2] > 0:
#                     electrons_coordinates = (electrons_coordinates[0]-elec_speed, electrons_coordinates[1])
#                 else:
#                     if type(circuit[comp][2]) != tuple:
#                         comp = circuit[comp][2]
#                         cycle_num = 1
#                     # else:
#                     #     old_comp = comp
#                     #     comp = []
#                     #     for i in circuit[old_comp][2]:
#                     #         comp.append(i)
#                     #     cycle_num = 1
#         elif comp[0] == "B" or comp[0] == "F":

#             # Inserting IMG
#             if comp[0] == "B":
#                 circuit['ON'+comp] = (None, (circuit[comp][1][0], circuit[comp][1][1], 'resources/images/on_180_b_img.png') , None)
#             if comp[0] == "F":
#                 circuit['ON'+comp] = (None, (circuit[comp][1][0], circuit[comp][1][1], 'resources/images/on_180_f_img/1.png') , None)


#             if cycle_num == 1:
#                 electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1]+70)
#                 cycle_num += 1
#             else:
#                 if circuit[comp][1][2][20] == "1" or circuit[comp][1][2][21] == "1":
#                     if electrons_coordinates[0] + elec_speed < circuit[comp][1][0]+130:
#                         electrons_coordinates = (electrons_coordinates[0]+elec_speed, electrons_coordinates[1])
#                     else:
#                         if type(circuit[comp][2]) != tuple:
#                             comp = circuit[comp][2]
#                             cycle_num = 1
#                         # else:
#                         #     old_comp = comp
#                         #     comp = []
#                         #     for i in circuit[old_comp][2]:
#                         #         comp.append(i)
#                         #     cycle_num = 1
#     return comp, electrons_coordinates



""" Pygame Setup """ 

# Initialize Pygame
pygame.init()

# Set up the window

window = pygame.display.set_mode()
WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()
print(WINDOW_WIDTH, WINDOW_HEIGHT)

pygame.display.set_caption("Circuit Debugger")










""" Creating simulation enviroment for circuit """ 



#Creating Linked list

circuit = create_a_linkedlist()
present = dict(circuit)




#Variables
component_selected = False
component = ''
init_mouse_pos = (0,0)
line_ending_point = (0,0)
DIVISION = 70
create_line = False
WIRE_COLOR = (0,0,0)
GRID_COLOR = (180,180,180)
simulation = False
line = "H"






# Set up colors
WHITE = (255, 255, 255)
OFF_WHITE = (200,200,200)
RED = (255, 0, 0)
LIGHT_BLUE = (64, 64, 128)
YELLOW = (255, 255, 102)



# Menu Tools Constants

tools = 5
rect_speed = 5
MENU_BUTTON_SIZE = 9600
TOOLS_BUTTON_SIZE = 5000
SCALED_GUI_SIZE = (200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)
BUTTON_SCALED_SIZE = (200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 200*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)


scaled_tool_size = (131.136, 131.136)



menu_scaled_tool_size = (480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 480*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)

point_scaled_tool_size = (100*WINDOW_WIDTH//TOOLS_BUTTON_SIZE, 100*WINDOW_WIDTH//TOOLS_BUTTON_SIZE)

# Playbutton:

playbutton_img = pygame.image.load("resources/images/play_button_img.png")

scaled_playbutton_size = (40*WINDOW_WIDTH//873, 40*WINDOW_WIDTH//873)

scaled_playbutton = pygame.transform.scale(playbutton_img, (scaled_playbutton_size))

scaled_playbutton.set_alpha(128)

playbutton_rect = scaled_playbutton.get_rect(topleft = (WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.09))


# Electron:

elec_speed = 7
comp = ""
cycle_num = 1





# Menu Button
menuIcon_img = pygame.image.load('resources/images/menu_icon.png')
menuIcon_img_size = menuIcon_img.get_size()
scaled_menuIcon_img = pygame.transform.scale(menuIcon_img, (menuIcon_img_size[0]*WINDOW_WIDTH//MENU_BUTTON_SIZE, menuIcon_img_size[1]*WINDOW_WIDTH//MENU_BUTTON_SIZE))
scaled_menuIcon_img_size = scaled_menuIcon_img.get_size()
menu_btn_x = WINDOW_WIDTH*0.01
menu_btn_y = WINDOW_HEIGHT*0.1
menu_btn_close_x = WINDOW_WIDTH*0.01
menu_btn_open_x = WINDOW_WIDTH*0.15
menu_open = False






# Importing Images

# Battery Images
battery_img = pygame.image.load('resources/images/battery.png')

# Bulb Images
bulbOn_img = pygame.image.load('resources/images/bulb_on.png')
menu_scaled_bulbOn_img = pygame.transform.scale(bulbOn_img, menu_scaled_tool_size)

# Fan Images
fanOn_img = pygame.image.load('resources/images/fan_on.gif')
menu_scaled_fanOn_img = pygame.transform.scale(fanOn_img, menu_scaled_tool_size)

# Battery Image
menu_scaled_battery_img = pygame.transform.scale(battery_img, menu_scaled_tool_size)

#Highlight Image
highlight_img = pygame.image.load('resources/images/highlight.png')
scaled_highlight_img = pygame.transform.scale(highlight_img, menu_scaled_tool_size)
button_highlight_img = pygame.transform.scale(highlight_img, BUTTON_SCALED_SIZE)

#Symbolic Images
symbol_size = (140, 140)
bulb_image = pygame.image.load('resources/images/off_180_b_img.png')
scaled_bulb_image = pygame.transform.scale(bulb_image, symbol_size)
fan_image = pygame.image.load('resources/images/off_180_f_img.png')
scaled_fan_image = pygame.transform.scale(fan_image, symbol_size)
battery_image = pygame.image.load('resources/images/on_0_ps_img.png')
scaled_battery_image = pygame.transform.scale(battery_image, symbol_size)
switch_image = pygame.image.load("resources/images/switch.png")
scaled_switch_image = pygame.transform.scale(switch_image, symbol_size)
menu_scaled_switch_image = pygame.transform.scale(switch_image, menu_scaled_tool_size)








mouse = pygame.mouse.get_pressed()
mouse_pos = pygame.mouse.get_pos()
    
# Main game loop
while True: 

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
               
            # checking if key "8" was pressed
            if event.key == pygame.K_8 and not simulation:
                james = 1 # a variable that counts for the last component inserted in the circuit dictionary.  
                for jomes in circuit: # this loop removes the last component inserted. 
                    if james == len(circuit):
                        remove_connection(circuit, jomes)
                        break
                    james+=1
            
            # checking if key "space" was pressed
            if event.key == pygame.K_SPACE:
                if simulation:
                    remove_animation(circuit)
                simulation = not simulation
                comp = 'PS1'
                cycle_num = 1





    # Interactivity of menu button
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    



    # Check whether menu button clicked or not.

    if is_clicked(((menu_btn_x, menu_btn_y),(menu_btn_x + scaled_menuIcon_img_size[0], menu_btn_y + scaled_menuIcon_img_size[1])), mouse_pos, mouse):
        # Opens or closes the menu bar
        menu_open = not menu_open
        if menu_btn_x == menu_btn_open_x:
            menu_btn_x = menu_btn_close_x
        elif menu_btn_x == menu_btn_close_x:
            menu_btn_x = menu_btn_open_x
    




    # Fill the background
    window.fill(OFF_WHITE)
    draw_grid(DIVISION)
   





    # Draw Tool Tab
    if menu_open:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05,WINDOW_WIDTH*0.2, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_x, menu_btn_y))

        # Draw Tools on Tab
        
        window.blit(menu_scaled_bulbOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))
        
        # Menu Bulb
        if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1),(WINDOW_WIDTH*0.05+menu_scaled_tool_size[0], (((WINDOW_HEIGHT-70)/(tools+1))*1) + menu_scaled_tool_size[1])), mouse_pos):
            window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1))
        if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*1),(WINDOW_WIDTH*0.05+menu_scaled_tool_size[0], (((WINDOW_HEIGHT-70)/(tools+1))*1) + menu_scaled_tool_size[1])), mouse_pos,mouse):
            component_selected = True
            component = 'bulb'
            mouse = (False, mouse[1], mouse[2])
            time.sleep(0.1)

        # Menu Fan
        window.blit(menu_scaled_fanOn_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*2))
        if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*2),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*2) + scaled_tool_size[1])), mouse_pos):
            window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*2))
        if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*2),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*2) + scaled_tool_size[1])), mouse_pos,mouse):
            component_selected = True
            component = "fan"
            mouse = (False, mouse[1], mouse[2])
            time.sleep(0.1)
        
        #Menu Battery
        window.blit(menu_scaled_battery_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*3))
        if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*3),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*3) + scaled_tool_size[1])), mouse_pos):
            window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*3))
        if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*3),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*3) + scaled_tool_size[1])), mouse_pos,mouse):
            component_selected = True
            component = "battery"
            mouse = (False, mouse[1], mouse[2])
            time.sleep(0.1)
        # Menu Switch
        window.blit(menu_scaled_switch_image, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*4))
        if is_hovering(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*4),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*4) + scaled_tool_size[1])), mouse_pos):
            window.blit(scaled_highlight_img, (WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT)/(tools+1))*4))
        if is_clicked(((WINDOW_WIDTH*0.05, ((WINDOW_HEIGHT-70)/(tools+1))*4),(WINDOW_WIDTH*0.05+scaled_tool_size[0], (((WINDOW_HEIGHT)/(tools+1))*4) + scaled_tool_size[1])), mouse_pos,mouse):
            component_selected = True
            component = "switch"
            mouse = (False, mouse[1], mouse[2])
            time.sleep(0.1)

    else:
        pygame.draw.rect(window, LIGHT_BLUE, (0, WINDOW_HEIGHT*0.05, WINDOW_WIDTH*0.06, WINDOW_HEIGHT), border_top_right_radius = 50)
        window.blit(scaled_menuIcon_img, (menu_btn_close_x, menu_btn_y))








    # Draw Wire
    if not simulation:
        if menu_open:
            if is_clicked(((WINDOW_WIDTH*0.2, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)), mouse_pos, mouse) and component_selected == False and is_clicked(((WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.09),(WINDOW_WIDTH*0.9+playbutton_rect.width,WINDOW_HEIGHT*0.09+playbutton_rect.height)) ,mouse_pos, mouse) != True:
                if create_line:  # Uses connect wire function to create a wire between two end points. 
                    connect_wire()


                create_line = not create_line
                init_mouse_pos = (near_DIVISION_multiple(DIVISION, mouse_pos[0]), near_DIVISION_multiple(DIVISION, mouse_pos[1]))
                time.sleep(0.2)
        else:
            if is_clicked(((WINDOW_WIDTH*0.06, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)), mouse_pos, mouse) and component_selected == False and is_clicked(((WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.09),(WINDOW_WIDTH*0.9+playbutton_rect.width,WINDOW_HEIGHT*0.09+playbutton_rect.height)) ,mouse_pos, mouse) != True:
                if create_line:  # Uses connect wire function to create a wire between two end points. 
                    connect_wire()

                create_line = not create_line
                init_mouse_pos = (near_DIVISION_multiple(DIVISION, mouse_pos[0]), near_DIVISION_multiple(DIVISION, mouse_pos[1]))
                time.sleep(0.2)


        if create_line:
            line_ending_point = (near_DIVISION_multiple(DIVISION, mouse_pos[0]), near_DIVISION_multiple(DIVISION, mouse_pos[1]))
            if abs(line_ending_point[0] - init_mouse_pos[0]) < abs(line_ending_point[1] - init_mouse_pos[1]):
                line_ending_point = (init_mouse_pos[0], line_ending_point[1])
            else:
                line_ending_point = (line_ending_point[0], init_mouse_pos[1])
            
            pygame.draw.line(window, WIRE_COLOR, 
                    [init_mouse_pos[0], init_mouse_pos[1]], 
                    [line_ending_point[0], line_ending_point[1]], 5)
        


    # Draw Component
    if component_selected:
        create_line = False
        if component == 'bulb':
            window.blit(scaled_bulb_image, (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70)))
        elif component == "fan":
            window.blit(scaled_fan_image, (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70)))
        elif component == "battery":
            window.blit(scaled_battery_image, (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70)))
        elif component == "switch":
            window.blit(scaled_switch_image, (near_DIVISION_multiple(DIVISION, mouse_pos[0]-70), near_DIVISION_multiple(DIVISION, mouse_pos[1]-70)))
        if mouse[0] == True:
            component_selected = False
            connect_component(component)
            time.sleep(0.2)
    

  
    display_circuit_from_linked_list(circuit)


    
    # Place the play button
    
    window.blit(scaled_playbutton, playbutton_rect)
    if is_hovering(((WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.09),(WINDOW_WIDTH*0.9+playbutton_rect.width,WINDOW_HEIGHT*0.09+playbutton_rect.height)) ,mouse_pos):
        button_highlight_img1 = pygame.transform.scale_by(button_highlight_img, 1.25)
        window.blit(button_highlight_img1, (WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.09))
    
    # Start the simulation
    components = list(circuit.keys())
    # Turns simulation On or Off:
    if is_clicked(((WINDOW_WIDTH*0.9,WINDOW_HEIGHT*0.09),(WINDOW_WIDTH*0.9+playbutton_rect.width,WINDOW_HEIGHT*0.09+playbutton_rect.height)) ,mouse_pos, mouse) and circuit[components[-1]][2] == "PS1":
        if simulation:
            remove_animation(circuit)
        simulation = not simulation
        comp = 'PS1'
        cycle_num = 1
        time.sleep(0.2)
    if ("switch" in circuit and is_clicked(((circuit["switch"][1][0], circuit["switch"][1][1]), (circuit["switch"][1][0]+140, circuit["switch"][1][1]+140)), mouse_pos, mouse)):
            circuit["switch"] = (circuit["switch"][0], (circuit["switch"][1][0], circuit["switch"][1][1], circuit["switch"][1][2], not circuit["switch"][1][3]), circuit["switch"][2])
            time.sleep(0.2)
    
    if True: #complete_circuit( circuit):
        if "switch" not in circuit or circuit["switch"][1][3]:
            if simulation:
                if type(comp) != list:
                    if comp[:2] == "PS":
                        if cycle_num == 1:
                            electrons_coordinates = (circuit[comp][1][0]+70, circuit[comp][1][1]+70)
                            cycle_num += 1
                        if electrons_coordinates[0]+elec_speed < circuit[comp][1][0]+130:
                            pygame.draw.line(window,YELLOW, electrons_coordinates, (electrons_coordinates[0]+10, electrons_coordinates[1]), 5)
                            electrons_coordinates = (electrons_coordinates[0]+elec_speed, electrons_coordinates[1])
                        else:
                            if type(circuit[comp][2]) != tuple:
                                comp = circuit[comp][2]
                                cycle_num = 1
                            else:
                                old_comp = comp
                                comp = []
                                for i in circuit[old_comp][2]:
                                    comp.append(i)
                                cycle_num = 1
                    else:
                        if comp[0] =="L":
                            if cycle_num == 1:
                                electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1])
                                cycle_num += 1
                            if circuit[comp][1][0] == circuit[comp][1][2]:
                                if circuit[comp][1][3] - electrons_coordinates[1] > 0:
                                    pygame.draw.line(window,YELLOW, electrons_coordinates, (electrons_coordinates[0], electrons_coordinates[1]+10), 5)
                                    electrons_coordinates = (electrons_coordinates[0], electrons_coordinates[1]+elec_speed)
                                elif electrons_coordinates[1] - circuit[comp][1][3] > 0:
                                    pygame.draw.line(window,YELLOW, electrons_coordinates, (electrons_coordinates[0], electrons_coordinates[1]-10), 5)
                                    electrons_coordinates = (electrons_coordinates[0], electrons_coordinates[1]-elec_speed)
                                else:
                                    if type(circuit[comp][2]) != tuple:
                                        comp = circuit[comp][2]
                                        cycle_num = 1
                                    else:
                                        old_comp = comp
                                        comp = []
                                        for i in circuit[old_comp][2]:
                                            comp.append(i)
                                        cycle_num = 1
                            else:
                                if circuit[comp][1][2] - electrons_coordinates[0] > 0:
                                    pygame.draw.line(window,YELLOW, electrons_coordinates, (electrons_coordinates[0]+10, electrons_coordinates[1]), 5)
                                    electrons_coordinates = (electrons_coordinates[0]+elec_speed, electrons_coordinates[1])
                                elif electrons_coordinates[0] - circuit[comp][1][2] > 0:
                                    pygame.draw.line(window,YELLOW, electrons_coordinates, (electrons_coordinates[0]-10, electrons_coordinates[1]), 5)
                                    electrons_coordinates = (electrons_coordinates[0]-elec_speed, electrons_coordinates[1])
                                else:
                                    if type(circuit[comp][2]) != tuple:
                                        comp = circuit[comp][2]
                                        cycle_num = 1
                                    else:
                                        old_comp = comp
                                        comp = []
                                        for i in circuit[old_comp][2]:
                                            comp.append(i)
                                        cycle_num = 1
                        elif comp[0] == "B" or comp[0] == "F":

                            # Inserting IMG
                            if comp[0] == "B":
                                circuit['ON'+comp] = (None, (circuit[comp][1][0], circuit[comp][1][1], 'resources/images/on_180_b_img.png') , None)
                            if comp[0] == "F":
                                circuit['ON'+comp] = (None, (circuit[comp][1][0], circuit[comp][1][1], 'resources/images/on_180_f_img/1.png') , None)


                            if cycle_num == 1:
                                electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1]+70)
                                cycle_num += 1
                            else:
                                if circuit[comp][1][2][20] == "1" or circuit[comp][1][2][21] == "1":
                                    if electrons_coordinates[0] + elec_speed < circuit[comp][1][0]+130:
                                        pygame.draw.line(window, YELLOW, electrons_coordinates, (electrons_coordinates[0]+10, electrons_coordinates[1]), 5)
                                        electrons_coordinates = (electrons_coordinates[0]+elec_speed, electrons_coordinates[1])
                                    else:
                                        if type(circuit[comp][2]) != tuple:
                                            comp = circuit[comp][2]
                                            cycle_num = 1
                                        else:
                                            old_comp = comp
                                            comp = []
                                            for i in circuit[old_comp][2]:
                                                comp.append(i)
                                            cycle_num = 1
                else:
                    if cycle_num == 1:
                        electrons_coordinates = []
                        prev = circuit[comp[0]][0]
                        for _ in range(len(comp)):
                            if prev[:2] == "PS" or prev[0] == "B" or prev[0] == "F":
                                electrons_coordinates.append((circuit[prev][1][0]+140, circuit[prev][1][1]+70))
                            else:
                                electrons_coordinates.append((circuit[prev][1][2], circuit[prev][1][3]))
                        cycle_num += 1
                    else:
                        for i in range(len(comp)):
                            if comp[i] != None:
                                if comp[i][:2] == "PS":
                                    if electrons_coordinates[i][0]+elec_speed < circuit[comp[i]][1][0]+130:
                                        pygame.draw.line(window,YELLOW, electrons_coordinates[i], (electrons_coordinates[i][0]+10, electrons_coordinates[i][1]), 5)
                                        electrons_coordinates[i] = (electrons_coordinates[i][0]+elec_speed, electrons_coordinates[i][1])
                                    else:
                                        comp[i] = circuit[comp[i]][2]
                                        if type(circuit[comp[i]][0]) != tuple:
                                            if comp[i][0] == "L":
                                                electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1])
                                            else:
                                                electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1]+70)
                                        else:
                                            if counter(comp) > 1:
                                                comp[i] = None
                                                electrons_coordinates[i] = None
                                            else:
                                                comp = comp[i]
                                                electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1])
                                        
                                else:
                                    if comp[i][0] =="L":
                                        if circuit[comp[i]][1][0] == circuit[comp[i]][1][2]:
                                            if circuit[comp[i]][1][3] - electrons_coordinates[i][1] > 0:
                                                pygame.draw.line(window,YELLOW, electrons_coordinates[i], (electrons_coordinates[i][0], electrons_coordinates[i][1]+10), 5)
                                                electrons_coordinates[i] = (electrons_coordinates[i][0], electrons_coordinates[i][1]+elec_speed)
                                            elif electrons_coordinates[i][1] - circuit[comp[i]][1][3] > 0:
                                                pygame.draw.line(window,YELLOW, electrons_coordinates[i], (electrons_coordinates[i][0], electrons_coordinates[i][1]-10), 5)
                                                electrons_coordinates[i] = (electrons_coordinates[i][0], electrons_coordinates[i][1]-elec_speed)
                                            else:
                                                comp[i] = circuit[comp[i]][2]
                                                if type(circuit[comp[i]][0]) != tuple:
                                                    if comp[i][0] == "L":
                                                        electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1])
                                                    else:
                                                        electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1]+70)
                                                else:
                                                    if counter(comp) > 1:
                                                        comp[i] = None
                                                        electrons_coordinates[i] = None
                                                    else:
                                                        comp = comp[i]
                                                        electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1])
                                        else:
                                            if circuit[comp[i]][1][2] - electrons_coordinates[i][0] > 0:
                                                pygame.draw.line(window,YELLOW, electrons_coordinates[i], (electrons_coordinates[i][0]+10, electrons_coordinates[i][1]), 5)
                                                electrons_coordinates[i] = (electrons_coordinates[i][0]+elec_speed, electrons_coordinates[i][1])
                                            elif electrons_coordinates[i][0] - circuit[comp[i]][1][2] > 0:
                                                pygame.draw.line(window,YELLOW, electrons_coordinates[i], (electrons_coordinates[i][0]-10, electrons_coordinates[i][1]), 5)
                                                electrons_coordinates[i] = (electrons_coordinates[i][0]-elec_speed, electrons_coordinates[i][1])
                                            else:
                                                comp[i] = circuit[comp[i]][2]
                                                if type(circuit[comp[i]][0]) != tuple:
                                                    if comp[i][0] == "L":
                                                        electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1])
                                                    else:
                                                        electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1]+70)
                                                else:
                                                    if counter(comp) > 1:
                                                        comp[i] = None
                                                        electrons_coordinates[i] = None
                                                    else:
                                                        comp = comp[i]
                                                        electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1])
                                    elif comp[i][0] == "B" or comp[i][0] == "F":
                                        # Inserting IMG
                                        if comp[i][0] == "B":
                                            circuit['ON'+comp[i]] = (None, (circuit[comp[i]][1][0], circuit[comp[i]][1][1], 'resources/images/on_180_b_img.png') , None)
                                        if comp[i][0] == "F":
                                            circuit['ON'+comp[i]] = (None, (circuit[comp[i]][1][0], circuit[comp[i]][1][1], 'resources/images/on_180_f_img/1.png') , None)


                                    
                                        if circuit[comp[i]][1][2][20] == "1" or circuit[comp[i]][1][2][21] == "1":
                                            if electrons_coordinates[i][0] + elec_speed < circuit[comp[i]][1][0]+130:
                                                pygame.draw.line(window, YELLOW, electrons_coordinates[i], (electrons_coordinates[i][0]+10, electrons_coordinates[i][1]), 5)
                                                electrons_coordinates[i] = (electrons_coordinates[i][0]+elec_speed, electrons_coordinates[i][1])
                                            else:
                                                comp[i] = circuit[comp[i]][2]
                                                if type(circuit[comp[i]][0]) != tuple:   
                                                    if comp[i][0] == "L": 
                                                        electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1])
                                                    else:
                                                        electrons_coordinates[i] = (circuit[comp[i]][1][0], circuit[comp[i]][1][1]+70)
                                                else:
                                                    if counter(comp) > 1:
                                                        comp[i] = None
                                                        electrons_coordinates[i] = None
                                                    else:
                                                        comp = comp[i]
                                                        electrons_coordinates = (circuit[comp][1][0], circuit[comp][1][1])
            else:
                comp = "PS1"
                cycle_num = 1
                count = 0
                for i in circuit:
                    if i[:2] == "ON":
                        count += 1
                while count > 0:
                    del circuit[components[-count]]
                    count -= 1                                    
    


                    


                        
    if present != circuit:
        print()
        present = dict(circuit)
        print(circuit)
        print()


    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)