wf = float(input('Enter the weight of the fishes'))

if wf > 50.0:
    print(f'The excess is {wf - 50}')
    print(f'The fine is {(wf - 50) * 4} dols')

else:
    print("The weight dosen't generates a fine")
