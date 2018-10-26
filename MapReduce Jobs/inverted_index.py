import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def transform_unique(sequence, method=None): 
  result = []
  seen = {}
  if method is None:
    def method(x): return x
  
  for i in sequence:
    marker = method(i)
    if marker in seen: continue
    seen[marker] = 1
    result.append(i)
  return result


def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in transform_unique(words):
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total_list = []
    for v in list_of_values:
      total_list.append(v)
    mr.emit((key, total_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
