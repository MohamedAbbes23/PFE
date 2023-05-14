a='1000'
b= int(a, 2)

print(b)

a = 'GGAGCGAGAGAGTGAG'
a = 'GGAGCGAGTGAGTAAG'

def XorBio(word1,word2):
    final = ''
    for i in range(len(word1)):
        if(word1[i] == 'A'):
            match word2[i]:
                case 'A':
                    final +='A' 
                case 'T':
                    final +='T'
                case 'C':
                    final +='C' 
                case 'G':
                    final +='G'
        if(word1[i] == 'T'):
            match word2[i]:
                case 'A':
                    final +='T' 
                case 'T':
                    final +='A'
                case 'C':
                    final +='G' 
                case 'G':
                    final +='C'
        if(word1[i] == 'C'):
            match word2[i]:
                case 'A':
                    final +='C' 
                case 'T':
                    final +='G'
                case 'C':
                    final +='A' 
                case 'G':
                    final +='T'
        if(word1[i] == 'G'):
            match word2[i]:
                case 'A':
                    final +='G' 
                case 'T':
                    final +='A'
                case 'C':
                    final +='T' 
                case 'G':
                    final +='C'
    return final 


a='ATCG'
b='GGGG'
print(XorBio(b,a))

    
    
