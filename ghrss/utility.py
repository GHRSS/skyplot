from astropy.io import ascii
import pickle
from ghrss import config


def read_data(file_names, header):
    """
    ###Description:
    reads the file using the file names
    File path can be changed accordingly
    ###Args:
    file_names: list of file names

    header: logical TRUE or FALSE, indicating whether the datafile has a file-specific header
    ###Returns
    map_to_files: the table containing the data from file

    header_names: list containing the headers of all the files
    """
    n = len(file_names)
    map_to_files = {}
    header_names = []
    file_path = config.FILE_PATH
    for f in file_names:
        # change the path of file accordingly
        if header:
            try:
                # Give the correct path of the files
                map_to_files[f] = ascii.read(
                    file_path + f + ".list", header_start=0, data_start=0
                )
            except Exception as e:
                print(e)
                n = 0
            header_names.append(map_to_files[f][0][0])
        else:
            try:
                # Give the correct path of the files
                map_to_files[f] = ascii.read(
                    file_path + f + ".csv", header_start=0, data_start=1, delimiter=","
                )
            except Exception as e:
                print(e)
                n = 0
            header_names.append("Pulsar_name")
            header_names.append("Period")
    if n != 0:
        return map_to_files, n, header_names


def append_file(a, b):
    """
    ###Descrption:
    appends any two files. a and b are the file names without the extension
    File path can be changed accordingly.
    ###Args:
    a: The name of the file to which the data is to be appended
    b: the name of the file which is to be appended

    """
    file_path = config.FILE_PATH
    f1 = open(file_path + a, "a")
    try:
        # change the path of file accordingly
        f2 = open(file_path + b, "r")
        f1.write("\n")
        f1.write(f2.read())
        f1.close()
        f2.close()
    except Exception as e:
        print(e)


def save_ax(img_obj):
    """Saves the image object 'plot.pkl' as  by using pickle"""
    with open("../plot.pkl", "wb") as fid:
        pickle.dump(img_obj, fid)
