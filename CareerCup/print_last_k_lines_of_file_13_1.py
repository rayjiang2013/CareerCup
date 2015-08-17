'''
Write a method to print the last K lines of an input file
'''

def print_last_k_lines_of_file(f,k):
    all_lines=f.readlines()
    num_of_lines=len(all_lines)
    if k>len(all_lines):       
        for l in all_lines:
            l=l.strip('\n')
            print l
    else:
        count=0
        x=num_of_lines/k
        y=num_of_lines%k
        while count<k:
            all_lines[x-1+y+count]=all_lines[x-1+y+count].strip('\n')
            print all_lines[x-1+y+count]
            count+=1
            

            
    
        