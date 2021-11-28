# Write your solution here.
# (Also, delete these comments before you upload, since they aren't
# relevant to your solution).
numApplicants = int(input())
applicantMoney = []
found = False

for applicant in range(numApplicants):
	applicantMoney.append(int(input()))

applicants = sorted(applicantMoney, reverse=True)
guess = numApplicants // 2
increment = guess // 2 + 1
bestGuess = 0

if not increment:
	increment = 1

while not found:
	cutoffPerson = applicants[guess]
	cutoffMoney = guess + 1
		
	if cutoffPerson < cutoffMoney:
		guess -= increment

	elif cutoffPerson >= cutoffMoney:
		if guess > bestGuess:
			bestGuess = guess
		else:
			found = True

		guess += increment
	
	if increment > 1:
		increment = increment // 2

print("outpet", bestGuess + 1)
