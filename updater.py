from enum import Enum
import lxml.etree as ET

class Type(Enum):
    OC = 'manual.onchange'
    VIEW = 'ir.ui.view.ionic'
    MENU = 'ir.ui.menu.ionic'
    CSS = 'ir.ui.css.ionic'
    PARAM = 'ir.ui.menu.ionic.param'
    LABEL = 'ir.ui.menu.ionic.label'

def update_record(xml_doc: ET.ElementTree, xml_id: str, content:str, rec_type=Type):
    """Updates the record's content inside the xml doc"""
    # output=$(cat file_content | xmlstarlet -Pu '<xpath to subnode>' -v '<new content>')
    # (doesn't quite work like that) output=$(cat file_content | xmlstarlet -Pi '<xpath to previous subnode>' -t text -n '' -v '<content>')
    return xml_doc.xpath(f".//record[@id='{xml_id}']/field[@name='code' or @name='raw_code']")

doc = ET.parse('/home/quentin/git/consulting/leatherwork/data/data_declaration_time.xml')
qwe = update_record(doc, 'INPUT_TIME_CUT_ORDER_m2o_cutting_order', '')
