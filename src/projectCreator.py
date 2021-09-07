# import pyautogui as auto
# from time import sleep as pause


from lxml import etree

# pause(5)
# auto.write('test')
# auto.press('space')

data = {'cached_stamp_file':
			{
				'E:\\Desktop\\Programmation\\gitDuBled\\explication.png': 
					{'stamp': 1630351478.1058757, 'type': 'png', 'backUp': '1'},
				'E:\\Desktop\\Programmation\\gitDuBled\\readme.md': 
				 	{'stamp': 1630361047.4295337, 'type': 'md', 'backUp': '1'}, 
				'E:\\Desktop\\Programmation\\gitDuBled\\run.bat':
					{'stamp': 1630352062.475876, 'type': 'bat', 'backUp': '1'}, 
				'E:\\Desktop\\Programmation\\gitDuBled\\src\\Function.py':
					{'stamp': 1630568836.9690905, 'type': 'py', 'backUp': '1'}, 
				'E:\\Desktop\\Programmation\\gitDuBled\\src\\main.py': 
					{'stamp': 1630352191.3874576, 'type': 'py', 'backUp': '1'}, 
				'E:\\Desktop\\Programmation\\gitDuBled\\src\\projectCreator.py': 
					{'stamp': 1630569098.0560904, 'type': 'py', 'backUp': '1'}, 
				'E:\\Desktop\\Programmation\\gitDuBled\\src\\watcher.py':
					{'stamp': 1630569223.1370907, 'type': 'py', 'backUp': '1'}
			},
		'cached_stamp_floder':
			{
				'E:\\Desktop\\Programmation\\gitDuBled':
					{'stamp': 4096},
				'E:\\Desktop\\Programmation\\gitDuBled\\src':
					{'stamp': 4096}
			},
		'dirs':
			[
				'E:\\Desktop\\Programmation\\gitDuBled',
				'E:\\Desktop\\Programmation\\gitDuBled\\src'
			], 
		'data': 
			[
				'E:\\Desktop\\Programmation\\gitDuBled\\explication.png',
				 'E:\\Desktop\\Programmation\\gitDuBled\\readme.md',
				  'E:\\Desktop\\Programmation\\gitDuBled\\run.bat', 
				  'E:\\Desktop\\Programmation\\gitDuBled\\src\\Function.py', 
				  'E:\\Desktop\\Programmation\\gitDuBled\\src\\main.py', 
				  'E:\\Desktop\\Programmation\\gitDuBled\\src\\projectCreator.py',
				   'E:\\Desktop\\Programmation\\gitDuBled\\src\\watcher.py'
			]
	}
dictFile = ["cached_stamp_file","cached_stamp_floder"]
with open("backup.xml","wb") as file:
			dataKey = etree.Element("backup")
			for key in data:
				cache = etree.SubElement(dataKey, "data")
				cache.set("name",key)
				if key in dictFile:
					for subKey in data[key]:
						stamp = etree.SubElement(cache, "file")
						stamp.text=subKey
						for dataKeyS in data[key][subKey]:
							dataStamp = etree.SubElement(stamp, "data")
							dataStamp.set("name",dataKeyS)
							dataStamp.text =  str(data[key][subKey][dataKeyS])
				else:
					for subKey in data[key]:
						stamp = etree.SubElement(cache, "path")	
						stamp.text=subKey
				
			# print(etree.tostring(dataKey, pretty_print=True).decode())
			file.write(etree.tostring(dataKey, pretty_print=True))


tree = etree.parse("backup.xml")
data2 = {}
for backup in tree.xpath("/backup"):
    for child in backup.getchildren():
    	key = (child.get('name'))
    	if key in dictFile:
    		data2[key] = {}
    		for data in child.getchildren():
    			data2[key][data.text] = {}
    			for stamps in data.getchildren():
    				keyData = stamps.get('name')
    				KeyDataData = stamps.text
    				if keyData == "stamp":
    					KeyDataData = float(KeyDataData)
    				data2[key][data.text][keyData] = KeyDataData
    	else:
    		data2[key] = []
    		for data in child.getchildren():
    			data2[key].append(data.text)

print(data2)


# user = etree.SubElement(users, "user")
# user.set("data-id", "101")
# nom = etree.SubElement(user, "nom")
# nom.text = "Zorro"
# metier = etree.SubElement(user, "metier")
# metier.text = "Danseur"

