import math

def main():
    can_sizes = [
        [ "#1 Picnic", 6.83, 10.16, 0.28 ],
        [ "#1 Tall", 7.78, 11.91, 0.43 ],
        [ "#2", 8.73, 11.59, 0.45 ],
        [ "#2.5", 10.32, 11.91, 0.61 ],
        [ "#3 Cylinder", 10.79, 17.78, 0.86 ],
        [ "#5", 13.02, 14.29, 0.83 ],
        [ "#6Z", 5.40, 8.89, 0.22 ],
        [ "#8Z short", 6.83, 7.62, 0.26 ],
        [ "#10", 15.72, 17.78, 1.53 ],
        [ "#211", 6.83, 12.38, 0.34 ],
        [ "#300", 7.62, 11.27, 0.38 ],
        [ "#303", 8.10, 11.11, 0.42 ]
    ]
    best_storage = 0
    best_storage_name = ""
    best_cost = 0
    best_cost_name = ""
    for can in can_sizes:
        name = can[0]
        radius = can[1]
        height = can[2]
        cost = can[3]
        storage_efficiency = compute_storage_efficiency(radius,height)
        cost_efficiency = compute_cost_efficiency(radius,height,cost)
        print(f"{name} {storage_efficiency:.2f} {cost_efficiency:.2f}")
        if storage_efficiency > best_storage:
            best_storage = storage_efficiency
            best_storage_name = name
        if cost_efficiency > best_cost:
            best_cost = cost_efficiency
            best_cost_name = name
    print("")
    print(f"{best_storage_name} has the best can storage efficiency")
    print(f"{best_cost_name} has the best can cost efficiency")

def compute_volume(radius,height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius,height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius,height):
    volume = compute_volume(radius,height)
    area = compute_surface_area(radius,height)
    return volume / area

def compute_cost_efficiency(radius,height,cost):
    volume = compute_volume(radius,height)
    return volume / cost

main()