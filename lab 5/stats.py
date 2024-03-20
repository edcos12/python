import statistics

# task 4

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"


grades = [int(num) for num in data.split(',')]

min_grades = min(grades)
max_grades = max(grades)

average = round(sum(grades) / len(grades), 2)
mean = round(statistics.mean(grades), 2)
median = round(statistics.median(grades))

print('''
      minimum grade: {} 
      maximum grade: {} 
      average grade: {} 
      mean grade: {} 
      median grade: {}'''.format(min_grades, max_grades, average, mean, median ))