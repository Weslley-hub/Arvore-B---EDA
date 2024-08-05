from process_data import process_file

# import random

# def generate_input_file(filename, num_numbers):
#     numbers = random.sample(range(1, 10000), num_numbers)
    
#     with open(filename, 'w') as f:
#         for number in numbers:
#             f.write(f"{number}\n")

if __name__ == "__main__":
    
    # filename = "../data/entrada.txt"
    # num_numbers = 201
    # generate_input_file(filename, num_numbers)

    input_file = "../data/entrada.txt"
    output_file = "../data/saida.txt"
    t = 3 
    process_file(input_file, output_file, t)
