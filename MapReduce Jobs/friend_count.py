import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    mr.emit_intermediate(person, 1)

def reducer(person, friend_count):
    total = 0
    for i in friend_count:
      total += i
    mr.emit((person, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)