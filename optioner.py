import enum

class OptType(enum.Enum):
    param = 'ir.ui.ionic.menu.param'
    label = 'ir.ui.ionic.menu.label'

SEPARATOR=";"
def parse_option(filename: str, separator=SEPARATOR) -> list:
    """Parses csv-ish file to extract its fields. Returns the fields (list) for every line (list)"""
    options = []
    with open(filename, 'r') as file:
        options = list(map(lambda line: [field.rstrip() for field in line.split(SEPARATOR)], file.readlines()))
    return options

class Interpreter:

    TEMPLATE_FIELDS = """
        <field name="name">{}</field>
        <field name="ionic_menu_id" eval="ref('{}')"/>
        <field name="value">{}</field>"""
    TEMPLATE_RECORD = """
    <record id="{}" model="{}">{}
    </record>
"""

    def __init__(self, menu: str, prefix: str):
        self.menu = menu
        self.prefix = prefix

    def build_xml(self, opt_type: OptType, options: list):
        records = []
        if(opt_type == OptType.param):
            params = self.interprete_params(options)
            for param in params:
                fields = self.TEMPLATE_FIELDS.format(param['name'], self.menu, param['value'])
                fields += '\n        <field name="note">{}</field>'.format(param['note'])
                xml_id = '{}_{}'.format(self.prefix, param['name'])
                record = self.TEMPLATE_RECORD.format(xml_id, opt_type.value, fields)
                records.append(record)
        elif(opt_type == OptType.label):
            labels = self.interprete_labels(options)
            for label in labels:
                fields = self.TEMPLATE_FIELDS.format(label['name'], self.menu, label['value'])
                xml_id = '{}_{}'.format(self.prefix, label['name'])
                record = self.TEMPLATE_RECORD.format(xml_id, opt_type.value, fields)
                records.append(record)
        else:
            raise ValueError('incoherent option type given')
        return records

    def interprete_params(self, fields: list) -> list:
        """Formats list of list into list of params obj"""
        params = [{'name': field[0], 'value': field[1], 'note': field[2] if len(field) > 2 else ''} for field in fields]
        return params

    def interprete_labels(self, fields: list) -> list:
        """Formats list of list into list of label obj"""
        labels = [{'name': field[0], 'value': field[1]} for field in fields]
        return labels
