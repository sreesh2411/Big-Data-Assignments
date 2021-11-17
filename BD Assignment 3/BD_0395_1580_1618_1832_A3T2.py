from __future__ import print_function
import sys
import pyspark
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    target_word= sys.argv[1]
    num_strokes=sys.argv[2]
    spark = SparkSession\
        .builder\
        .appName("SearchByCountry")\
        .getOrCreate()

data= spark.read.load(sys.argv[3], format="csv", sep=",", inferSchema="true", header="true")
data_1=spark.read.load(sys.argv[4], format="csv", sep=",", inferSchema="true", header="true")
data_part_1=data.repartition(numPartitions=15)
data_part_2=data_1.repartition(numPartitions=15)
final_data=data_part_1.join(data_part_2,['word','key_id'],"inner")
final_data=final_data.orderBy(('countrycode'))


select_data=(final_data.filter((final_data.word==target_word) & (final_data.recognized!="True") & (final_data.Total_Strokes<num_strokes)).groupby("countrycode").count()).collect()

store_dict={}
for record in select_data:
	store_dict[record.countrycode]=record['count']
for record in sorted(store_dict.keys()):
	print("%s,%s"%(record,store_dict[record]))



