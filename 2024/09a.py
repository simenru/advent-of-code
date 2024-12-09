with open("inputs/09.txt") as input:
    data = input.readline()
    data = data.strip()
    data = [int(c) for c in data]

def get_checksum(file_id, start_pos, end_pos) -> int:
    return file_id * ((end_pos-1)*end_pos/2 - (start_pos-1)*start_pos/2)

back_element_index = len(data)-1
if back_element_index % 2 == 1:
    back_element_index -= 1
back_element_remaining = data[back_element_index]

checksum = 0
position = 0



for i in range(len(data)):
    print(i, checksum, position, back_element_index, back_element_remaining)
    if i > back_element_index:
        break
    if i == back_element_index:
        checksum += get_checksum(i//2, position, position + back_element_remaining)
        break
    if i % 2 == 0:
        # File
        checksum += get_checksum(i//2, position, position + data[i])
        position += data[i]
        continue
    # Empty space - need to backfill
    space_length = data[i]
    while space_length > 0:
        print(" ", i, checksum, position, back_element_index, back_element_remaining)
        while back_element_remaining <= 0:
            back_element_index -= 2
            if back_element_index < i:
                print(checksum)
                exit()
            back_element_remaining = data[back_element_index]
        
        if back_element_remaining >= space_length:
            checksum += get_checksum(back_element_index//2, position, position + space_length)
            back_element_remaining -= space_length
            position += space_length
            space_length = 0
            continue
        
        checksum += get_checksum(back_element_index//2, position, position + back_element_remaining)
        position += back_element_remaining
        space_length -= back_element_remaining
        back_element_remaining = 0

print(checksum)