from os import listdir
from os.path import isfile, join

def index_maps():
	maps_folder = "static/maps/"
	return [f for f in listdir(maps_folder) if isfile(join(maps_folder, f))]