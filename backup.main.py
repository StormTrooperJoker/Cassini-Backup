#custom modules
from backup_parse import Backup_Parser
from xml.etree.ElementTree import ParseError

backup_handler = Backup_Parser()

#Load XML
try:
    backup_handler.load_xml()
except:
    raise ParseError
try:
    backup_handler.read_elements()
except:
    raise ValueError

try:
    backup_handler.preparse_elements()
except:
    pass

print(backup_handler.Backupconf)




