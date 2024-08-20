from questions import question_objects

class Quiz():
    house_score = {
        "slytherin": 0,
        "ravenclaw": 0,
        "hufflepuff": 0,
        "gryffindor": 0
    }

    def get_questions(self):
        return question_objects
    
    def get_results(self, answers: list) -> str:

        for answer in answers:
            question_obj = next((
                q for q in question_objects if q.get('order') == answer.question_number
            ), None)
            house_mapping = question_obj.get('house_maping')
            house = list(house_mapping.keys())[list(house_mapping.values()).index(answer.selected_answer)]
            self.house_score[house] += 1
        print(self.house_score)
        return max(self.house_score, key=self.house_score.get)




quiz = Quiz()