from jinja2 import Environment, FileSystemLoader
import base64
import yaml

secrets = {
    'SP_KEY'         : {'file': './secrets/sp/sp-key.pem'},
    'IDP_BACKCHANNEL': {'file': './secrets/idp/idp-backchannel.p12'},
    'IDP_BROWSER'    : {'file': './secrets/idp/idp-browser.p12'},
    'IDP_ENCRYPTION' : {'file': './secrets/idp/idp-encryption.key'},
    'IDP_SIGNING'    : {'file': './secrets/idp/idp-signing.key'},
    'IDP_SEALER'     : {'file': './secrets/idp/sealer.jks'}
}

for key, secret in secrets.items():
    with open(secret['file'], 'rb') as f:
        secrets[key] = base64.b64encode(f.read()).decode('utf-8')

env = Environment(loader = FileSystemLoader('./templates'), 
    trim_blocks=True, lstrip_blocks=True)

template = env.get_template('secrets.yaml.j2')

with open('./secrets.yaml', 'w') as out:
    out.write(template.render(secrets))
