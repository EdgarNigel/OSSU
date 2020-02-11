def payingDebt(balance, annualInterestRate, monthlyPaymentRate):
	
	mir = (annualInterestRate / 12)

	for i in range(12):
		mmpr = monthlyPaymentRate * balance
		unpaidBalance = balance - mmpr
		updatedBalance = unpaidBalance + (mir * unpaidBalance)
		balance = updatedBalance
	
	print(round(updatedBalance, 2))

def payingDebtFully(balance, annualInterestRate):
	
	monthlyPaymentRate = 0
	init_balance = balance
	monthlyInterestRate = annualInterestRate/12

	while balance > 0:
		for i in range(12):
			balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
		if balance > 0:
			monthlyPaymentRate += 10
			balance = init_balance
		elif balance <= 0:
			break
	
	print(monthlyPaymentRate)


def payingDebtBiSection(balance, annualInterestRate):

    mir = annualInterestRate / 12
    inititalBalance = balance
    lowerBound = balance / 12
    upperBound = (balance * (1 + mir)**12) / 12
    epsilon = 0.01

    while abs(balance) > epsilon:
        c = (lowerBound + upperBound) / 2
        balance = inititalBalance

        for i in range(12):
            balance = balance - c + (balance - c) * mir

        if balance > epsilon:
            lowerBound = c

        elif balance < -epsilon:
            upperBound = c

        else:
            break

    print(round(c, 2))