from flask import Flask, request, render_template
import experta

# Flask constructor
app = Flask(__name__)


class DateSize(experta.Fact):
    pass


class DateTaste(experta.Fact):
    pass


class DatePrice(experta.Fact):
    pass


class DateCal(experta.Fact):
    pass


class DateTexture(experta.Fact):
    pass


class DateWater(experta.Fact):
    pass


class DateTypeR(experta.KnowledgeEngine):
    global type
    type = "there is no type for your choices at the moment"



    #seting the rules that are requierd for gussing the date type
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('sweet')), DatePrice(has=('L')), DateCal(has=('H')),
                              DateTexture(has=('soft')), DateWater(has=('H'))))
    #seting the method to print the date type
    def guess_DateSarri(self):
        #printing the date type
        print("Date is Sarri")
        global type
        type = "Date is Sarri"
    #the same code for all date types
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('fare')), DatePrice(has=('L')), DateCal(has=('M')),
                              DateTexture(has=('hard')), DateWater(has=('M'))))
    def guess_DateBarni(self):
        print("Date is barni")
        global type
        type = "Date is barni"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('sweet')), DatePrice(has=('L')), DateCal(has=('H')),
                              DateTexture(has=('soft')), DateWater(has=('H'))))
    def guess_DateMaktomi(self):
        print("Date is maktomi")
        global type
        type = "Date is maktomi"
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('sweet')), DatePrice(has=('L')), DateCal(has=('H')),
                              DateTexture(has=('soft')), DateWater(has=('H'))))
    def guess_DateSaif(self):
        print("Date is nabtat saif")
        global type
        type = "Date is nabtat saif"
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('fare')), DatePrice(has=('H')), DateCal(has=('L')),
                              DateTexture(has=('hard')), DateWater(has=('M'))))
    def guess_DateBarhi(self):
        print("Date is barhi")
        global type
        type = "Date is barhi"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('fare')), DatePrice(has=('M')), DateCal(has=('M')),
                              DateTexture(has=('soft')), DateWater(has=('L'))))
    def guess_DateSafawi(self):
        print("Date is safawi")
        global type
        type = "Date is safawi"
    @experta.Rule(experta.AND(DateSize(has=('L')), DateTaste(has=('sweet')), DatePrice(has=('M')), DateCal(has=('M')),
                              DateTexture(has=('medium')), DateWater(has=('M'))))
    def guess_DateSufri(self):
        print("Date is sufri")
        global type
        type = "Date is sufri"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('sweet')), DatePrice(has=('L')), DateCal(has=('M')),
                              DateTexture(has=('soft')), DateWater(has=('M'))))
    def guess_DateRaziz(self):
        print("Date is raziz")
        global type
        type = "Date is raziz"
    @experta.Rule(experta.AND(DateSize(has=('L')), DateTaste(has=('fare')), DatePrice(has=('H')), DateCal(has=('L')),
                              DateTexture(has=('medium')), DateWater(has=('M'))))
    def guess_DateAnbarah(self):
        print("Date is anbarah")
        global type
        type = "Date is anbarah"
    @experta.Rule(experta.AND(DateSize(has=('L')), DateTaste(has=('fare')), DatePrice(has=('L')), DateCal(has=('L')),
                              DateTexture(has=('medium')), DateWater(has=('L'))))
    def guess_DateKhudri(self):
        print("Date is khudri")
        global type
        type = "Date is khudri"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('sweet')), DatePrice(has=('L')), DateCal(has=('M')),
                              DateTexture(has=('medium')), DateWater(has=('H'))))
    def guess_DateShishi(self):
        print("Date is shishi")
        global type
        type = "Date is shishi"
    @experta.Rule(experta.AND(DateSize(has=('L')), DateTaste(has=('fare')), DatePrice(has=('H')), DateCal(has=('L')),
                              DateTexture(has=('medium')), DateWater(has=('M'))))
    def guess_DateMajdool(self):
        print("Date is majdool")
        global type
        type = "Date is majdool"
    @experta.Rule(
        experta.AND(DateSize(has=('M')), DateTaste(has=('sweet')), DatePrice(has=('H')), DateCal(has=('M')),
                    DateTexture(has=('soft')), DateWater(has=('H'))))
    def guess_DateKhulas(self):
        print("Date is khulas")
        global type
        type = "Date is khulas"
    @experta.Rule(
        experta.AND(DateSize(has=('S')), DateTaste(has=('sweet')), DatePrice(has=('VH')), DateCal(has=('M')),
                    DateTexture(has=('medium')), DateWater(has=('L'))))
    def guess_DateAjwah(self):
        print("Date is ajwah")
        global type
        type = "Date is ajwah"
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('fare')), DatePrice(has=('M')), DateCal(has=('M')),
                              DateTexture(has=('medium')), DateWater(has=('M'))))
    def guess_DateSaqee(self):
        print("Date is saqee")
        global type
        type = "Date is saqee"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('fare')), DatePrice(has=('L')), DateCal(has=('H')),
                              DateTexture(has=('hard')), DateWater(has=('L'))))
    def guess_DateAli(self):
        print("Date is nabtat ali")
        global type
        type = "Date is nabtat ali"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('sweet')), DatePrice(has=('M')), DateCal(has=('H')),
                              DateTexture(has=('soft')), DateWater(has=('H'))))
    def guess_DateHulwa(self):
        print("Date is hulwa")
        global type
        type = "Date is hulwa"
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('sweet')), DatePrice(has=('M')), DateCal(has=('L')),
                              DateTexture(has=('hard')), DateWater(has=('H'))))
    def guess_DateSukari(self):
        print("Date is Sukari")
        global type
        type = "Date is Sukari"
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('fare')), DatePrice(has=('H')), DateCal(has=('M')),
                              DateTexture(has=('hard')), DateWater(has=('L'))))
    def guess_DateNour(self):
        print("Date is deglet Nour")
        global type
        type = "Date is deglet Nour"
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('fare')), DatePrice(has=('L')), DateCal(has=('L')),
                              DateTexture(has=('soft')), DateWater(has=('M'))))
    def guess_DateZahedi(self):
        print("Date is zahedi")
        global type
        type = "Date is zahedi"
    @experta.Rule(experta.AND(DateSize(has=('L')), DateTaste(has=('fare')), DatePrice(has=('VH')), DateCal(has=('H')),
                              DateTexture(has=('hard')), DateWater(has=('L'))))
    def guess_DateThore(self):
        print("Date is thore")
        global type
        type = "Date is thore"
    @experta.Rule(experta.AND(DateSize(has=('L')), DateTaste(has=('fare')), DatePrice(has=('M')), DateCal(has=('M')),
                              DateTexture(has=('medium')), DateWater(has=('H'))))
    def guess_DatePiarom(self):
        print("Date is piarom")
        global type
        type = "Date is piarom"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('sweet')), DatePrice(has=('VH')), DateCal(has=('M')),
                              DateTexture(has=('medium')), DateWater(has=('M'))))
    def guess_DateMazafati(self):
        print("Date is Mazafati ")
        global type
        type = "Date is Mazafati"
    @experta.Rule(experta.AND(DateSize(has=('L')), DateTaste(has=('sweet')), DatePrice(has=('L')), DateCal(has=('H')),
                              DateTexture(has=('soft')), DateWater(has=('L'))))
    def guess_DateSukarriDry(self):
        print("Date is sukarri Dry ")
        global type
        type = "Date is sukarri Dry"
    @experta.Rule(experta.AND(DateSize(has=('M')), DateTaste(has=('sweet')), DatePrice(has=('L')), DateCal(has=('M')),
                              DateTexture(has=('medium')), DateWater(has=('M'))))
    def guess_DateSayer(self):
        print("Date is Sayer")
        global type
        type = "Date is Sayer"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('fare')), DatePrice(has=('H')), DateCal(has=('L')),
                              DateTexture(has=('hard')), DateWater(has=('M'))))
    def guess_DateKabkab(self):
        print("Date is Kabkab ")
        global type
        type = "Date is Kabkab"
    @experta.Rule(experta.AND(DateSize(has=('S')), DateTaste(has=('fare')), DatePrice(has=('M')), DateCal(has=('M')),
                              DateTexture(has=('hard')), DateWater(has=('L'))))
    def guess_DateHalel(self):
        print("Date is halel ")
        global type
        type = "Date is halel"




    print("Welcome to date calssification system")
    #asking the user for thier location for data colliction
    #location = input("please enter your region: ")



