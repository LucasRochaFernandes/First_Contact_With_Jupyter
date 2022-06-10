import os
from pathlib import Path
import os

def save_table(folder, tag, df):
    myPath = str(Path.cwd())
    myPath = os.path.join(myPath, (folder+'/'))
    df.to_excel(myPath+'planilha_'+tag+'_.xlsx')