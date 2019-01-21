from sys import argv
from os.path import exists
script, from_file, to_file = argv
open(to_file, 'w').write(open(from_file).read())#don't need out_file, out_file.close
print "All done." 
