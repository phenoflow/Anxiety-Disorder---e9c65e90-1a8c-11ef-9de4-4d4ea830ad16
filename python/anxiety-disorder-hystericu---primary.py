# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Jonathan Green, Carolyn A Chew-Graham, Nav Kapur, Darren M Aschcroft, 2024.

import sys, csv, re

codes = [{"code":"Eu44.11","system":"readv2"},{"code":"E201z11","system":"readv2"},{"code":"E201511","system":"readv2"},{"code":"Eu44.13","system":"readv2"},{"code":"Eu45y12","system":"readv2"},{"code":"Eu41y11","system":"readv2"},{"code":"E201z12","system":"readv2"},{"code":"E201100","system":"readv2"},{"code":"E201611","system":"readv2"},{"code":"E201z00","system":"readv2"},{"code":"E201500","system":"readv2"},{"code":"E201612","system":"readv2"},{"code":"E201300","system":"readv2"},{"code":"Eu45511","system":"readv2"},{"code":"E201.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-disorder-hystericu---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-disorder-hystericu---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-disorder-hystericu---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
