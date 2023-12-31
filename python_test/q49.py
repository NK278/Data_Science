import csv

def read_csv(f1,f2,condition_clm_idx,c_val):
    with open(f1,'r') as f, open(f2,'w',newline='') as o:
        reader=csv.reader(f)
        writer=csv.writer(o)

        for row in reader:
            if row[condition_clm_idx]==c_val: writer.writerow(row)

