import re
with open('q04.in') as f:
    src = f.read().split('\n\n')

fields = {'required': ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], 
          'optional': ['cid']}

valid_passports = 0
for passport in src: 
    detected_fields = re.findall(r"\w+(?=:)", passport)
    if(all(item in detected_fields for item in fields['required'])):
        valid_passports += 1
print(f"Answer 1: {valid_passports}")

valid_passports = 0
for passport in src: 
    # Check if all values are present 
    detected_fields = re.findall(r"\w+(?=:)", passport)
    if(all(item in detected_fields for item in fields['required'])):
        # Data validation
        byr = re.findall(r"(?<=byr:)\d{4}(?=\b)", passport)
        iyr = re.findall(r"(?<=iyr:)\d{4}(?=\b)", passport)
        eyr = re.findall(r"(?<=eyr:)\d{4}(?=\b)", passport)
        hgt = re.findall(r"(?<=hgt:)\d{2,3}(?=[cm|in])", passport)
        hgt_unit = re.search(r"hgt:(\d+)(\w+)", passport).group(2)
        hcl = re.findall(r"(?<=hcl:)#[a-f|0-9]{6}", passport)
        ecl = re.findall(r"(?<=ecl:)amb|blu|brn|gry|grn|hzl|oth(?=\b)", passport)
        pid = re.findall(r"(?<=pid:)\d{9}(?=\b)", passport)
        # If any are empty, do nothing
        if 0 in [len(field) for field in [byr, iyr, eyr, hgt, hcl, ecl, pid]]:
            print(f"invalid: {byr, iyr, eyr, hgt, hgt_unit, hcl, ecl, pid}") 
        # Additional checks
        elif (1920 <= int(byr[0]) <= 2002 and \
              2010 <= int(iyr[0]) <= 2020 and \
              2020 <= int(eyr[0]) <= 2030) and \
              ((hgt_unit == 'cm' and 150 <= int(hgt[0]) <= 193) or 
               (hgt_unit == 'in' and 59 <= int(hgt[0]) <= 76)):
            print(f"valid: {byr, iyr, eyr, hgt, hgt_unit, hcl, ecl, pid}") 
            valid_passports += 1
        else: 
            print(f"invalid: {byr, iyr, eyr, hgt, hgt_unit, hcl, ecl, pid}") 
    else: 
        print(f"invalid: {byr, iyr, eyr, hgt, hgt_unit, hcl, ecl, pid}") 
print(f"Answer 2: {valid_passports}")