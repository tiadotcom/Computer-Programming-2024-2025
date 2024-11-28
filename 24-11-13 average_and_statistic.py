d = {
    '120012': {'Operating Systems': 29, 'Mathematics': 19, 'Programming': 28, 'Databases': 24},
    '120230': {'Mathematics': 19, 'Statistics': 30, 'Programming': 27, 'Algorithms': 21},
    '121320': {'Statistics': 30, 'Programming': 27, 'Mathematics': 30, 'Databases': 25}
}

subj_list = {}

def find_avrg_marks(d):
    for student in d:
        for subj, mark in d[student].items():
            if subj not in subj_list:
                subj_list[subj] = {"Sum": mark, "Count": 1}
            else:
                subj_list[subj]["Sum"] += mark
                subj_list[subj]["Count"] += 1
    average_marks = {subj: round((subj_list[subj]["Sum"] / subj_list[subj]['Count']), 1) for subj in subj_list}
    print("Average marks =", average_marks)

def find_best_student(d, subj):
    best_student = None
    best_score = -1
    for student, aux_d in d.items():
        if subj in aux_d and aux_d[subj] > best_score:
            best_score = aux_d[subj]
            best_student = student
    return best_student

# Calculate average marks
find_avrg_marks(d)

# Create a dictionary to store the best student for each subject
best_students = {subj: find_best_student(d, subj) for subj in subj_list}
print("Best students =", best_students)
