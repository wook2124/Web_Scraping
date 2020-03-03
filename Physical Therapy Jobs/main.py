from pt_indeed import get_jobs as get_indeed_jobs
from save import save_file

indeed_jobs = get_indeed_jobs()

jobs = indeed_jobs 
save_file(jobs)

# https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%EB%AC%BC%EB%A6%AC%EC%B9%98%EB%A3%8C&limit=50&radius=25