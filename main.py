import zipfile
import pandas as pd

#An empty list to append the dfs created by every csv
virtual_csvs = []
def engg_test():
    #Initially listing the files in the zip archieve
    with zipfile.ZipFile("C:\\Users\\prana\\Downloads\\Engineering Test Risk Analytics .zip", "r") as f:
        for name in f.namelist():
            #Traversing to files in the requisite folder
            if name.startswith("Engineering Test Risk Analytics /Engineering Test Files"):
                #Excluding other file formats except csv
                if name.endswith(".csv"):
                    #Looping for all files, except Combined file
                    if (name.split('/')[-1].split('.')[-2]) != 'Combined':
                        data = f.open(name)
                        #Reading csv to Pandas df
                        df = pd.read_csv(data, index_col=False)
                        #Adding a new required column 'Environment' based on file name
                        df['Environment'] = name.split('/')[-1].split('.')[-2]
                        #Appending all dfs
                        virtual_csvs.append(df)

    combine_df = pd.concat(virtual_csvs)
    #Transforming data as per requirements
    combine_df = combine_df.filter(['Source IP','Environment'])
    combine_df.sort_values("Source IP", inplace = True)
    combine_df.drop_duplicates(subset ="Source IP",keep ='first', inplace = True)

    #Creating the resultant Combined file
    combine_df.to_csv('C:\\Users\\prana\\Downloads\\Combined.csv',index= False)

if __name__ == '__main__':
    engg_test()


