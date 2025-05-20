from jcamp import jcamp_readfile

# path to your .jdx file
file_path = "./12125-02-9-IR.jdx"

# load the data
data = jcamp_readfile(file_path)

# extract x and y
x = data['x']
y = data['y']

print("x:", x)
print("y:", y)
