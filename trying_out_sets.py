from pprint import pprint as pp

students = ["Amy", "Ben", "Charlie", "Deb", "Fred", "Deb", "Gary", "Heather", "Ian", "Janice", "Katie"]

students_taking_art = ("John", "Beth", "Daniel")

students_taking_stats = [students[0], "John", students[9]]

chemistry = {students[1], students[1], students[3], students[2], students[6]}

biology = {students[3], students[1], students[0], students[7], students[9]}

algebra = set(chemistry.union(biology))

art = set(students_taking_art)

stats = set(students_taking_stats)


print("Union example 1:\n", "students taking either chemistry or biology or both: ", chemistry.union(biology))

#print("Union example 2:\n", "students taking either art or stats or both: ", art.union(stats))

#print("intersection example 1:\n", "students taking chemistry and biology only:\n", chemistry.intersection(biology))

#print("intersection example 2:\n", "students taking art and stats only:\n", art.intersection(stats))

#print("Difference example 1:\n", "students taking chemistry but not biology: ", chemistry.difference(biology))

#print("Difference example 3:\n", "students taking art but not stats: ", art.difference(stats))

#print("Difference example 2:\n", "students taking biology but not chemistry: ", biology.difference(chemistry))

#print("Difference example 4:\n", "students taking stats but not art: ", stats.difference(art))

#print("Symmetric Difference example 1:\n", "students taking biology or chemistry, but not both:\n", biology.symmetric_difference(chemistry))

#print("Symmetric Difference example 2:\n", "students taking art or stats, but not both:\n", art.symmetric_difference(stats))

print("Subset example 1:\n", "are all of the biology students in the algebra class:\n", biology.issubset(algebra))

print("Subset example 2:\n", "are all of the algebra students in the biology class:\n", algebra.issubset(biology))
