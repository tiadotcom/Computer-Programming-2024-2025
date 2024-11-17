# File with the scores
scores_file = 'scores.txt'

scores = {}
fin = open(scores_file)
for line in fin:
    data = line.strip().split(': ')
    # print(data)
    if data[0]: # the line is not empty
        # an empty line separates the records in the file
        if data[0] == 'Matr':
            # the matriculation number is used as the key
            matr = data[1]
            scores[matr] = {}
        else:
            scores[matr][data[0]] = data[1]

print('Dataset:', scores)

# Compute the average score in each course
# Create the dictionary with the list of scores for each course
course_scores = {}
for s in scores:
    for c in scores[s]:
        if c not in course_scores:
            course_scores[c] = []
        course_scores[c].append(int(scores[s][c]))
print("Scores per courses:", course_scores)
# Print the average score
print('\nAverage scores:')
for c in course_scores:
    print(c, ':', round((sum(course_scores[c])/len(course_scores[c])), 1))

