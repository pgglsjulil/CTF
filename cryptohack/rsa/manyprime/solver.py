#!/usr/bin/env python3

from Crypto.Util.number import *
n = 580642391898843192929563856870897799650883152718761762932292482252152591279871421569162037190419036435041797739880389529593674485555792234900969402019055601781662044515999210032698275981631376651117318677368742867687180140048715627160641771118040372573575479330830092989800730105573700557717146251860588802509310534792310748898504394966263819959963273509119791037525504422606634640173277598774814099540555569257179715908642917355365791447508751401889724095964924513196281345665480688029639999472649549163147599540142367575413885729653166517595719991872223011969856259344396899748662101941230745601719730556631637
e = 65537
# ct = 320721490534624434149993723527322977960556510750628354856260732098109692581338409999983376131354918370047625150454728718467998870322344980985635149656977787964380651868131740312053755501594999166365821315043312308622388016666802478485476059625888033017198083472976011719998333985531756978678758897472845358167730221506573817798467100023754709109274265835201757369829744113233607359526441007577850111228850004361838028842815813724076511058179239339760639518034583306154826603816927757236549096339501503316601078891287408682099750164720032975016814187899399273719181407940397071512493967454225665490162619270814464
ct = 49085379776944113897124026303282099218200554421730609642162526781420905597881193129053606805476191564273546573633711358811070231391388600055525561327993848989655939788475216276640357365357159283601343526854549848803759724091475562722860919923558299395288708459654473827887904861900038738052839648861222745411166
n = 68936702896215919913611570954986340465700435643707363044019868126549297259672266569828292588281465957589195152718096207629516756106645654646394195856526059138847116857222395108330112421874901743242089831481566183656536715601846591577399237595071803229513484232116474751291862438874099999049917890490269122596339
# factor_n = "9282105380008121879 9303850685953812323 9389357739583927789 10336650220878499841 10638241655447339831 11282698189561966721 11328768673634243077 11403460639036243901 11473665579512371723 11492065299277279799 11530534813954192171 11665347949879312361 12132158321859677597 12834461276877415051 12955403765595949597 12973972336777979701 13099895578757581201 13572286589428162097 14100640260554622013 14178869592193599187 14278240802299816541 14523070016044624039 14963354250199553339 15364597561881860737 15669758663523555763 15824122791679574573 15998365463074268941 16656402470578844539 16898740504023346457 17138336856793050757 17174065872156629921 17281246625998849649"
factor_n = "16603 17021 17117 17189 17981 18341 18427 18701 19183 19259 19441 19471 19597 19727 19813 19973 20393 20399 20663 20663 20747 21149 21163 21221 21961 22093 22259 22717 22943 23143 23203 23333 23539 23593 23767 23831 24077 24247 24281 24847 24917 25169 25357 25439 25523 25537 25657 25931 26357 26417 26557 26863 27077 27337 27967 28229 28517 29027 29077 29131 31013 31193 31337 31477 31973 32083 32191 32377 32401 32441 32569"
factor_n = list(map(int, factor_n.split()))

totient = 1
for prime in factor_n:
	totient = totient * (prime - 1)
# print(totient)
d = pow(e, -1, totient)
pt = pow(ct, d, n)
m = long_to_bytes(pt)
print(m)