df.loc[df["sex"]=="male","sex"] = 0
df.loc[df["sex"]=="female","sex"] = 1

df.loc[df["smoker"]=="no","smoker"] = 0
df.loc[df["smoker"]=="yes","smoker"] = 1

df.loc[df["region"]=="northwest","region"] = 0
df.loc[df["region"]=="northeast","region"] = 1
df.loc[df["region"]=="southwest","region"] = 2
df.loc[df["region"]=="southeast","region"] = 3

df = df.astype({"sex":"category"})
df = df.astype({"smoker":"category"})
df = df.astype({"region":"category"})

smoker = df[df["smoker"]=="yes"]["smoker"].count()
dontSmoker = df[df["smoker"]=="no"]["smoker"].count()

underWeight = df[df["bmi"]<18.5]["bmi"].count()
healthyWeight = df[(df["bmi"]>=18.5)&(df["bmi"]<24.9)]["bmi"].count()
overWeight = df[(df["bmi"]>=24.9)&(df["bmi"]<29.9)]["bmi"].count()
obeseWeight = df[(df["bmi"]>=29.9)&(df["bmi"]<39.9)]["bmi"].count()
extremlyObeseWeight = df[df["bmi"]>=39.9]["bmi"].count()

baby = df[df["age"]<3]["age"].count()
child = df[(df["age"]>=3)&(df["age"]<17)]["age"].count()
young = df[(df["age"]>=18)&(df["age"]<30)]["age"].count()
adult = df[(df["age"]>=30)&(df["age"]<50)]["age"].count()
old = df[df["age"]>=50]["age"].count()

def ageRange(age):
    if age<3:
        return 0
    elif age >=3 and age <17:
        return 1
    elif age >=18 and age <30:
        return 2
    elif age >=30 and age <50:
        return 3
    else:
        return 4

def bmiRange(bmi):
    if bmi<18.5:
        return 0
    elif bmi >=18.5 and bmi <24.9:
        return 1
    elif bmi >=24.9 and bmi <29.9:
        return 2
    elif bmi >=29.9 and bmi <39.9:
        return 3
    else:
        return 4

def chargesRange(charge,df):
    q1 = df.quantile(0.25)
    median = df.quantile(0.5)
    q3 = df.quantile(0.75)

    if charge < q1:
        return 0
    elif charge >= q1 and charge < median:
        return 1
    elif charge >= median and charge < q3:
        return 2
    else:
        return 3

df["age range"] = df["age"].apply(lambda x:ageRange(x))
df["bmi range"] = df["bmi"].apply(lambda x:bmiRange(x))
df["charges range"] = df["charges"].apply(lambda x:chargesRange(x,df["charges"]))



nonSmokerQ1 = df.loc[df["smoker"]==0]["charges"].quantile(0.25)
nonSmokerQ3 = df.loc[df["smoker"]==0]["charges"].quantile(0.75)

smokerQ1 = df.loc[df["smoker"]==0]["charges"].quantile(0.25)
smokerQ3 = df.loc[df["smoker"]==0]["charges"].quantile(0.75)







