import os, re, requests, datetime
print("-----------------------------------------------------------------------------")
print("\t\tReport generated on" ,datetime.datetime.now())
raw_data = requests.get("https://www.mohfw.gov.in").text
totalregex = re.compile(r'''<strong>(\d*?)</strong>.*?<span.*?>(.*?)</span>''',re.DOTALL)
data = totalregex.findall(raw_data)
sum = 0
for i, l in enumerate(data):
    if i == 4:
        print("Total Cases :", str(sum))
        break
    sum = sum + int(l[0])
    print(f'{l[1]} : {l[0]}')
print("-----------------------------------------------------------------------------")
stateregex = re.compile(r'''<td>(\d+)</td>\n\t<td>(.*?)</td>\n\t<td>(\d+)</td>\n\t<td>(\d+)</td>\n\t<td>(\d+)</td>''',re.DOTALL)
state_data = stateregex.findall(raw_data)
for state in state_data:
    print(f"{state[0]}  {state[1]} :")
    print(f"\tTotal Confirmed cases : {state[2]}")
    print(f"\tCured/Discharged/Migrated : {state[3]}")
    print(f"\tDeath : {state[4]}")
    print('*****************************************************************************')
