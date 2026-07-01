# DNA analysis Toolkit
# Analyzes DNA sequences from FASTA files
# Author: Jaina Modi

def is_valid(sequence):
    ##Check if a sequence contains only valid DNA bases(A,T,G,C)##
    allowed = "ATCG"
    for base in sequence:
        if base not in allowed:
            return False
    return True


def base_counts(sequence):
    ##Count occurrences of each base in the sequence##
    a=sequence.count("A")
    t=sequence.count("T")
    g=sequence.count("G")
    c=sequence.count("C")
    print(f"A:{a} | T:{t} | G:{g} | C:{c}")

def gc_content(sequence):
     ##Calculate GC content as a percentage##
     g=sequence.count("G")
     c=sequence.count("C")
     return (g+c)/len(sequence)*100

def transcribe(sequence):
     ##Transcribe DNA sequence into RNA##
     rna=sequence.replace("T","U")
     return rna

def complement(sequence):
     ##Return a complementary DNA strand##
     result=""
     for base in sequence:
          if base=="A":
                result=result+"T"
          elif base=="T":
                result=result+"A"
          elif base=="G":
                result=result+"C"
          elif base=="C":
                result=result+"G"
     return result

def dna_report(name,sequence):
     ##Print a full analysis report for a single DNA sequence##
     print(f"\n{'='*40}")
     print(f"Sequence:{name}")
     print(f"{'='*40}")
     if  is_valid(sequence):
          print(f"Length:{len(sequence)}bp")
          print(f"GC content: {gc_content(sequence):.2f}%")
          print(f"Base counts:")
          base_counts(sequence)
          print(f"Transcript: {transcribe(sequence)}")
          print(f"Complement: {complement(sequence)}")
     else:
          print("Invalid sequence — contains non-DNA characters")


def read_fasta(filename):
##Read a FASTA file and return a list of (name, sequence) tuples##
     sequences=[]
     name=""
     sequence=""
     with open(filename,"r") as file:
          for line in file:
               line=line.strip()
               if line.startswith(">"):
                    if name and sequence:
                         sequences.append((name,sequence))
                    name=line[1:]
                    sequence=""
               else:
                    sequence=sequence+line
     if name and sequence:
          sequences.append((name, sequence))
     return sequences

if __name__=="__main__":
     sequences=read_fasta("sequences.fasta")
     for name, sequence in sequences:
          dna_report(name,sequence)
