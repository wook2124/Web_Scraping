from indeed import get_jobs as get_indeed_jobs
from sof import get_jobs as get_sof_jobs
from save import save_file


indeed_jobs = get_indeed_jobs()
# sof_jobs = get_sof_jobs()

jobs = indeed_jobs 
# + sof_jobs
save_file(jobs)