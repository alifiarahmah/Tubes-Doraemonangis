import os

def load(dir_path):
	try:
		os.chdir(dir_path) # Nge-set Working Directory
		
		os.rename("gadget.csv", "gadget_temp.csv")
		os.rename("consumable.csv", "consumable_temp.csv")
		os.rename("consumable_history.csv", "consumable_history_temp")
		os.rename("gadget_return_history.csv", "gadget_return_history_temp.csv")
		os.rename("gadget_borrow_history.csv", "gadget_borrow_history_temp.csv")
		
		g = open("gadget_temp.csv", "r")
		f = open("gadget.csv", "w+")
		f.write(g.read())
		g.close()
		f.close()
		g = open("consumable_temp.csv", "r")
		f = open("consumable.csv", "w+")
		f.write(g.read())
		g.close()
		f.close()
		g = open("consumable_history_temp.csv", "r")
		f = open("consumable_history.csv", "w+")
		f.write(g.read())
		g.close()
		f.close()
		g = open("gadget_return_history_temp.csv", "r")
		f = open("gadget_return_history.csv", "w+")
		f.write(g.read())
		g.close()
		f.close()
		g = open("gadget_borrow_history_temp.csv", "r")
		f = open("gadget_borrow_history.csv", "w+")
		f.write(g.read())
		g.close()
		f.close()
		
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	except OSError: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False