#method for getting the data needed from the user
def QandA():
    #initiating a variable for needed loops
    i = 0
    #global variable so the expert system can read it
    global DSize
    #loop for takning the right ansowers from the user (in the final form the loops wont be needed because it will be a multiable choice quistion)
    while i==0:
        #geting the info from the user
        DSize = wSize
        if DSize == 'S':
            i=1
            break
        if DSize == 'M':
            i=1
            break
        if DSize == 'L':
            i=1
            break
        else:
            print("Please enter one of these choices: S, M, L")
        # the same code for all date facts
    i = 0
    global DTaste
    while i == 0:

        DTaste = wTaste
        if DTaste == 'sweet':
            i = 1
            break
        if DTaste == 'fare':
            i = 1
            break
        else:
            print("Please enter one of these choices: fare, Sweet")


    i = 0
    global DPrice
    while i == 0:

        DPrice = wPrice
        if DPrice == 'L':
            i = 1
            break
        if DPrice == 'M':
            i = 1
            break
        if DPrice == 'H':
            i = 1
            break
        if DPrice == 'VH':
            i = 1
            break
        else:
            print("Please enter one of these choices: L, M, H, VH")

    i = 0
    global DCalories
    while i == 0:

        DCalories = wCalories
        if DCalories == 'L':
            i = 1
            break
        if DCalories == 'M':
            i = 1
            break
        if DCalories == 'H':
            i = 1
            break
        else:
            print("Please enter one of these choices: L, M, H")

    i = 0
    global DTexture
    while i == 0:

        DTexture = wTexture
        if DTexture == 'soft':
            i = 1
            break
        if DTexture == 'medium':
            i = 1
            break
        if DTexture == 'hard':
            i = 1
            break
        else:
            print("Please enter one of these choices: soft, medium, hard")

    i = 0
    global DWater
    while i == 0:

        DWater = wWater
        if DWater == 'L':
            i = 1
            break
        if DWater == 'M':
            i = 1
            break
        if DWater == 'H':
            i = 1
            break
        else:
            print("Please enter one of these choices: L, M, H")

    i = 0
