from Pipeline import Pipeline
from Pipeline import append_pipeline
from Pipeline import execute_pipeline



append_pipeline(lambda Pipeline(), x: _ , x)
plus_10 = lambda x: x + 10
append_pipeline(plus_10)

print(execute_pipeline())