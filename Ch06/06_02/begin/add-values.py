infile = open('Ch06/06_02/begin/values.txt', 'r')
outfile = open('Ch06/06_02/begin/values-totaled.txt', 'w')
print('Processing input')
sum = 0
for line in infile:
    sum += int(line)
    print(line.rstrip(), file=outfile)
print('\nTotal: ' + str(sum), file=outfile)
outfile.close()
print('Output complete')
