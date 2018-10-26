import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, personB)

def reducer(personA, friend_list):
	for friend in friend_list:
		if friend not in mr.intermediate.keys() or personA not in mr.intermediate[friend]:
			mr.emit((personA,friend))
			mr.emit((friend,personA))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)