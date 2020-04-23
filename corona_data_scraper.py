
import os, re, requests, datetime
print("-"*101)
print(("Report generated on " +str(datetime.datetime.now())).center(101))
raw_data = requests.get("https://www.mohfw.gov.in").text
totalregex = re.compile(r'''<strong>(\d*?)</strong>.*?<span.*?>(.*?)</span>''',re.DOTALL)
data = totalregex.findall(raw_data)
sum = 0
for i, l in enumerate(data):
    if i == 4:
        print(("Total Cases :"+ str(sum)).center(101))
        break
    sum = sum + int(l[0])
    print(f'{l[1]} : {l[0]}'.center(101))
print("-"*101)
stateregex = re.compile(r'''<td>(\d+)</td>\n\t<td>(.*?)</td>\n\t<td>(\d+)</td>\n\t<td>(\d+)</td>\n\t<td>(\d+)</td>''',re.DOTALL)
state_data = stateregex.findall(raw_data)
print("|","S.No","|","Name of State / UT".center(30),"|","Total Confirmed cases","|","Cured/Discharged/Migrated","|","Death","|")
print("-"*101)
for state in state_data:
    print("|",state[0].center(4),"|",state[1].center(30),"|",state[2].center(21),"|",state[3].center(25),"|",state[4].center(5),"|")
    print("-"*101)