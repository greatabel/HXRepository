import os
import pickle
import datetime
import csv
from single_record import SingleRecord

Col_len = 1093


def csv_printer_from_localfile(filename, directory='./'):
    with open(os.path.join(directory, filename), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
        
        # i = 0
        all_rows = []
        for row in reader:
            if row is not None:
                # if i == 0:
                #     print(row, '\n', '#'*20, len(row), type(row))
                # i += 1
                items = []
                split_row = row[0].replace("[", "").replace("]", "").split("),")
                

                # if i == 0:

                for singlerow in split_row:
                    r = singlerow.replace("(", "").split(", ")
                   
                    singlerow = SingleRecord(r[0], r[1], r[2], r[3])
                    # singlerow.displaySingleRecord()
                    items.append(singlerow)

                # i += 1       
                all_rows.append(items)
                # print(len(items))
        return all_rows

def generate_dict(processed_rows):
    dic = {}
    i = 0
    for record in processed_rows:

        # myid = generate_unique_utc()
        # myid += 10
        # print('#', myid)
        dic[i] = record
        i += 1
        print(i)
    return dic



# def generate_unique_utc():
#     d = datetime.datetime.utcnow()
#     epoch = datetime.datetime(1970,1,1)
#     t = (d - epoch).total_seconds()
#     return int(t*1000)

def save_to_localfile(filename, content, directory='./'):
    # http://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python
    with open(os.path.join(directory, filename), 'w') as f:
        f.write(content)

def main():
    # print(generate_unique_utc(), '$'*20)
    filename = 'newfile.txt'

    processed_rows = csv_printer_from_localfile(filename)
    print('len=', len(processed_rows))
    dic = generate_dict(processed_rows)
    content = ''
    for k, v in dic.items():
        print(k)
        line = str(k) 
        for singlerecord in v:
            line += ', ' + singlerecord.name +', ' + singlerecord.value + ', ' + singlerecord.status \
                + ', ' + singlerecord.record_date
        line += '\n'
        content += line
    save_to_localfile('processed.csv', content)

if __name__ == "__main__":
    main()