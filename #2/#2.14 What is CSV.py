# main.py에 import save_file을 해주고
# save_file(jobs)를 불러오도록 준비해줌
from indeed import get_jobs as get_indeed_jobs
from sof import get_jobs as get_sof_jobs
from save import save_file


indeed_jobs = get_indeed_jobs()
# sof_jobs = get_sof_jobs()

jobs = indeed_jobs 
# + sof_jobs
save_file(jobs)


# save.py를 만들어서 csv작업준비를 함
import csv

def save_file(jobs):
  return