#read the metadata file and update metadata
#LA, 08/2017

import json

def extract_metadata(input_filename, output_filename, wanted_key):

    with open(input_filename, "r") as infile:
        data = json.load(infile)

    changed = False

    if "extended" in data['metadata']:
        if "callInformation" not in data['metadata']['extended']:
            data['metadata']['extended'].update(callInformation={})
        if "modelTargets" not in data['metadata']['extended']:
            data['metadata']['extended'].update(modelTargets={})
    	with open(output_filename, "w") as outfile:
            json.dump(data['metadata'], outfile)        
               
    else: 
        data['metadata'].update(extended={"loadedBy": "voicebase"},modelTargets={},callInformation={})
        changed = True

    if changed == True:
        with open(output_filename, "w") as outfile:
            json.dump(data['metadata'], outfile)

if __name__ == "__main__":
	extract_metadata("metadata_test_Aug10.json", "result_test_Aug10.json", "metadata")