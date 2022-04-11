from astropy.io import ascii
import pickle


# reads the file using the file names
def read_data(file_names, header):
    n = len(file_names)
    map_to_files = {}
    header_names = []
    for f in file_names:

        # change the path of file accordingly
        if header:
            try:
                # Give the correct path of the files
                map_to_files[f] = ascii.read("/home/shreyaprabhu/GHRSS/data/" + f + ".list", header_start=0,
                                             data_start=0)
            except Exception as e:
                print(e)
                n = 0
            header_names.append(map_to_files[f][0][0])
        else:
            try:
                # Give the correct path of the files
                map_to_files[f] = ascii.read("/home/shreyaprabhu/GHRSS/data/" + f + ".csv", header_start=0,
                                             data_start=1, delimiter=',')
            except Exception as e:
                print(e)
                n = 0
            header_names.append("Pulsar_name")
            header_names.append("Period")
    if n != 0:
        return map_to_files, n, header_names


# code to append any two files. a and b are the file names without the extension
def append_file(a, b):
    # change the path of file accordingly
    f1 = open("/home/shreyaprabhu/GHRSS/data/" + a, 'a')
    try:
        # change the path of file accordingly
        f2 = open("/home/shreyaprabhu/GHRSS/data/" + b, 'r')
        f1.write('\n')
        f1.write(f2.read())
        f1.close()
        f2.close()
    except Exception as e:
        print(e)


# Saves the image object by using pickel
def save_ax(img_obj):
    with open('myplot.pkl', 'wb') as fid:
        pickle.dump(img_obj, fid)