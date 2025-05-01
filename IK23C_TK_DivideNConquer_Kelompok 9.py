import math
import random

# Fungsi menghitung jarak Euclidean
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Brute force jika jumlah titik <= 3
def brute_force(points):
    min_dist = float('inf')
    closest_pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    return closest_pair, min_dist

# Cari jarak terdekat dalam strip (titik-titik di sekitar garis tengah)
def strip_closest(strip, d_min):
    min_dist = d_min
    closest_pair = None
    strip.sort(key=lambda point: point[1])  # Urutkan berdasarkan y

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (strip[i], strip[j])

    return closest_pair, min_dist if closest_pair else (None, d_min)

# Divide and Conquer utama
def closest_pair_recursive(points_sorted_x):
    n = len(points_sorted_x)

    if n <= 3:
        return brute_force(points_sorted_x)

    mid = n // 2
    left_points = points_sorted_x[:mid]
    right_points = points_sorted_x[mid:]

    left_pair, left_dist = closest_pair_recursive(left_points)
    right_pair, right_dist = closest_pair_recursive(right_points)

    if left_dist < right_dist:
        d_min = left_dist
        closest_pair = left_pair
    else:
        d_min = right_dist
        closest_pair = right_pair

    # Garis tengah x
    mid_x = points_sorted_x[mid][0]
    strip = [p for p in points_sorted_x if abs(p[0] - mid_x) < d_min]

    strip_pair, strip_dist = strip_closest(strip, d_min)
    if strip_pair and strip_dist < d_min:
        return strip_pair, strip_dist

    return closest_pair, d_min

# Fungsi utama
def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda point: point[0])
    return closest_pair_recursive(points_sorted_x)

# Fungsi bantu untuk menampilkan hasil
def run_test_case(title, points):
    print(f"\n {title}")
    print(f"Jumlah titik: {len(points)}")
    pair, distance = closest_pair(points)
    print("Pasangan titik terdekat:", pair)
    print("Jarak terdekat:", distance)

# =====================
# CONTOH INPUT
# =====================

if __name__ == "__main__":
    # Contoh 1: 10 titik
    points1 = [(10, 20), (15, 24), (18, 27), (50, 60), (60, 70),
               (70, 80), (100, 110), (5, 25), (20, 28), (11, 21)]

    # Contoh 2: 20 titik
    points2 = [(10, 5), (2, 3), (50, 50), (3, 4), (100, 100), (5, 6),
               (40, 41), (60, 62), (70, 72), (90, 91), (10, 8), (11, 7),
               (12, 6), (13, 5), (15, 3), (16, 2), (17, 1), (18, 0),
               (55, 60), (56, 59)]

    # Contoh 3: 50 titik acak
    random.seed(1)
    points3 = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(50)]

    # Jalankan semua test case
    run_test_case("Contoh 1 - 10 Titik", points1)
    run_test_case("Contoh 2 - 20 Titik", points2)
    run_test_case("Contoh 3 - 50 Titik (Acak)", points3)
