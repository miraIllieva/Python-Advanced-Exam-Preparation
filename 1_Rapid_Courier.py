from collections import deque

packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])

total_deliver = 0

while packages and couriers:
    current_packages = packages[-1]
    current_couriers = couriers[0]

    if current_couriers >= current_packages:
        capacity = current_couriers - current_packages * 2
        couriers.popleft()
        if capacity > 0:
            couriers.append(capacity)
        total_deliver += packages.pop()
    else:
        packages[-1] -= couriers.popleft()
        total_deliver += current_couriers

print(f"Total weight: {total_deliver} kg")

if not packages and not couriers:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
if packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join([str(el) for el in packages])}")
if couriers and not packages:
    print(f"Couriers are still on duty: {', '.join([str(el) for el in couriers2 ])} but there are no more packages to deliver.")
