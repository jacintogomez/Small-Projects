def alphabetize_it(filename):
    with open(filename,'r') as file:
        items=[line.strip() for line in file if line.strip()]
    unique_items=sorted(set(items))
    with open(filename,'w') as file:
        for item in unique_items:
            file.write(item+'\n')

fname=input('Enter filename: ')
pathname='word_lists/'+fname
alphabetize_it(pathname)
print('Alphabetized file',pathname)