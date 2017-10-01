# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:15:10 2017

"""
import pandas
import Orange
from orangecontrib.associate.fpgrowth import *
data=Orange.data.Table("C:\Users\siddu\Desktop\Internship\SWaT_Dataset_Normal_v0(AutoRecovered).csv")

new_domain=Orange.data.Domain(list(data.domain.attributes[0:14]), 
             data.domain.attributes[14], 
             metas=data.domain.metas)


data=Orange.data.Table(new_domain,data)
X, mapping=OneHot.encode(data, include_class=True)
itemsets= dict(frequent_itemsets(X,.007))

class_items = {item
for item, var, _ in OneHot.decode(mapping, data, mapping)
if var is data.domain.class_var}
rules = [(P, Q, supp, conf)
for P, Q, supp, conf in association_rules(itemsets, .9)
if len(Q) == 1 and Q & class_items]

target = open("D:\FileData", 'w')
print(len(rules))
target.write(str(len(rules)))
target.write("\n")
names = {item: '{}={}'.format(var.name, val)
for item, var, val in OneHot.decode(mapping, data, mapping)}
for ante, cons, supp, conf in rules[:10000000]:
    print(', '.join(names[i] for i in ante), '-->', names[next(iter(cons))], '(supp: {}, conf: {})'.format(supp, conf))
    target.write(', '.join(names[i] for i in ante))
    #target.write('-->')
    target.write('==')
    target.write(names[next(iter(cons))])
    #target.write('(supp: {}, conf: {})'.format(supp, conf))
    target.write(',supp= {}, ,conf= {}'.format(supp, conf))
    target.write("\n")
target.close()