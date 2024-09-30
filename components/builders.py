def build_onchange(record_values: dict, code: str, settings: dict) -> str:
    content_type = f"{'raw_' if settings['RAW'] else ''}code"
    data['id'] = data['id'] if 'id' in data else data['name']
    content = list(filter(None, [
        f"""    <record id="{values['id']}" model="manual.onchange">""",
        f"""        <field name="name">{values['name']}</field>""",
        f"""        <field name="model_id" search="[('model', '=', '{values['model']}')]"/>""",
        f"""        <field name="is_translatable_code" eval="{not RAW}"/>""" if RAW == 2 else None,
        f"""        <field name="{content_type}code">""",
        f"""{code}""",
        f"""        </field>""",
        f"""    </record>\n\n""",
    ]))
    if(not SECURE):
        content.insert(2, """        <field name="is_security_check" eval="False"/>""")
    return '\n'.join(content)
    return 
