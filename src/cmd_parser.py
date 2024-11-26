import os
from argparse import ArgumentParser
from configparser import ConfigParser


def parse_cmd()->ArgumentParser:
    # find all default vals
    config = ConfigParser()
    config_path = os.path.join('src','backend_core','backend_helpers','CryoDataBotConfig.ini')
    config.read(config_path)
    sections = config.sections()
    sections.remove('user_settings')
    default_keys = [key for section in sections for key in config.options(section)]

    parser = ArgumentParser(
        prog='CryoDataBot',
    )

    subparsers = parser.add_subparsers(title='Functionalities',
                                       help='subcommand help',
                                       required=True,
                                       dest='mode'
                                       )
    
    # add subparser for functions
    func_parser = subparsers.add_parser('functions', 
                                        aliases=['f'],)
    func_parser.add_argument('-f', '--file', required=True)
    func_parser.add_argument('-r', '--run', 
                        choices=['pipeline',
                                 'fetch',
                                 'filter',
                                 'preprocess',
                                 'label',
                                 'test'],
                        required=True,
                        )
    
    # add subparser for changing defaults
    add_parser = subparsers.add_parser('change', 
                                        aliases=['c'])
    add_parser.add_argument('-n', '--name',
                            choices=default_keys, 
                            type=str,
                            required=True)
    add_parser.add_argument('-v', '--val',
                            type=str, 
                            required=True)
    
    
    # add subparser for showing current variable vals
    add_parser = subparsers.add_parser('show', 
                                        aliases=['s'])
    add_parser.add_argument('-n', '--name',
                            choices=default_keys, 
                            type=str,
                            required=True)
    
    return parser
