import csv

def cnt_rows(file_path):
   with open(file_path,'r') as file:
     csv_r=csv.reader(file)
    #  rw_cnt=len(list(csv_r))
     rw_cnt=sum(1 for r in csv_r)
     return rw_cnt
print(cnt_rows('stud.csv'))     