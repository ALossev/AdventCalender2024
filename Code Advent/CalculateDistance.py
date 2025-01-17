from collections import Counter
def read_list_from_file(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list
def calculate_total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    total_distance = sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))
    return total_distance


def calculate_similarity_score(left_list, right_list):
    right_counts = Counter(right_list)
    
    similarity_score = sum(left * right_counts[left] for left in left_list)
    
    return similarity_score
file_path = 'numberList.txt'

left_list, right_list = read_list_from_file(file_path)

total_distance = calculate_total_distance(left_list, right_list)
print("Total Distance:", total_distance)

similarity_score = calculate_similarity_score(left_list, right_list)
print("Similarity Score:", similarity_score)