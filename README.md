# programming-exercise
My programming exercise in computational linguistics

Exercise 1 
Problem: Write a function that takes a string as input and returns the frequency of each word in the string.

Exercise 2
Problem: Write a function that takes two textual files as inputs. The function should merge the contents into a new file. In the merged file, even-indexed lines come from the first file and odd-indexed lines from the second. Each line should have three columns: line number, original filename, and content, separated by tabs. 

Exercise 4 
Problem: Download and decompress the file "Dataset_Xiang-Kuperberg_2015.zip". In the decompressed "Dataset_Xiang-Kuperberg_2015.txt" file, you'll find sentences for psycholinguistic experiments. Your task is to prepare these sentences for some deep neural models (e.g., BERT). 

(1)	Write a function replacing the target word (fifth column) in the sentence (third column) with the tag '[MASK]'. Retain all other fields unchanged.

(2)	Write another function randomly select a word in the sentence (third column) and replace it with the tag '[UNK]'. Retain all other fields unchanged.
