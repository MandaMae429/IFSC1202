def DDMMSStoDecimals(deg,min,sec):
  return deg+(min/60)+(sec/3600)
def ParseDegreeString(degstr):
  seg=""
  deg=0
  min=0
  sec=0
  for char in degstr:
    if char==chr(176):
      deg=float(seg)
      seg=""
      continue
    if char=="'":
      min=float(seg)
      seg=""
      continue
    if char=="\"":
      sec=float(seg)
      break
    seg=seg+char
  print(DDMMSStoDecimals(deg, min, sec))
  return (DDMMSStoDecimals(deg, min, sec))
  

inputfile=open("07.Project Angles Input.txt", "r")
outputfile=open("07.Project Angles Output.txt", "w")
while True:
    line=inputfile.readline()
    if not line:
        break
    decdeg=ParseDegreeString(line)
    print (decdeg)
    outline=str(decdeg)+"\n"
    outputfile.write(outline)
outputfile.close
inputfile.close
print("records processed")