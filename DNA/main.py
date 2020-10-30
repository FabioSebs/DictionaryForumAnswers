from bio import kmercounts as kc

dna = input("Enter DNA: ")
k = int(input("Enter K: "))

if __name__ == "__main__":
    print(kc(dna, k))