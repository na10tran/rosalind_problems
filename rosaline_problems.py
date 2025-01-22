def counting_dna_nucleotides(dna_string):
    num_character = []
    dna_string = dna_string.upper()
    num_character.append(dna_string.count("A"))
    num_character.append(dna_string.count("C"))
    num_character.append(dna_string.count("G"))
    num_character.append(dna_string.count("T"))
    
    return num_character

def transcribing_dna_into_rna(dna_string):
    return dna_string.replace('T', 'U')
    
def complementing_strand_dna(dna_string):
    reverse = dna_string[::-1]
    
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    reversed = "".join(complement[base] for base in reverse)
    return reversed
    

def main():
    input_file = "rosalind_dna.txt"
    output_file = "answer.txt"

    try:
        with open(input_file, "r") as file:
            dna = file.read().strip()  
            
        answer = complementing_strand_dna(dna)
        print(answer)
        

        #with open(output_file, "w") as file:
        #    file.write(" ".join(map(str, answer)))

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    


if __name__ == "__main__":
    main()