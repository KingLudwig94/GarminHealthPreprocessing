from garmin_health_processing.pipeline import *
from garmin_health_processing.hrv import *
from garmin_health_processing.spo2 import *
from garmin_health_processing.utils import *
from pandas import DataFrame
import json

# import data from json
file = 'data/5-4-22.json'
with open(file) as f:
    data = json.load(f)[0]

# get json string as output
hr = data['heart_rate']['data']
if (hr != None):
    hr2 = {}
    for row in hr:
        hr2[row['offset']] = row['value']
    hr = hr2
timespan = np.fromiter(hr.keys(), dtype=float)
retimed = retime(hr, 15, timespan[-1], cumulative=False, startTime=timespan[0])
filled_hrv = HRV(hr).inputation(retimed)
hrv_clean = moving_average(filled_hrv, 5)

showpreprocess(retimed, filled_hrv, hrv_clean, 'HR preprocess')

spo2 = data['sleep']['spo2']
if (spo2 != None):
    spo22 = {}
    for row in spo2:
        spo22[row['offset']] = row['value']
    spo2 = spo22
timespan = np.fromiter(spo2.keys(), dtype=float)
spo2retimed = retime(spo2, 60, timespan[-1], cumulative=False, startTime=timespan[0], )
filled_spo2 = SPO2(spo2, data['sleep']['duration']).inputation(spo2retimed)
spo2_clean = moving_average(filled_spo2, 5)
start = data['sleep']['start_offset']# - timespan[0]
showpreprocess(spo2retimed, filled_spo2, spo2_clean, 'spO2 preprocess', start=start)


rsp = data['sleep']['respiration']
if (rsp != None):
    rsp2 = {}
    for row in rsp:
        rsp2[row['offset']] = row['value']
    rsp = rsp2
timespan = np.fromiter(rsp.keys(), dtype=float)
rspretimed = retime(rsp, 60, timespan[-1], cumulative=False, startTime=timespan[0], )
filled_rsp = SPO2(rsp, data['sleep']['duration']).inputation(rspretimed)
rsp_clean = moving_average(filled_rsp, 5)
start = data['sleep']['start_offset']# - timespan[0]
showpreprocess(rspretimed, filled_rsp, rsp_clean, 'Respiration preprocess', start=start)