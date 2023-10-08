infile = open('Ch06/06_02/begin/values.txt', 'rt')
outfile = open('Ch06/06_02/begin/values_summed.txt', 'wt')

sum = 0
for line in infile:
    sum += int(line)
    print(line.strip(), file= outfile)
print(f'\nTotal is: {sum}', file=outfile)
outfile.close()