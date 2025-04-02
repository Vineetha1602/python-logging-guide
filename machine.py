import logging

logger = logging.getLogger(__name__) # will be main if we are running the file directly, if as an import then the filename
logger.setLevel(logging.INFO) # setting the level

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s') # setting the format

file_handler = logging.FileHandler('./generated_log_files/machine.log') # setting the log file
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename='machine.log', level=logging.INFO,
#                     format='%(levelname)s:%(message)s')

class Machine:
    """A sample Machine class"""

    def __init__(self, name, model, serial_number):
        self.name = name
        self.model = model
        self.serial_number = serial_number

        logger.info('Created Machine: {} - {} - {}'.format(self.name, self.model, self.serial_number))

    @property
    def details(self):
        return 'Machine: {} | Model: {} | Serial Number: {}'.format(self.name, self.model, self.serial_number)


machine_1 = Machine('Excavator', 'CAT320', 'EX123456')
machine_2 = Machine('Bulldozer', 'KomatsuD65', 'BD789012')
machine_3 = Machine('Crane', 'LiebherrLTM', 'CR345678')
