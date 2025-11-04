import streamlit as st

st.title('CALCULATOR')

first_num = st.number_input('Enter A First Number')
second_num = st.number_input('Enter a Second Number')

operation = st.selectbox('Choose Operation : ',
                         ( '➕', '➖', '❌', '➗', 'PERCENTAGE') )

if st.button('==CALCULATE=='):
    if operation == '➕':
        result= first_num + second_num 
        st.success(f'The Addition of {first_num} and {second_num} is : {result}')
    elif operation == '➖':
        result= first_num - second_num 
        st.success(f'The Substraction of {first_num} and {second_num} is : {result}')
    elif operation == '❌':
        result= first_num * second_num 
        st.success(f'The Multiplication of {first_num} and {second_num} is : {result}')
    elif operation == 'PERCENTAGE':
        result= (first_num * second_num)/100 
        st.success(f'The {second_num} Percentage of {first_num} is : {result}')
    elif operation == '➗':
        if (second_num != 0):
            result = first_num / second_num
            st.success(f'The Division of {first_num} and {second_num} is : {result}')
        else:
            st.error('Cannot divide by Zero ❌')

    
    