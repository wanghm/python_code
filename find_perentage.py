if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_scores = student_marks[query_name]
    
    sum_score = 0
    for i in range(len(query_scores)):
        sum_score += query_scores[i]
    print("{:.2f}".format(sum_score / len(query_scores), 2))

