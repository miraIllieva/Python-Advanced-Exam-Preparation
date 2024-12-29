def boarding_passengers(ship_capacity, *passengers_list):
    program_data = {}
    total_to_board = sum([group[0] for group in passengers_list])

    for count, group_name in passengers_list:
        if ship_capacity == 0:
            break  # Stop if the ship is full

        if count <= ship_capacity:  # Can board this group
            if group_name not in program_data:
                program_data[group_name] = 0
            program_data[group_name] += count
            ship_capacity -= count

    total_onboarded = sum(program_data.values())
    unaborded_guest = total_to_board - total_onboarded

    # Sort the boarding details
    sorted_data = sorted(program_data.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    # Build result
    result = "Boarding details by benefit plan:\n"
    for group_name, count in sorted_data:
        result += f"## {group_name}: {count} guests\n"

    # Final message
    if unaborded_guest == 0:
        result += "All passengers are successfully boarded!"
    elif ship_capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {ship_capacity}."

    return result
