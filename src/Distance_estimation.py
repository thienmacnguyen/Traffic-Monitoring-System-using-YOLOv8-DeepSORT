def estimate_distance(bbox, class_id):
    height_pixel = bbox[3] - bbox[1]
    if height_pixel <= 0:
        return -1

    real_heights = {
        0: 1.55,   # human
        1: 1.0,   # bike
        2: 1.5,   # car
        3: 1.2,   # motor
        5: 3.5,   # bus
        7: 4.0    # truck
    }
    real_height = real_heights.get(class_id, 1.7)
    f = 800  # tiêu cự giả định
    distance_m = (f * real_height) / height_pixel
    return round(distance_m, 2)
