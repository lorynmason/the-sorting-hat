from questions import question_objects

house_score = {
    "slytherin": 0,
    "ravenclaw": 0,
    "hufflepuff": 0,
    "gryffindor": 0
}

for question_obj in question_objects:
    question = question_obj.get('question')
    options = question_obj.get('options')
    house_mapping = question_obj.get('house_maping')
    # ask question and show options
    print(question)
    for k, v in options.items():
        print(f"{k}) {v}")
    # get input 
    answer = input(question)

    # update house score
    for k, v in house_mapping.items():
        if v == answer:
            house_score[k] += 1


# show house with the most points

print(f"YOU'RE IN {max(house_score, key=house_score.get).upper()}!!!!")
print(house_score)