#method for the test itself
def test():
    #calling the Q and A method to get the info from the user
    QandA()
    #seting the knoledge engin
    engine = DateTypeR()
    engine.reset()

    #gussing the date type for the user based on his answers
    engine.declare(DateSize(has=DSize), DateTaste(has=DTaste), DatePrice(has=DPrice), DateCal(has=DCalories),
                   DateTexture(has=DTexture), DateWater(has=DWater))

    #if the user chose the price to be very high, it will guess all date types with the prices
    if DPrice == 'VH':
        engine.declare(DateSize(has=DSize), DateTaste(has=DTaste), DatePrice(has="H"), DateCal(has=DCalories),
                       DateTexture(has=DTexture), DateWater(has=DWater))
        engine.declare(DateSize(has=DSize), DateTaste(has=DTaste), DatePrice(has="M"), DateCal(has=DCalories),
                       DateTexture(has=DTexture), DateWater(has=DWater))
        engine.declare(DateSize(has=DSize), DateTaste(has=DTaste), DatePrice(has="L"), DateCal(has=DCalories),
                       DateTexture(has=DTexture), DateWater(has=DWater))

    if DPrice == 'H':
        engine.declare(DateSize(has=DSize), DateTaste(has=DTaste), DatePrice(has="M"), DateCal(has=DCalories),
                       DateTexture(has=DTexture), DateWater(has=DWater))
        engine.declare(DateSize(has=DSize), DateTaste(has=DTaste), DatePrice(has="L"), DateCal(has=DCalories),
                       DateTexture(has=DTexture), DateWater(has=DWater))

    if DPrice == 'M':
        engine.declare(DateSize(has=DSize), DateTaste(has=DTaste), DatePrice(has="L"), DateCal(has=DCalories),
                       DateTexture(has=DTexture), DateWater(has=DWater))

    engine.run()













# A decorator used to tell the application
# which URL is associated function
@app.route('/EX', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        global wSize
        global wTaste
        global wPrice
        global wCalories
        global wTexture
        global wWater

        #type = "there is no type for your choices at the moment"
        # getting input with name = fname in HTML form
        wSize = request.form.get("wsize")
        # getting input with name = lname in HTML form
        wTaste = request.form.get("wtaste")

        wPrice = request.form.get("wprice")

        wCalories = request.form.get("wcalories")

        wTexture = request.form.get("wtexture")

        wWater = request.form.get("wwater")
        test()

        return type
    return render_template("form.html")


if __name__ == '__main__':
    app.run(port=3001)
    app.run()