def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_elenment = tuple_data[-1]
    return first_element, last_elenment

    
input_tuple = eval(input("Nhập tuple: "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên: ", first)    
print('Phần tử cuối cùng: ', last)