import pipeline
import json

""" 
Simple script to visualize the result of the pipeline on a specific input file
"""
with open('garmin_health_processing/bin/data/5-4-22.json', 'r') as f:
    data = json.load(f)

pipeline.run_pipeline(data, True, False)
