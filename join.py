my_str = 'This is a test'
print ('Normal: ',my_str)

string_element=my_str.split()
print ('Split: ',string_element)

reversed_element=[]
for element in string_element:
	reversed_element.append(element[::-1])
print ('Reversed: ',reversed_element)

new_str = ' '.join(reversed_element)
print ('Reversed Joined: ',new_str)
