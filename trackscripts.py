# -*- coding: utf-8 -*-
# this script can only be used under ASCII enviroment
import os
import json

workpath = os.getcwd()
fp_json = open("scripts.json", "a+")
fp_readme = open("ReADME.md", "a+")


try:
    fp_json.seek(0, 0)
    exist_script = json.loads(fp_json.read())
    print("now exists: ", exist_script)
    flag = 1
except:
    print("File script.json is empty")
    exist_script = []
    flag = 0



def find_new_script(directory_name):
    script_name = []
    for filename in os.listdir(directory_name):
        if not filename in exist_script:
            if filename.endswith(".py"): script_name.append(filename)
    return script_name

def write_json(new_script):
    final_list = exist_script + new_script
    fp_json.close()
    fp_json_new = open("scripts.json", "w+")
    fp_json_new.write(json.dumps(final_list))

def write_readme():
    new_script = find_new_script(workpath)
    write_json(new_script)
    print("Added: ", new_script)
    for scripts in new_script:
        tempstr = "- " + scripts + "\n\n"
        fp_readme.write(tempstr)

write_readme()