from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from collections import defaultdict

""" def crashes_by_vehicle(make, model, model_year, body_type, from_caseyear, to_caseyear, state):
    url = f"https://crashviewer.nhtsa.dot.gov/CrashAPI/crashes/GetCrashesByVehicle?make={make}&model={model}&modelyear={model_year}&bodyType={body_type}&fromCaseYear={from_caseyear}&toCaseYear={to_caseyear}&state={state}&format=json"
    page = requests.get(url)
    #print(page.status_code)
    #soup = BeautifulSoup(page.text,'html.parser')
    #print(soup.prettify())
    data = page.text
    parse_json = json.loads(data)
    print(parse_json)
    attributeDict = defaultdict(list)
    for attribute in parse_json["Results"][0]:
        
        attributeDict["Make"].append(attribute["MAKE"])
        attributeDict["Make model"].append(attribute["MAK_MOD"])
        attributeDict["Vehicle involved"].append(attribute["MAK_MODNAME"])
        attributeDict["Model_Year"].append(attribute["MOD_YEAR"])
        dataframe = pd.DataFrame(attributeDict)
        dataframe.to_csv('C:/Users/RuchaN1507/OneDrive - Cal State Fullerton/Attachments/Spring_2023/ISDS_558/558_project/Test1.csv')
        print(dataframe)
        print(dataframe.isna().sum())
crashes_by_vehicle(6,41,2003,4,2010,2015,21)
 """


def crash_by_occupant(age, sex, seat_pos, injury_sev, from_caseyear, to_caseyear, state, include_occupants, include_nonoccupants):
    severity_level = []
    drinking = []
    dataframe = pd.DataFrame({
        "Severity Level": severity_level,
        "Drinking Involvement": drinking
    })
    url = f"https://crashviewer.nhtsa.dot.gov/CrashAPI/crashes/GetCrashesByPerson?age={age}&sex={sex}&seatPos={seat_pos}&injurySeverity={injury_sev}&fromCaseYear={from_caseyear}&toCaseYear={to_caseyear}&state={state}&includeOccupants={include_occupants}&includeNonOccupants={include_nonoccupants}&format=json"
    page = requests.get(url)
    # print(page.status_code)
    soup = BeautifulSoup(page.text,'html.parser')
    # print(soup.prettify())
    data = page.text
    parse_json = json.loads(data)
    # print(parse_json)
    attributeDict = defaultdict(list)
    # for attribute in parse_json["Results"][0]:
        # attributeDict['None'].append(None)
        # attributeDict["Age"].append(attribute["AGE"])
        # attributeDict["Sex"].append(attribute["SEX"])
        # attributeDict["Sex_Name"].append(attribute["SEXNAME"])
        # attributeDict["Seat"].append(attribute["SEAT_POS"])
        # attributeDict["Seat_pos"].append(attribute["SEAT_POSNAME"])
        # attributeDict["Fatality"].append(attribute["DEATH_HRNAME"])
        # attributeDict["State Case"].append(attribute["ST_CASE"])
        # attributeDict["Drinking_Involvement"].append(attribute["DRINKING"])
        # attributeDict["Drugs_involvement"].append(attribute["DRUGS"])
        # attributeDict["Injury_Severity"].append(attribute["INJ_SEV"] +" || "+ attribute["INJ_SEVNAME"])
        # attributeDict["Race_Involvement"].append(attribute["RACE"])
        # attributeDict["Rollover"].append(attribute["ROLLOVER"] +" || "+ attribute["ROLLOVERNAME"])
        # attributeDict["SchoolBus_involvement"].append(attribute["SCH_BUS"])
        # attributeDict["Vehicle_withTrailers"].append(attribute["TOW_VEH"])
    try:
        drinking.append(parse_json["Results"][0][0]['DRINKING'])
    except:
        drinking.append('Null')
    try:
        severity_level.append(parse_json["Results"][0][0]['INJ_SEV'])
    except:
        severity_level.append('Null')
        # dataframe.to_csv('C:/Users/RuchaN1507/OneDrive - Cal State Fullerton/Attachments/Spring_2023/ISDS_558/558_project/Test2.csv')
    return dataframe
age = 20
final_dataframe = pd.DataFrame()
for i in range(age,70,1):
    final_dataframe.append(crash_by_occupant(i,4,11,2,2012,2013,1,True,True))
final_dataframe.to_csv('Test_Crash_Occupant.csv')
# crash_by_occupant(25,2,11,2,2012,2013,1,True,True)