def solution(participant, completion):
    complete = {}

    for person in participant:
        complete[person] = 1 + complete.get(person, 0)

    for person in completion:
        complete[person] -= 1

    for person, count in complete.items():
        if count > 0:
            return person
