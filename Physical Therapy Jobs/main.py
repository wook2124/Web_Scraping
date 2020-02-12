from pt_indeed import get_jobs as get_indeed_jobs
from save import save_file


indeed_jobs = get_indeed_jobs()

jobs = indeed_jobs 
save_file(jobs)