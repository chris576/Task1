import math

problem_size_56 = math.pow(2, 56)
problem_size_512 = math.pow(2, 512-1)

cpu_time_56 = problem_size_56 / (3.3*10**7)
gpu_time_56 = problem_size_56 / (14.0 * 10**7)
cloud_time = problem_size_56 / (92.5 * 10**7)

cpu_time_512 = problem_size_512 / (3.3*10**7)
gpu_time_512 = problem_size_512 / (14.0 * 10**7)
cloud_time_512 = problem_size_512 / (92.5 * 10**7)

print((cpu_time_56 / 60 / 60 / 24 / 356))
print((gpu_time_56 / 60 / 60 / 24 / 356))
print((cloud_time / 60 / 60))

print((cpu_time_512 // 60 // 60 // 24 // 365))
print((gpu_time_512 // 60 // 60 // 24 // 365))
print((cloud_time_512 // 60 // 60 // 24 // 365))


