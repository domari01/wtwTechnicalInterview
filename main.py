import os

with open(os.getcwd()+"/"+"input") as f:
    lines = f.readlines()

orgn_yr = []


orgn_yr_comp = []

inc_val = []
orgn_yr_NonComp = []
inc_val1 = []



for line in lines:

    line = line.rstrip()
    n_line = line.split(",")

    if n_line[0] == "Comp" or n_line[0] == "Non-Comp":
        nxt_line = n_line[1]
        orgn_yr.append(int(nxt_line))


    if n_line[0] == "Comp":
        orgn_yr_comp.append(n_line[1].lstrip())
        inc_val.append(float(n_line[-1].lstrip()))

    if n_line[0] == "Non-Comp":
        orgn_yr_NonComp.append(n_line[1].lstrip())
        inc_val1.append(float(n_line[-1].lstrip()))



fst_orgn_yr_comp = orgn_yr_comp[0]
fst_inc_val = inc_val[0]

comp = ""
comp += str(inc_val[0]).replace(".0", "")
count = 0
cum1 = 0



for i in range(1, len(orgn_yr_comp)):
    if orgn_yr_comp[i] == fst_orgn_yr_comp:

        count += 1
        if count > 1:
            sum1 = inc_val1[i] + cum1
            comp += ", " + str(sum1).replace(".0", "")

        else:
            summ = inc_val[i] + fst_inc_val
            comp += ", " + str(summ).replace(".0", "")
            fst_orgn_yr_comp = orgn_yr_NonComp[i]
            fst_inc_val = inc_val1[i]
            cum1 = summ



    else:
        comp += ", " +str(inc_val[i]).replace(".0", "")
        fst_orgn_yr_comp = orgn_yr_comp[i]
        fst_inc_val = inc_val[i]


fst_orgn_yr_Noncomp = orgn_yr_NonComp[0]
fst_inc_val = inc_val1[0]

NonComp = ""
NonComp += str(inc_val1[0]).replace(".0", "")
count = 0
cum1 = 0
for i in range(1, len(orgn_yr_NonComp)):
    if orgn_yr_NonComp[i] == fst_orgn_yr_Noncomp:

            count += 1
            if count > 1:
                sum1 = inc_val1[i] + cum1
                NonComp += ", " + str(sum1).replace(".0", "")

            else:
                summ = inc_val1[i] + fst_inc_val
                NonComp += ", "+ str(summ).replace(".0", "")
                fst_orgn_yr_Noncomp = orgn_yr_NonComp[i]
                fst_inc_val = inc_val1[i]
                cum1 = summ



    else:
        NonComp += ", " + str(inc_val1[i]).replace(".0", "")
        fst_orgn_yr_comp = orgn_yr_NonComp[i]
        fst_inc_val = inc_val1[i]
        count = 0







#print(dev_yrs)
#print(i_val1)
#print(org_yr_NonComp)
earliest_origin_yr = min(orgn_yr)
latest_origin_yr = max(orgn_yr)
dev_yr = (latest_origin_yr - earliest_origin_yr)+1
#write lines 16 and 18 into the output file
with open(os.getcwd()+"/"+"balance", "w") as writing:
    for i in range(0, 3):
        if i == 0:
            writing.write(str(earliest_origin_yr) + ", " + str(dev_yr) +"\n")

        if i == 1:
            writing.write("Comp" + ", " + comp + "\n")

        if i == 2:


            writing.write("Non-Comp" + ", " + NonComp + "\n")


    writing.close()












