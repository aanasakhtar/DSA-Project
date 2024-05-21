def create_a_linkedlist(): # Creates the linked list:
    return {}

def form_connection(linked_list, ID, pre_ID, data, next_ID): # Connects two components:
    if ID == "switch":
        linked_list[ID] = (None, (data[0], data[1], data[2], True), "PS1")
    else:
        linked_list[ID] = (pre_ID, data, next_ID)

def remove_connection(linked_list, ID): # Removes connections of the whole circuit:
    del linked_list[ID]
    for i in linked_list:
        if linked_list[i][0] == ID:
            linked_list[i] = (None, linked_list[i][1], linked_list[i][2])
        if linked_list[i][2] == ID:
            linked_list[i] = (linked_list[i][0], linked_list[i][1], None)


def get_node_data(linked_list, ID): # Returns data of a particular component with key ID:
    return linked_list[ID][1]



def length_of_linkedlist(linked_list): # Returns the number of components in the system:
    return len(linked_list.keys())



def display_linked_list(linked_list, starting_node):
    current_ID = linked_list[starting_node]
    lst = []
    while current_ID[2] != None:
        current_ID = linked_list[current_ID[2]]
        lst.append(current_ID)
    return lst


def last_node_ID(linked_list):
    current_ID = "PS1"
    while linked_list[current_ID][2] != None:
        current_ID = linked_list[current_ID][2]
    return current_ID
        
