from django.shortcuts import render

# Create your views here.
def mainscreen(request):
    return render(request,"web2/frontpage.html")
score=0
def page2(request):
    list1=[]
    t=1
    h=1
    for i in question:
        list2=[]
        z=1
        for j in question[i]:
            list2.append(createquestion(t,h,z))
            t+=1
            z+=1
        h+=1
        list1.append(list2)
    questions={}
    t=0
    for i in queslist:
        questions[i]=list1[t]
        t+=1
    # print(questions)
    return render(request,"web2/page2.html",context={"questions":questions})

def page3(request):
    if request.method=="POST":
        dict=request.POST.dict()
        del dict['csrfmiddlewaretoken']
        
    return render(request,"web2/page3.html",context={"age":age,"household":household})

def page4(request):
    if request.method=="POST":
        dict=request.POST.dict()
        del dict['csrfmiddlewaretoken']
        score=0
        for i in dict:
            z=dict[i].split("_")
            score+=(int(z[1])-1)
        for i in outcome:
            if score <= int(i): 
                result = outcome[i]
                break
    total=30
    return render(request,"web2/page4.html",context={"marks":score,"total":total,"result":result})


def createquestion(t,h,z):
    return '''<div class="radio">
        <input type="radio" id="a{0}" name="q{1}" value="q{1}_{2}" onclick="resetmsg()" required="required"/>
        <label class="btn btn-default" for="a{0}">{3}</label>
    </div>'''.format(t,h,z,question['q%d'%(h)][z-1])

question = {
    "q1": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q2": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q3": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q4": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q5": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q6": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q7": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q8": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q9": ["NOT AT ALL","SEVERAL DAYS","MORE THAN HALF THE DAYS","NEARLY EVERY DAY"],
    "q10": ["NOT DIFFICULT AT ALL","SOMEWHAT DIFFICULT","VERY DIFFICULT","EXTREMELY DIFFICULT"]
}
queslist = [
    "1. Little interest or pleasure in doing things",
    "2. Feeling down, depressed, or hopeless",
    "3. Trouble falling or staying asleep, or sleeping too much",
    "4. Feeling tired or having little energy",
    "5. Poor appetite or overeating",
    "6. Feeling bad about yourself - or that you are a failure or have let yourself or your family down",
    "7. Trouble concentrating on things, such as reading the newspaper or watching television",
    "8. Moving or speaking so slowly that other people could have noticed Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual",
    "9. Thoughts that you would be better off dead, or of hurting yourself",
    " 10. If you checked off any problems, how difficult have these problems made it for you at work, home, or with other people?"
]    
age='''<select id="age-range" name="age-range">
        <option value="0">None</option>
        <option value="1000">1000</option>
        <option value="2500">2500</option>
        <option value="5000">5000</option>
        </select>'''

household='''<select id="household-income" name="household-income">
        <option value="0">None</option>
        <option value="1000">1000</option>
        <option value="2500">2500</option>
        <option value="5000">5000</option>
        </select>'''

outcome = {'0':'No Depression',
           '10':'Mild Depression',
           '20':'Moderate Depression',
           '30':'Severe Depression'
        }


