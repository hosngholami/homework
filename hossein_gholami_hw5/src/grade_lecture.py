def grade_lecture(lectures):
    for key, value in lectures.items():
        grade = input(f'enter grade for lecture {key}: ')
        lectures[key] = grade
    return lectures 