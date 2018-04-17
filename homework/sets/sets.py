# Matthew Kosloski
# Exercise 9-6
# CPSC 3310-01 SP2018

def main():
    # Get input text of first file and create set containing 
    # its unique words
    input_name = input('Enter the name of the first input file: ')
    file1 = open(input_name, 'r')
    text1 = file1.read()
    file1.close()
    words1 = text1.split()
    set1 = set(words1)

    # Get input text of second file and create set containing its 
    # unique words
    input_name = input('Enter the name of the second input file: ')
    file2 = open(input_name , 'r')
    text2 = file2.read() 
    file2.close()
    words2 = text2.split() 
    set2 = set(words2)

    # Obtain the union of the sets and print the items in it
    union = set1.union(set2)
    print('These are the unique words that are ' \
          'contained in both files:')
    for item in union: 
        print(item)
    print()

    # Obtain the intersection of the sets and print the items in it
    intersection = set1.intersection(set2)
    print('These are the words that appear in both files:')
    for item in intersection: 
        print(item)
    print()

    # Obtain the difference between set1 and set2 and 
    # print the items in it
    difference1 = set1.difference(set2)  
    print('These are the words that appear in the first file' \
          ' but do not appear in the second file:')
    for item in difference1: 
        print(item)
    print()

    # Obtain the difference between set2 and set1 and 
    # print the items in it
    difference2 = set2.difference(set1) 
    print('These are the words that appear in the second file' \
          ' but do not appear in the first file:')
    for item in difference2: 
        print(item)
    print()

    # Obtain the symmetric difference between set1 and set2 
    # and print the items in it
    sym_diff = set1.symmetric_difference(set2)
    print('These are the words that appear in the first' \
          ' file or the second file but do not appear in' \
          ' the both files:')
    for item in sym_diff: 
        print(item)
    print()

main()

