# Return string `s` duplicated `i` times.
def duplicate(s, i):
    ret = ""
    for j in range(i):
        ret += s
    return ret

in_name = input("What file are we converting? (full name) ")
outfile = open(in_name + ".org", 'w')
wfDone = "[COMPLETE]"
orgDone = "DONE"

for num, line in enumerate(open(in_name)):
    if line.isspace():
        outfile.write(line + "\n")
        continue

    if line.strip()[0] == "-":
      dash = line.find("-")
      line = line[dash + 1:].strip() # get line contents only
      if line.startswith(wfDone):
          line = line.replace(wfDone, orgDone, 1) # replace a single occurrence
      line = duplicate("*", dash // 2 + 1) + " " + line # build the new line
    
    outfile.write(line + "\n")

outfile.close()
