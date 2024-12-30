
def accommodate(*guests, **rooms):
    rooms_sorted = sorted(rooms.items(), key=lambda x: (x[1], x[0]))

    accommodations = {}
    not_accommodate = 0

    for guest in guests:
        for room in rooms_sorted:
            if room[1] >= guest:
                accommodations[room[0][-3:]] = guest
                rooms_sorted.remove(room)
                break
        else:
            not_accommodate += guest
    result = []
    if accommodations:
        result.append(f"A total of {len(accommodations)} accommodations were completed!")
        for room, guest in sorted(accommodations.items()):
            result.append(f"<Room {room} accommodates {guest} guests>")

    else:
        result.append("No accommodations were completed!")
    if not_accommodate:
        result.append(f"Guests with no accommodation: {not_accommodate}")
    if rooms_sorted:
        result.append(f"Empty rooms: {len(rooms_sorted)}")

    return "\n".join(result)




print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))

print(accommodate(10, 9, 8,room_307=6, room_802=5))
