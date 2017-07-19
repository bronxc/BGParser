import sys
import re

from optparse import OptionParser

def handle_file(fname):
    with open(fname) as f:
        data = f.readlines()
        
    return data

def get_fields(d, fields):
    data = []
    
    for f in fields:
        if f in d:
            data.append(d[f].strip())
        else:
            data.append("")

    return data
    
def main(args):
    data = handle_file(args.file)
    result = []
    
    if args.new_record:
        new_record = re.compile(args.new_record)
    
    fields = args.fields.strip().split(',')
    
    dataDict = {}
    
    # Iterate over all of our data and begin best guess parsing
    for line in data:
        line = line.strip()
        
        # If we detect a new record, lets create it
        if args.new_record and new_record.match(line) and len(dataDict) > 1:
            result.append(dataDict)
            dataDict = {}
        
        try:
            # Split line based on our provided separator
            key,value = line.split(args.sep)
                
            if key in dataDict and not args.new_record:
                result.append(dataDict)
                dataDict = {}
                
            dataDict[key] = value
        except:
            continue
    
    if len(dataDict) > 0:
        result.append(dataDict)
    
    # Print the CSV header
    print('"{0}"'.format('","'.join(fields)))
    
    # Print all the dictionaries with matching fields
    for d in result:
        try:
            print('"{0}"'.format('","'.join(get_fields(d, fields))))
        except:
            continue

class NonCorrectingOptionParser(OptionParser):

    def _match_long_opt(self, opt):
        # Is there an exact match?
        if opt in self._long_opt:
            return opt
        else:
            self.error('"{0}" is not a valid command line option.'.format(opt))
        
def get_parser():
    parser = NonCorrectingOptionParser(add_help_option=False)
    
    parser.add_option('-h', '--help', help='Show help message',
        action='store_true')
    parser.add_option('-f', '--file', help='File name to parser',
        action='store')
    parser.add_option('-s', '--sep', help='Separator used to identify key/value pairs.',
        action='store')
    parser.add_option('--fields', help='Fields to be displayed after parser (comma separated)',
        action='store')
    parser.add_option('--new-record', help='Regular Expression to identify the start of a new record',
        action='store')
        
    return parser

def print_help(parser):
    print(parser.format_help().strip())
     
def validate_args(args):
    if args.file and args.sep and args.fields:
        return True
    
    return False
     
def ArgEntry():
    parser = get_parser()
    args = parser.parse_args()[0]

    if args.help:
        print_help(parser)
    elif not validate_args(args):
        usage(sys.argv[0])
        exit()
    else:
        main(args)
        
       
def usage(scriptname):

    print('Usage:')
    print(' > {0} [filename]\n'.format(scriptname))
    print(' BG Parser is a "Best Guess" parser which will attempt to parser the')
    print(' provided data into key-value-pairs. BG Parser looks for multi-line')
    print(' formatted data in Key/Value pair notation.')
        
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        usage(sys.argv[0])
        exit()
    
    ArgEntry()