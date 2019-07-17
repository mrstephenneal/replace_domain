import os
import shutil
from replace_domain import replace_domain


DOMAIN = 'validation.example.com'
CONF_FILE = os.path.join(os.path.dirname(__file__), 'data', 'default.conf')
CONF_FILE_REPLACED = os.path.join(os.path.dirname(__file__), 'data', 'default_replaced.conf')
PLACEHOLDER = '$VALIDATION_DOMAIN'


def main():
    # Copy test conf file
    shutil.copyfile(CONF_FILE, CONF_FILE_REPLACED)

    # Replace domain
    replace_domain(DOMAIN, CONF_FILE_REPLACED, PLACEHOLDER)

    # Show contents of the domain replaced conf
    with open(CONF_FILE_REPLACED, 'r') as conf:
        print(conf.read())

    # Delete replaced conf file
    os.remove(CONF_FILE_REPLACED)


if __name__ == '__main__':
    main()
