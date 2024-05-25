# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Jonathan Green, Carolyn A Chew-Graham, Nav Kapur, Darren M Aschcroft, 2024.

import sys, csv, re

codes = [{"code":"E263z00","system":"readv2"},{"code":"Eu45325","system":"readv2"},{"code":"Eu45323","system":"readv2"},{"code":"E264200","system":"readv2"},{"code":"E264500","system":"readv2"},{"code":"E263.00","system":"readv2"},{"code":"Eu45320","system":"readv2"},{"code":"E265100","system":"readv2"},{"code":"Eu45y13","system":"readv2"},{"code":"Eu45324","system":"readv2"},{"code":"E264000","system":"readv2"},{"code":"E263000","system":"readv2"},{"code":"E265200","system":"readv2"},{"code":"E267.00","system":"readv2"},{"code":"Eu44y13","system":"readv2"},{"code":"Eu45y11","system":"readv2"},{"code":"Eu44412","system":"readv2"},{"code":"Eu46y16","system":"readv2"},{"code":"E261300","system":"readv2"},{"code":"Eu45322","system":"readv2"},{"code":"E261000","system":"readv2"},{"code":"E261400","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["psychogenic-anxiety-disorder---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["psychogenic-anxiety-disorder---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["psychogenic-anxiety-disorder---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
