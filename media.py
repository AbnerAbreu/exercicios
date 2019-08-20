import statistics as st

nota1 = float(input('digite sua primeira nota'))
nota2 = float(input('digite sua segunda nota'))
nota3 = float(input('digite sua terceira nota'))
nota4 = float(input('digite sua quarta nota'))

media = st.mean([nota1,nota2,nota3,nota4])

print('Sua média é: ' +str(media))