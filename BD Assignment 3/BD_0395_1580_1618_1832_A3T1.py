from __future__ import print_function
import sys
import pyspark
from operator import add
from pyspark.sql import SparkSession
import pyspark.sql.functions as F     

if __name__ == "__main__":
    target_word= sys.argv[1]
    spark = SparkSession\
        .builder\
        .appName("SearchByCountry")\
        .getOrCreate()

data= spark.read.load(sys.argv[2], format="csv", sep=",", inferSchema="true", header="true")
data_1=spark.read.load(sys.argv[3], format="csv", sep=",", inferSchema="true", header="true")

store_dict={}
net_list=[]

def sum_col(df, col):
    return df.select(F.sum(col)).collect()[0][0]

select_data_1=(data_1.filter((data_1.word==target_word) & (data_1.recognized=="True")))
select_data_2=(data_1.filter((data_1.word==target_word) & (data_1.recognized=="False")))
select_data=(data_1.filter((data_1.word==target_word)).groupby("recognized").count()).collect()
for record in select_data:
	store_dict[record.recognized]=record['count']
for record in sorted(store_dict.keys()):
	net_list.append(float(store_dict[record]))

total_strokes_recog=float(net_list[1])
total_strokes_unrecog=float(net_list[0])


net_sum_recog=sum_col(select_data_1,'Total_Strokes')
net_sum_unrecog=sum_col(select_data_2,'Total_Strokes')

avg_recog=net_sum_recog/total_strokes_recog
avg_unrecog=net_sum_unrecog/total_strokes_unrecog
print("%1.5f" % (round(avg_recog,5)))
print("%1.5f" % (round(avg_unrecog,5)))






