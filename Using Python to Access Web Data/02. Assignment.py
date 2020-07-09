import re 
  
def getNumbers(str,sum): 
    array = re.findall(r'[0-9]+', str) 
    for i in array:
        sum+=int(i)
    return sum 
  
sum = 0
file = "regex_sum_702801.txt"
fh = open(file)
for line in fh:
    result = getNumbers(line,sum) 
    sum = result

print(sum)