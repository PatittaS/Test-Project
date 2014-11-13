def calbmr(sex, high, weight, age):
    '''Calculate BMR (Basal Metabolic Rate)
    from sex high weight and age.'''
    if sex == 'male':
        return int((66 + (13.7 * weight) + (5 * high) - (6.8 * age)))
    else:
        return int((665 + (9.6 * weight) + (1.8 * high) - (4.7 * age)))


def caltdee(excer):
    '''Calculate TDEE(Tatal Daily Energy Expenditure)
    from BMR multiply How many excercise/week.'''
    cage = ['alway', 'usually', 'often', 'sometimes', 'never']
    bmr = calbmr(raw_input(), input(), input(), input())
    for _ in cage:
        if excer == cage[0]:
            return str(int(bmr * 1.9)) + ' kcal'
        elif excer == cage[1]:
            return str(int(bmr * 1.725)) + ' kcal'
        elif excer == cage[2]:
            return str(int(bmr * 1.55)) + ' kcal'
        elif excer == cage[3]:
            return str(int(bmr * 1.375)) + ' kcal'
        else:
            return str(int(bmr * 1.2)) + ' kcal'
            
            blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
print caltdee(raw_input())


