import csv,unittest,ranking
from lab8.sortandcount import *
from lab8.merge_sort import *

#[bonus] unittest!
class Mytest(unittest.TestCase):
    def runTest(self):
        inversion = SortAndCount([2,1,2,3,4,5,6,1,6,13,17])
        self.assertEqual(inversion.getInversionnum(),7)
        inversion = SortAndCount([5,4,3,2,1,0])
        self.assertEqual(inversion.getInversionnum(),15)
        data = list()
        useridls = list()
        inversionls = list()
        with open("msd_1m.txt") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                useridls.append(list(row.values())[0])
                indata =  [int(x) for x in list(row.values())[1:10]]
                sorteddata = indata.copy()
                sorteddata.sort(reverse=True)
                rank = self.trans2rank(sorteddata)
                data.append([rank.rank(x) for x in indata])
                #  print([rank.rank(x) for x in indata])
        for row in data:
            inversionls.append(SortAndCount(row).getInversionnum())
        relationtable = zip(useridls,data,inversionls)
        relationtable = list(relationtable)
        relationtable.sort(key=lambda tup: tup[2])
        rank_result = list(zip(*relationtable))
        #[bonus] write out result
        with open('SimilarityMetric.txt', 'w') as resultfile:
            for item in relationtable:
                resultfile.write("%s,%s\n" % (item[0],item[2]))

    def trans2rank(self,ls):
        return ranking.Ranking(ls)


if __name__ == '__main__':
    unittest.main()

        

