from garmin_health_processing.pipeline import *
import json

# import data from json
file = 'data/5-4-22.json'
with open(file) as f:
  data = json.load(f)

# get json string as output
features = run_pipeline(data, showPlots=True)
print(features)
