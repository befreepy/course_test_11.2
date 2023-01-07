import json

""""– возвращает список всех кандидатов """


def load_candidates_from_json():
    with open('candidates.json', "r", encoding='utf8') as file:
        return json.load(file)


"""– возвращает одного кандидата по его id"""


def get_all():
    return load_candidates_from_json()


""""– возвращает кандидатов по имени"""


def get_candidate_by_id(pk):
    for candidate in load_candidates_from_json():
        if candidate['id'] == pk:
            return candidate
    return 'Not found'


def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


"""возвращает кандидатов по навыку"""


def get_candidates_by_skill(skill):
    result = []
    for candidate in load_candidates_from_json():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result
