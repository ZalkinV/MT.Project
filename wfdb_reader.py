import os
from pathlib import Path
import matplotlib.pyplot as plt
import wfdb


CONSOLE_WIDTH = os.get_terminal_size()[0]
OUTPUT_DELIMETER = "".ljust(CONSOLE_WIDTH, "-")


DATA_PATH = Path("wfdb_data")
DAT_FILE_PATH = DATA_PATH / "dats" / "3001924p"
PHYS_FILE_PATH = DATA_PATH / "physionet" / "a103l"


if __name__ == "__main__":
    phys_record = wfdb.rdrecord(PHYS_FILE_PATH)
    print(phys_record.p_signal)
    print(OUTPUT_DELIMETER)
    print(phys_record.__dict__)
    print(OUTPUT_DELIMETER)

    signals, fields = wfdb.rdsamp(PHYS_FILE_PATH)
    print(signals)
    print(OUTPUT_DELIMETER)
    print(fields)

    wfdb.plot_wfdb(record=phys_record, title='Local record a103l from Physionet Challenge 2015') 

    remote_record = wfdb.rdrecord('a103l', pb_dir='challenge/2015/training/')
    wfdb.plot_wfdb(record=remote_record, title='Remote record a103l from Physionet Challenge 2015')