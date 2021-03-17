import os
import argparse
import random
import datetime
import re
FILE_TO_CHANGE = os.path.join(os.getcwd(),'useless.txt')

def make_commit(date):
    d,m,y = date.split('/')
    dt = datetime.datetime(int(y),int(m),int(d))
    datestr = dt.strftime('%a %d %b %Y 14:02:03 GMT+0700')
    os.system('echo "{mess}" >> {file}'.format(mess='stupid ' + str(random.randint(0,1e6)),file=FILE_TO_CHANGE))
    os.system('git add {}'.format(FILE_TO_CHANGE))
    os.system('git commit -m "{}"'.format('stupid commit'))
    os.system('GIT_COMMITTER_DATE="{}" git commit --amend --no-edit --date "{}"'.format(datestr,datestr))

def make_year_commit(year):
    monthDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                 11: 30, 12: 31}
    for month in monthDict.keys():
        for day in range(1,monthDict[month]+1):
            date = '{}/{}/{}'.format(day,month,year)
            make_commit(date)
    os.system('git push --set-upstream origin master --force')


def file_commits(filepath):
    with open(os.path.join(os.getcwd(),filepath),'r') as fs:
        lines = fs.readlines()
        regex = '^[\d]{2}\/[\d]{2}\/[\d]{4}[\s][\d]{1,3}$'
        for line in lines:
            if re.match(regex,line.strip()):
                date,times = line.strip().split(' ')
                times = int(times)
                for i in range(times):
                    make_commit(date)

    os.system('git push --set-upstream origin master --force')

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fp','--filepath',help="Select file with dates",default=None)
    parser.add_argument('-d','--date',default=None,help='Specify date in dd/mm/yyyy format')
    parser.add_argument('-a','--all',help='Specify the year you wanna commit every single day!',type=int)
    parser.add_argument('-t','--time',default=0,help='The number of commits')
    args = parser.parse_args()
    return vars(args)

def main(args):
    if args['filepath'] is not None:
        # file_commits(args['filepath'])
        make_year_commit(2018)

if __name__ == '__main__':
    args = parser()
    main(args)
