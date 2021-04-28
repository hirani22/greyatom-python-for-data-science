# --------------
#Code starts here
#Function to read file
def read_file(path):
    file = open(path,'r')
    sentence= file.read()
    file.close
    return sentence
    #Opening of the file located in the path in 'read' mode
    #Reading of the first line of the file and storing it in a variable
    #Closing of the file
    #Returning the first line of the file
   
    

#Calling the function to read file
sample_message= read_file(file_path)
#Printing the line of the file
print(sample_message)
message_1= read_file(file_path_1)
message_2= read_file(file_path_2)
print(message_1)
print(message_2)


#Function to fuse message
def fuse_msg(message_a,message_b):
    quotient=int(message_b)//int(message_a)
    return str(quotient)

secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)

#Calling the function to read file  
message_3=read_file(file_path_3)
#Calling the function to read file
print(message_3)

#Function to substitute the message
def substitute_msg(message_c):
    if(message_c=="Red"):
        sub="Army General"
    elif(message_c=="Green"):
        sub="Data Scientist"
    elif(message_c=="Blue"):
        sub="Marine Biologist"
    return sub

#Calling the function to read file
secret_msg_2= substitute_msg(message_3)
print(secret_msg_2)

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)

#Function to compare message
def compare_msg(message_d,message_e):
    a_list= message_d.split()
    b_list= message_e.split()
    #Comparing the elements from both the lists
    c_list=[]
    for i in a_list:
        if i not in b_list:
            c_list.append(i)
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)
#Calling the function to read file
message_6=read_file(file_path_6)
print(message_6)

#Function to filter message
def extract_msg(message_f):
    a_list=message_f.split()
    even_word=lambda x:len(x)%2==0
    b_list= list(filter(even_word, a_list))
    final_msg= " ".join(b_list)
    return final_msg
  
#Calling the function to read file
secret_msg_4=extract_msg(message_6)
print(secret_msg_4)


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg=" ".join(message_parts)

# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message

#Function to write inside a file
def write_file(secret_msg,path):
    file=open(final_path, 'a+')
    file.write(secret_msg)
    file.close()

write_file(secret_msg, final_path)
print(secret_msg)

#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


