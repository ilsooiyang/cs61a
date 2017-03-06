def bathtub(n):

    def ducky_annihilator(rate):
        def ducky():
            nonlocal n
            n -= rate
            return "{0} rubber duckies left".format(n)
        return ducky

    return ducky_annihilator

annihilator = bathtub(500)
darth_vader = annihilator(10)
print(darth_vader())
obi_wan = annihilator(-20)
print(obi_wan())
print(darth_vader())
