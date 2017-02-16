import math

jason = {
        'R': [-7134.398648809276129, -1344.209105925399003 , 2616.198919025931575 ],
        'V': [2.737026697769760242 , -2.641277223887037396, 6.099438445144469672 ],
        'keplerian':{
            'a':7719.637185686771549,
            'e':0.0004933931548963581687,
            'i':1.152688636308465185 ,
            'Ω':3.167019390999958014 ,
            'ω':1.161348667194184864 ,
            'ν':5.501897470565231553 
            },
        'time':1450256432.184
    }
GPSIIR = {
        'R': [-17662.41643,4031.322128,-19465.284702],
        'V': [0.41219989,-3.67984866,-1.12269641],
        'keplerian':{
            'a':26559.45536811388409 ,
            'e':0.0028139222014726429,
            'i':0.9077268890773122381,
            'Ω':5.063017814062672041,
            'ω':0.06663686045640246166,
            'ν':4.266175869989886267
            }
    }

Galileo = {
        'R': [1998.262166,26807.029665,-12370.888483],
        'V': [-2.2176139989,1.36088755712,2.5893515261],
        'keplerian':{
            'a':29601.04674412769265,
            'e':0.0003642504036890733373,
            'i':0.9614657410409044464,
            'Ω':1.823372879929565251,
            'ω':5.29272150055702184,
            'ν':0.4555038029563247135
            }
    }

Intelsat = {
        'R': [40568.021657,-2422.86491,58.47416],
        'V': [0.265204,3.17952,-6.933e-05],
        'keplerian':{
            'a':42241.11780447884709,
            'e':0.04461501670143204985,
            'i':0.001439896472618427217,
            'Ω':4.614079806539448909,
            'ω':1.029490680250953739 ,
            'ν':0.5799621215309532638 
            }
    }

GM = 398600.4415
BASETIME = 946728000.000
EARTHRR = math.pi*2 / 86400 #rotation rate of earth in radians/s
