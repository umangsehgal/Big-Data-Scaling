import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id= record[1]
    mr.emit_intermediate(order_id, record)

def reducer(order_id, line):
    length = len(line)
    for i in range(1,length):
      v = []
      v += line[0]
      v += line[i]
      mr.emit(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)