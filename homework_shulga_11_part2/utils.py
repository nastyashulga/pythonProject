import json
from homework_shulga_11_part2.candidates import Candidate

def load_candidates_from_json(file):
    """
    возвращает список всех кандидатов
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
        candidate = Candidate(item['id'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        list_candidates.append(candidate)
    return list_candidates

def get_candidate(id, list_candidates):
    """
    возвращает одного кандидата по его id
    """
    for item in list_candidates:
        if item.id == id:
            return item

def get_candidates_by_name(name, list_candidates):
    """
    возвращает кандидатов по имени
    """
    for item in list_candidates:
        if item.name.lower() == name.lower():
            return item

def get_candidates_by_skill(skill_name, list_candidates):
    """
    возвращает кандидатов по навыку
    """
    skills_list = []
    for item in list_candidates:
        if skill_name.lower() in item.skills.lower():
            skills_list.append(item)
    return skills_list


