import xml.etree.ElementTree as ETree

class Backup_XML_Handler:

    def __init__(self):
        
        #global variable
        self.Backupconf = {}
        self.cmd_out = ["(x)","(+)"]
        
        #class variable
        self.xml_root = None


    def load_xml(self):
        xml_tree = ETree.parse('backup.xml')

        #xml file
        self.xml_root = xml_tree.getroot()

    def read_elements(self):

        #Parsing Environments 'name' attribute
        for backup in self.xml_root.findall('Backup'):
            #get backupname
            backup_name = backup.get('name')

            #dictionary for <paths>
            for path in backup.findall('path'):
                path_info = {
                    'path': path.text,
                    'include': path.get('include', None),
                    'exclude': path.get('exclude', None)
                }
            #dictionary for <destination>
            for destination in backup.findall('destination'):
                destination_info = {
                    'destination': destination.text,
                    'name': destination.get('name', None),
                    'host': destination.get('host', None)
                }

            #merge dicts
            self.Backupconf[backup_name] = path_info, destination_info

def get_backupconf():
    backup_handler = Backup_XML_Handler()
    try:
        backup_handler.load_xml()
    except:
        raise ETree.ParseError

    try:
        backup_handler.read_elements()
    except:
        raise ValueError
    
    return backup_handler.Backupconf
