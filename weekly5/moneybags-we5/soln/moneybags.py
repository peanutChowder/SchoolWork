# Write your solution here.
# (Also, delete these comments before you upload, since they aren't
# relevant to your solution).
numApplicants = input()
applicantMoney = []
found = False

for applicant in range(numApplicants):
	applicantMoney.append(int(input()))

applicants = sorted(applicantMoney, reverse=True)
guess = numApplicants // 2
increment = guess // 2

while not found:
	cutoffPerson = applicants[guess]
	cutoffMoney = guess + 1

	if increment == 0:
		found = True
		
	if cutoffPerson < cutoffMoney:
		guess -= increment

	elif cutoffPerson > cutoffMoney:
		guess += increment

	elif cutoffMoney == 


	increment /= 2
