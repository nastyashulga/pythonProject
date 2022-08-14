import json
from candidates import Candidate

def load_candidates(file):
    """
    загрузит данные из файла
    """
    with open(file, 'r', encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates

def get_all(candidates):
    """
    покажет всех кандидатов
    """
    list_candidates = []
    for item in candidates:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        list_candidates.append(candidate)
    return list_candidates

def get_by_pk(pk, list_candidates):
    """
    вернет кандидата по pk
    """
    for item in list_candidates:
        if item.pk == pk:
            return item

def get_by_skill(skill_name, list_candidates):
    """
    вернет кандидатов по навыку
    """
    skills_list = []
    for item in list_candidates:
        if skill_name in item.skills:
            skills_list.append(item)
    return skills_list