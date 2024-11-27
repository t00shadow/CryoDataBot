import os
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from configparser import ConfigParser


def parse_cmd()->ArgumentParser:
    # find all default vals
    config = ConfigParser()
    config_path = os.path.join('src','backend_core','backend_helpers','CryoDataBotConfig.ini')
    config.read(config_path)
    sections = config.sections()
    sections.remove('user_settings')
    default_keys = [key for section in sections for key in config.options(section)]

    from . import __description__ as prog_desc
    parser = ArgumentParser(
        prog='CryoDataBot',
        description=prog_desc,
        formatter_class=RawDescriptionHelpFormatter,
        #add_help=False,
    )

    subparser_des = """
f, function - select a function to run
c, change - change a default variable value
s, show - show the current value of a default variable
"""

    subparsers = parser.add_subparsers(title='Functionalities',
                                       description=subparser_des,
                                       help='-h, --help - show more help',
                                       required=True,
                                       dest='mode',
                                       metavar='mode'
                                       )
    
    # add subparser for functions
    func_parser = subparsers.add_parser('functions', 
                                        aliases=['f'],)
    func_parser.add_argument('-f', '--file', 
                             required=True,
                             help='path to the .json file',
                             metavar='file_path'
                             )
    func_parser.add_argument('-r', '--run', 
                        choices=['pipeline',
                                 'fetch',
                                 'filter',
                                 'preprocess',
                                 'label',
                                 'test'],
                        required=True,
                        help='select one of the functions to run'
                        )
    
    # add subparser for changing defaults
    add_parser = subparsers.add_parser('change', 
                                        aliases=['c'])
    add_parser.add_argument('-n', '--name',
                            choices=default_keys, 
                            type=str,
                            required=True,
                            help='name of the variable',
                            metavar='var_name',
                            )
    add_parser.add_argument('-v', '--val',
                            type=str, 
                            required=True,
                            help='new value of the variable',
                            metavar='new_val',
                            )
    
    
    # add subparser for showing current variable vals
    add_parser = subparsers.add_parser('show', 
                                        aliases=['s'])
    add_parser.add_argument('-n', '--name',
                            choices=default_keys, 
                            type=str,
                            required=True,
                            help='name of the variable',
                            metavar='var_name',
                            )
    
    return parser
