import pandas as pd
from tkinter import messagebox, filedialog
import datetime

def main():
    #Prompt user for input
    messagebox.showinfo(None,"Please select an IZ Bib Processing report to process.")
    #Read CEF IZ report (.csv)
    file = filedialog.askopenfilename()
    try:
        df = pd.read_csv(file)
        print(df)
    except:
        print("Error: Please select a .csv report to process.")
        quit()
    
    #Create empty strings to receive outputs
    MMSIds = "MMS Id\n"
    recordstoupdate = "001,035$a\n"

    #Select all records with action type "match" and new OCLC # to load
    for index, row in df.iterrows():
        #For records with existing OCLC #'s
        if row["Action"] == "match":
            if row["Existing 035a"] != row["Incoming 035a"]:
                MMSIds = MMSIds + f'{str(row["Network Id"])}\n'
                recordstoupdate = recordstoupdate + f'{str(row["Network Id"])},{str(row["Incoming 035a"]).rstrip('.0')}\n'
                print(recordstoupdate)
                print("Updated OCLC # found. Writing to outputs.")
        #For new records
        elif row["Action"] == "create":
            if row["Existing 035a"] == "":
                recordstoupdate = recordstoupdate + f'{str(row["Network Id"])},{str(row["Incoming 035a"]).rstrip('.0')}\n'
                print("New record found. Writing to outputs.")
        #All other records
        else:
            print(f'Record {row["Network Id"]} does not match parameters for update. Manual review may be required.')

    #Write outputs to files
    datestamp = datetime.datetime.today().strftime('%m%d%H%M')
    with open(f'IZIDs_{datestamp}.csv', 'w') as fh:
        fh.write(MMSIds)
    with open(f'OCLC_Import_{datestamp}.csv', 'w') as fj:
        fj.write(recordstoupdate)
    print(f'Outputs saved to IZIDs_{datestamp}.csv and OCLC_Import_{datestamp}.csv.')

if __name__ == "__main__":
    main()