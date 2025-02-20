# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"13302","system":"gprdproduct"},{"code":"13240","system":"gprdproduct"},{"code":"16038","system":"gprdproduct"},{"code":"13127","system":"gprdproduct"},{"code":"13075","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ca-channel-blocker-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ca-channel-blocker-cephalon---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ca-channel-blocker-cephalon---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ca-channel-blocker-cephalon---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
