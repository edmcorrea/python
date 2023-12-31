from typing import List, Dict
from src.insights.jobs import read


# A função funciona similar a função "get_unique_job_types" no file "./jobs"
def get_unique_industries(path: str) -> List[str]:
    jobsDecoded = read(path)
    industry = set()
    for job in jobsDecoded:
        industry.add(job['industry'])
    industry = list(filter(None, industry))
    return industry


# A função deve retornar uma lista de dicionários com todos os empregos
# onde a coluna industry corresponde ao parâmetro industry.
def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industries = [job for job in jobs if job["industry"] == industry]
    return industries
