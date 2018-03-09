import ee
import subprocess
import string
import os

def mover(assetpath,destinationpath):
	for line in subprocess.check_output("earthengine ls "+assetpath,shell=True).split('\n'):
                try:
                    src= line
                    dest=line.replace(assetpath,destinationpath)
                    com=(str('earthengine mv ')+str(src)+' '+str(dest))
                    process = subprocess.call(com,shell=True)
                except Exception:
                        print(com)
                        with open(errorlogmove.csv,'a') as csvfile:
                                writer=csv.writer(csvfile,delimiter=',')
                                writer.writerow([com])
                                csvfile.close()
                print("Assets Move Completed")
