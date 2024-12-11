from dataclasses import dataclass

with open("inputs/09.txt") as input:
    data = input.readline()
    data = data.strip()
    data = [int(c) for c in data]

def get_checksum(file_id, start_pos, end_pos) -> int:
    return file_id * ((end_pos-1)*end_pos/2 - (start_pos-1)*start_pos/2)

@dataclass
class Segment():
    id: int | None
    length: int
    data: bool
    attemped_move: bool | None

    def __repr__(self) -> str:
        return(f"({self.id}, {self.length}, {self.data})")

segments: list[Segment] = []

for i, d in enumerate(data):
    if i % 2 == 0:
        segments.append(Segment(
            id=i //2,
            length=d,
            data=True,
            attemped_move=False,
        ))
    else:
        segments.append(Segment(
            id=None,
            length=d,
            data=False,
            attemped_move=None,
        ))

def find_spot(segments: list[Segment], segment: Segment) -> int:
    """Find an index at which segment fits."""
    for i, s in enumerate(segments):
        if s.data == False and s.length >= segment.length:
            return i
    return -1

def find_last_unmoved_segment(segments: list[Segment]) -> int:
    """Find index of last unmoved segment."""
    for i, s in reversed(list(enumerate(segments))):
        if s.attemped_move is False:
            return i
    return -1

def join_empty_segments(segments: list[Segment]) -> list[Segment]:
    # Remove empty segments
    i = 0
    while i < len(segments):
        while segments[i].length == 0:
            segments = segments[:i] + segments[i+1:]
        i += 1

    i = 0
    while i < len(segments):
        s0 = segments[i]
        if s0.data == False:
            while i+1 < len(segments) and segments[i+1].data == False:
                s0 = Segment(None, s0.length + segments[i+1].length, False, None)
                segments = segments[:i] + [s0] + segments[i+2:]
        i += 1

    return segments

### Move stuff around
segments = join_empty_segments(segments)
while True:
    #print(str(segments))
    next_segment_to_move = find_last_unmoved_segment(segments)
    #print(next_segment_to_move)
    if next_segment_to_move == -1:
        break

    segments[next_segment_to_move].attemped_move = True

    target_spot = find_spot(segments, segments[next_segment_to_move])
    if target_spot == -1 or target_spot > next_segment_to_move:
        continue

    segment = segments[next_segment_to_move]

    ### Remove segment from old spot
    segments[next_segment_to_move] = Segment(None, segment.length, False, None)

    ### Add segment to new spot
    old_space = segments[target_spot]
    segments[target_spot] = segment
    if segment.length < old_space.length:
        segments = segments[:target_spot+1] + [Segment(None, old_space.length-segment.length, False, None)] + segments[target_spot+1:]

    
    segments = join_empty_segments(segments)


### Calculate checksum
checksum = 0
position = 0
for segment in segments:
    if segment.data:
        checksum += get_checksum(segment.id, position, position + segment.length)
    position += segment.length

print(checksum)