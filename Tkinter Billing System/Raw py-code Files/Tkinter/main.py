#extensions import section
from tkinter import *
from tkinter import messagebox
import random,os,tempfile


#Main file  Functions part
  
def total():
# for HOT BEVERAGE price
    global TANDOORI_TEAprice,MASALA_TEAprice,FILTER_COFEEprice,GREEN_TEAprice,LEMON_TEAprice,BLACK_TEAprice,HERBAL_TEAprice,JASMINE_TEAprice

    TANDOORI_TEAprice=int(lablel1Entry.get())*25
    MASALA_TEAprice=int(lablel2Entry.get())*15
    FILTER_COFEEprice=int(lablel3Entry.get())*20
    GREEN_TEAprice=int(lablel4Entry.get())*15
    LEMON_TEAprice=int(lablel5Entry.get())*15
    BLACK_TEAprice=int(lablel6Entry.get())*12
    HERBAL_TEAprice=int(lablel7Entry.get())*15
    JASMINE_TEAprice=int(lablel8Entry.get())*17
    HOT_BEVERAGEprice=TANDOORI_TEAprice+MASALA_TEAprice+FILTER_COFEEprice+ GREEN_TEAprice+LEMON_TEAprice+BLACK_TEAprice+HERBAL_TEAprice+JASMINE_TEAprice
    hotlablelEntry.delete(0,END)
    hotlablelEntry.insert(0,'Rs. '+str(HOT_BEVERAGEprice))
        #for tax section of HOT_BEVERAGE
    BEVERAGEtax = HOT_BEVERAGEprice*0.04
    HOT_BEVERAGEtax=round(BEVERAGEtax,2)
    hot_taxlablelEntry.delete(0,END)
    hot_taxlablelEntry.insert(0,HOT_BEVERAGEtax)
    
    # for FRIENCH FRIES price
    global REG_FRENCH_FRIESprice,PERI_FRENCH_FRIESprice,BBQ_FRENCH_FRIESprice,CHEESY_FRENCH_FRIESprice,BISTO_FRENCH_FRIESprice,BOARDWALK_FRIESprice,COTTAGE_FRIESprice,CRINKLE_FRIESprice
    
    REG_FRENCH_FRIESprice=int(lablel21Entry.get())*50
    PERI_FRENCH_FRIESprice=int(lablel22Entry.get())*60
    BBQ_FRENCH_FRIESprice=int(lablel23Entry.get())*60
    CHEESY_FRENCH_FRIESprice=int(lablel24Entry.get())*75
    BISTO_FRENCH_FRIESprice=int(lablel25Entry.get())*65
    BOARDWALK_FRIESprice=int(lablel26Entry.get())*65 
    COTTAGE_FRIESprice=int(lablel27Entry.get())*70
    CRINKLE_FRIESprice=int(lablel28Entry.get())*40
    FRIENCH_FRIESprice=REG_FRENCH_FRIESprice+PERI_FRENCH_FRIESprice+BBQ_FRENCH_FRIESprice+CHEESY_FRENCH_FRIESprice+BISTO_FRENCH_FRIESprice+BOARDWALK_FRIESprice+COTTAGE_FRIESprice+CRINKLE_FRIESprice
    hotlablel1Entry.delete(0,END)
    hotlablel1Entry.insert(0,f'Rs. {FRIENCH_FRIESprice}')
    #for tax section of FRIENCH FRIES
    FRIESpricetax=FRIENCH_FRIESprice*0.05
    FRIENCH_FRIESpricetax=round(FRIESpricetax,2)
    hot_taxlablel1Entry.delete(0,END)
    hot_taxlablel1Entry.insert(0,FRIENCH_FRIESpricetax)
    
    # for SANDWITCH price
    global VEG_SANDWICHprice,PANEER_SANDWICHprice,CHICKEN_SANDWICHprice,EGG_SANDWICHprice,SEAFOOD_SANDWICHprice,BEEF_SANDWICHprice,MEAT_BALL_SANDWICHprice,PRAWN_SANDWICHprice
    VEG_SANDWICHprice=int(lablel31Entry.get())*50
    PANEER_SANDWICHprice=int(lablel32Entry.get())*65
    CHICKEN_SANDWICHprice=int(lablel33Entry.get())*70
    EGG_SANDWICHprice=int(lablel34Entry.get())*60
    SEAFOOD_SANDWICHprice=int(lablel35Entry.get())*100
    BEEF_SANDWICHprice=int(lablel36Entry.get())*40
    MEAT_BALL_SANDWICHprice=int(lablel37Entry.get())*55
    PRAWN_SANDWICHprice=int(lablel38Entry.get())*150
    SANDWITCHprice=VEG_SANDWICHprice+PANEER_SANDWICHprice+CHICKEN_SANDWICHprice+EGG_SANDWICHprice+SEAFOOD_SANDWICHprice+BEEF_SANDWICHprice+MEAT_BALL_SANDWICHprice+PRAWN_SANDWICHprice
    hotlablel2Entry.delete(0,END)
    hotlablel2Entry.insert(0,f'Rs. {SANDWITCHprice}')

    #for tax section of  SANDWITCH
    SANDWITCH=SANDWITCHprice*0.06
    SANDWITCH_pricetax=round(SANDWITCH,2)
    hot_taxlablel2Entry.delete(0,END)
    hot_taxlablel2Entry.insert(0,SANDWITCH_pricetax)
    
    global total_bill_price
    totalbills= HOT_BEVERAGEprice+FRIENCH_FRIESprice+SANDWITCHprice+HOT_BEVERAGEtax+FRIENCH_FRIESpricetax+SANDWITCH_pricetax  
    total_bill_price=round(totalbills,2)

#Random generation for bill number
billnumber=random.randint(1000,9000)

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'{billnumber} is saved successfully')
        billnumber=random.randint(1000,9000)

#Creating a folder for save bills       
if not os.path.exists('bills') :
    os.mkdir('bills') 

def bill_area():
    from datetime import datetime
    if nameEntry.get()=='' or PhoneEntry.get()=='':
        messagebox.showerror('Error','Customer deatails are requied')
    elif hotlablelEntry.get()=='' and hotlablel1Entry.get()=='' and hotlablel2Entry.get()=='':
        messagebox.showerror('Error','Nothing selected from items')
    elif hotlablelEntry.get()=='Rs. 0' and hotlablel1Entry.get()=='Rs. 0' and hotlablel2Entry.get()=='Rs. 0':
        messagebox.showerror('Error','Nothing selected from items')
    else:
        now1=datetime.now()
        date1=now1.strftime("%d/%m/%Y - %H:%M")
        textarea.delete(1.0,END)
        textarea.insert(END,'\t***INDIRA Cofee Shop***')
        textarea.insert(END,'\n=======================================')
        textarea.insert(END,f'\nDate: {date1}')
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nCustomer Ph.no: {PhoneEntry.get()}')
        textarea.insert(END,'\n=======================================')
        textarea.insert(END,'\nProduct\t\tQty\t\tprice')                         
        textarea.insert(END,'\n=======================================')
        #section 1 products
        if lablel1Entry.get()!='0':
            textarea.insert(END,f'\nTANDOORI TEA\t\t{lablel1Entry.get()}\t\t{TANDOORI_TEAprice}')
        if lablel2Entry.get()!='0':
            textarea.insert(END,f'\nMASALA TEA\t\t{lablel2Entry.get()}\t\t{MASALA_TEAprice}')
        if lablel3Entry.get()!='0':
            textarea.insert(END,f'\nFILTER COFEE\t\t{lablel3Entry.get()}\t\t{FILTER_COFEEprice}')
        if lablel4Entry.get()!='0':
            textarea.insert(END,f'\nGREEN TEA\t\t{lablel4Entry.get()}\t\t{GREEN_TEAprice}')
        if lablel5Entry.get()!='0':
            textarea.insert(END,f'\nLEMON TEA\t\t{lablel5Entry.get()}\t\t{LEMON_TEAprice}')
        if lablel6Entry.get()!='0':
            textarea.insert(END,f'\nBLACK TEA\t\t{lablel6Entry.get()}\t\t{BLACK_TEAprice}')
        if lablel7Entry.get()!='0':
            textarea.insert(END,f'\nHERBAL TEA\t\t{lablel7Entry.get()}\t\t{HERBAL_TEAprice}')
        if lablel8Entry.get()!='0':
            textarea.insert(END,f'\nJASMINE TEA\t\t{lablel8Entry.get()}\t\t{JASMINE_TEAprice}')
        #section 2 products
        if lablel21Entry.get()!='0':
            textarea.insert(END,f'\nREG FRIES\t\t{lablel21Entry.get()}\t\t{REG_FRENCH_FRIESprice}')
        if lablel22Entry.get()!='0':
            textarea.insert(END,f'\nPERI FRIES\t\t{lablel22Entry.get()}\t\t{PERI_FRENCH_FRIESprice}')
        if lablel23Entry.get()!='0':
            textarea.insert(END,f'\nBBQ FRIES\t\t{lablel23Entry.get()}\t\t{BBQ_FRENCH_FRIESprice}')
        if lablel24Entry.get()!='0':
            textarea.insert(END,f'\nCHEESY FRIES\t\t{lablel24Entry.get()}\t\t{CHEESY_FRENCH_FRIESprice}')
        if lablel25Entry.get()!='0':
            textarea.insert(END,f'\nBISTO FRIES\t\t{lablel25Entry.get()}\t\t{BISTO_FRENCH_FRIESprice}')
        if lablel26Entry.get()!='0':
            textarea.insert(END,f'\nBOARDWALK FRIES\t{lablel26Entry.get()}\t\t\t{BOARDWALK_FRIESprice}')
        if lablel27Entry.get()!='0':
            textarea.insert(END,f'\nCOTTAGE FRIES\t\t{lablel27Entry.get()}\t\t{COTTAGE_FRIESprice}')
        if lablel28Entry.get()!='0':
            textarea.insert(END,f'\nCRINKLE FRIES\t\t{lablel28Entry.get()}\t\t{CRINKLE_FRIESprice}')
            
        #section 3 products
        if lablel31Entry.get()!='0':
            textarea.insert(END,f'\nVEG SANDWICH\t\t{lablel31Entry.get()}\t\t{VEG_SANDWICHprice}')
        if lablel32Entry.get()!='0':
            textarea.insert(END,f'\nPANEER SANDWICH\t{lablel32Entry.get()}\t\t\t{PANEER_SANDWICHprice}')
        if lablel33Entry.get()!='0':
            textarea.insert(END,f'\nCHICKEN SANDWICH{lablel33Entry.get()}\t\t\t\t{CHICKEN_SANDWICHprice}')
        if lablel34Entry.get()!='0':
            textarea.insert(END,f'\nEGG SANDWICH\t\t{lablel34Entry.get()}\t\t{EGG_SANDWICHprice}')
        if lablel35Entry.get()!='0':
            textarea.insert(END,f'\nSEAFOOD SANDWICH{lablel35Entry.get()}\t\t\t\t{SEAFOOD_SANDWICHprice}')
        if lablel36Entry.get()!='0':
            textarea.insert(END,f'\nBEEF SANDWICH\t\t{lablel36Entry.get()}\t\t{BEEF_SANDWICHprice}')
        if lablel37Entry.get()!='0':
            textarea.insert(END,f'\nMEAT SANDWICH\t\t{lablel37Entry.get()}\t\t{MEAT_BALL_SANDWICHprice}')
        if lablel38Entry.get()!='0':
            textarea.insert(END,f'\nPRAWN SANDWICH\t\t{lablel38Entry.get()}\t\t{PRAWN_SANDWICHprice}')
        textarea.insert(END,'\n=======================================')
        # tax section 
        if hot_taxlablelEntry.get()!='0.0':
            textarea.insert(END,f'\nHOT BEVERAGE tax\t\t\t\t{hot_taxlablelEntry.get()}')
        if hot_taxlablel1Entry.get()!='0.0':
            textarea.insert(END,f'\nFRIENCH FRIES tax\t\t\t\t{hot_taxlablel1Entry.get()}')
        if hot_taxlablel2Entry.get()!='0.0':
            textarea.insert(END,f'\nSANDWITCH tax\t\t\t\t{hot_taxlablel2Entry.get()}')
        textarea.insert(END,'\n=======================================')
        textarea.insert(END,f'\nTotal bill\t\t\t\t{total_bill_price}')
        #bill saving message box section
        save_bill()


def search_bill():
    file_path=r"./bills" 
    bill_number= billEntry.get()
    file_path=os.path.join(file_path,f"{bill_number}.txt")
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            bill_contents = file.read()
            textarea.delete('1.0','end')
            textarea.insert('1.0',bill_contents)
    else:
        messagebox.showerror('Error','Invalid bill number')  


def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def clear():
    lablel1Entry.delete(0,END)
    lablel2Entry.delete(0,END)
    lablel3Entry.delete(0,END)
    lablel4Entry.delete(0,END)
    lablel5Entry.delete(0,END)
    lablel6Entry.delete(0,END)
    lablel7Entry.delete(0,END)
    lablel8Entry.delete(0,END)

    lablel1Entry.insert(0,0)
    lablel2Entry.insert(0,0)
    lablel3Entry.insert(0,0)
    lablel4Entry.insert(0,0)
    lablel5Entry.insert(0,0)
    lablel6Entry.insert(0,0)
    lablel7Entry.insert(0,0)
    lablel8Entry.insert(0,0)

    lablel21Entry.delete(0,END)
    lablel22Entry.delete(0,END)
    lablel23Entry.delete(0,END)
    lablel24Entry.delete(0,END)
    lablel25Entry.delete(0,END)
    lablel26Entry.delete(0,END)
    lablel27Entry.delete(0,END)
    lablel28Entry.delete(0,END)

    lablel21Entry.insert(0,0)
    lablel22Entry.insert(0,0)
    lablel23Entry.insert(0,0)
    lablel24Entry.insert(0,0)
    lablel25Entry.insert(0,0)
    lablel26Entry.insert(0,0)
    lablel27Entry.insert(0,0)
    lablel28Entry.insert(0,0)

    lablel31Entry.delete(0,END)
    lablel32Entry.delete(0,END)
    lablel33Entry.delete(0,END)
    lablel34Entry.delete(0,END)
    lablel35Entry.delete(0,END)
    lablel36Entry.delete(0,END)
    lablel37Entry.delete(0,END)
    lablel38Entry.delete(0,END)


    lablel31Entry.insert(0,0)
    lablel32Entry.insert(0,0)
    lablel33Entry.insert(0,0)
    lablel34Entry.insert(0,0)
    lablel35Entry.insert(0,0)
    lablel36Entry.insert(0,0)
    lablel37Entry.insert(0,0)
    lablel38Entry.insert(0,0)

    hotlablelEntry.delete(0,END)
    hotlablel1Entry.delete(0,END)
    hotlablel2Entry.delete(0,END)

    hot_taxlablelEntry.delete(0,END)
    hot_taxlablel1Entry.delete(0,END)
    hot_taxlablel2Entry.delete(0,END)

    nameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    billEntry.delete(0,END)

    textarea.delete(0.1,END)            

    #GUI part

root=Tk()
root.title("Billing System")
root.iconbitmap('C:\\Python\\Project\\Tkinter\\icon1.ico')
# icon=PhotoImage(file="C:\Python\Project\Tkinter\icons2.png")
# root.iconphoto(True,icon)

#Open window on fixed position and fixed size

root.geometry("1300x685")
root.resizable(False,False)

#wiget area start:

headingLable=Label(root,text='INDIRA COFEE SHOP',font=('helvetica',30,'bold'),bg='gold',fg='brown',bd=12,relief=RIDGE)
headingLable.pack(fill=X)
#Customer Details section
Custumer_frame=LabelFrame(root,text='Customer Details',font=('helvetica',15,'bold'),bg='gray20',fg='red',bd=8,relief=GROOVE)
Custumer_frame.pack(fill=X)#direction of lable to fill background

namelable=Label(Custumer_frame,text='Name',font=('helvetica',15,'bold'),bg='gray20',fg='wheat')
namelable.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(Custumer_frame,font=('arial',15),bd=5,width=15)
nameEntry.grid(row=0,column=1,padx=20)
#for phone number
Phonelable=Label(Custumer_frame,text='Number',font=('helvetica',15,'bold'),bg='gray20',fg='wheat')
Phonelable.grid(row=0,column=2,padx=20)

PhoneEntry=Entry(Custumer_frame,font=('arial',15),bd=5,width=15)
PhoneEntry.grid(row=0,column=3,padx=20)
#for Bill number
billlable=Label(Custumer_frame,text='Bill Number',font=('helvetica',15,'bold'),bg='gray20',fg='wheat')
billlable.grid(row=0,column=4,padx=20)

billEntry=Entry(Custumer_frame,font=('arial',15),bd=5,width=15)
billEntry.grid(row=0,column=5,padx=6)
#search button
searchbutton=Button(Custumer_frame,text='SEARCH',font=('helvetica',10,'bold'),bd=5,width=12,command=search_bill)
searchbutton.grid(row=0,column=6,padx=20,pady=5)


#for Items section
menuframe=Frame(root,bg='gray20',bd=4,relief=GROOVE)
menuframe.pack(fill=X)

Itemsframe=LabelFrame(menuframe,text='HOT BEVERAGES',font=('helvetica',13,'bold'),bg='gray20',fg='red',bd=4,relief=GROOVE)
Itemsframe.grid(row=0,column=0,padx=0,pady=2)

lablel1=Label(Itemsframe,text='TANDOORI TEA',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel1.grid(row=0,column=0,padx=20,pady=3,sticky=W)

lablel1Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel1Entry.grid(row=0,column=1,padx=16,pady=3)
lablel1Entry.insert(0,0)

lablel2=Label(Itemsframe,text='MASALA TEA',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel2.grid(row=1,column=0,padx=20,pady=3,sticky=W)

lablel2Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel2Entry.grid(row=1,column=1,padx=20,pady=3)
lablel2Entry.insert(0,0)

lablel3=Label(Itemsframe,text='FILTER COFEE',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel3.grid(row=2,column=0,padx=20,pady=3,sticky=W)

lablel3Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel3Entry.grid(row=2,column=1,padx=20,pady=3)
lablel3Entry.insert(0,0)

lablel4=Label(Itemsframe,text='GREEN TEA',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel4.grid(row=3,column=0,padx=20,pady=3,sticky=W)

lablel4Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel4Entry.grid(row=3,column=1,padx=20,pady=3)
lablel4Entry.insert(0,0)

lablel5=Label(Itemsframe,text='LEMON TEA',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel5.grid(row=4,column=0,padx=20,pady=3,sticky=W)

lablel5Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel5Entry.grid(row=4,column=1,padx=20,pady=3)
lablel5Entry.insert(0,0)

lablel6=Label(Itemsframe,text='BLACK TEA',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel6.grid(row=5,column=0,padx=20,pady=3,sticky=W)

lablel6Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel6Entry.grid(row=5,column=1,padx=20,pady=3)
lablel6Entry.insert(0,0)

lablel7=Label(Itemsframe,text='HERBAL TEA',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel7.grid(row=6,column=0,padx=20,pady=3,sticky=W)

lablel7Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel7Entry.grid(row=6,column=1,padx=20,pady=3)
lablel7Entry.insert(0,0)

lablel8=Label(Itemsframe,text='JASMINE TEA',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel8.grid(row=7,column=0,padx=20,pady=3,sticky=W)

lablel8Entry=Entry(Itemsframe,font=('arial',15),bd=5,width=8)
lablel8Entry.grid(row=7,column=1,padx=20,pady=3)
lablel8Entry.insert(0,0)


#2ND items sections
Items2frame=LabelFrame(menuframe,text='FRENCH FRIES',font=('helvetica',13,'bold'),bg='gray20',fg='red',bd=5,relief=GROOVE)
Items2frame.grid(row=0,column=1,padx=0,pady=2)

lablel21=Label(Items2frame,text='REG FRENCH FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel21.grid(row=0,column=0,padx=15,pady=3,sticky=W)

lablel21Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel21Entry.grid(row=0,column=1,padx=15,pady=3)
lablel21Entry.insert(0,0)

lablel22=Label(Items2frame,text='PERI FRENCH FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel22.grid(row=2,column=0,padx=15,pady=3,sticky=W)

lablel22Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel22Entry.grid(row=2,column=1,padx=15,pady=3)
lablel22Entry.insert(0,0)

lablel23=Label(Items2frame,text='BBQ FRENCH FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel23.grid(row=3,column=0,padx=15,pady=3,sticky=W)

lablel23Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel23Entry.grid(row=3,column=1,padx=15,pady=3)
lablel23Entry.insert(0,0)

lablel24=Label(Items2frame,text='CHEESY FRENCH FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel24.grid(row=4,column=0,padx=15,pady=3,sticky=W)

lablel24Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel24Entry.grid(row=4,column=1,padx=15,pady=3)
lablel24Entry.insert(0,0)

lablel25=Label(Items2frame,text='BISTO FRENCH FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel25.grid(row=5,column=0,padx=15,pady=3,sticky=W)

lablel25Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel25Entry.grid(row=5,column=1,padx=15,pady=3)
lablel25Entry.insert(0,0)

lablel26=Label(Items2frame,text=' BOARDWALK FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel26.grid(row=6,column=0,padx=15,pady=3,sticky=W)

lablel26Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel26Entry.grid(row=6,column=1,padx=15,pady=3)
lablel26Entry.insert(0,0)

lablel27=Label(Items2frame,text=' COTTAGE FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel27.grid(row=7,column=0,padx=15,pady=3,sticky=W)

lablel27Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel27Entry.grid(row=7,column=1,padx=15,pady=3)
lablel27Entry.insert(0,0)

lablel28=Label(Items2frame,text=' CRINKLE FRIES',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel28.grid(row=8,column=0,padx=15,pady=3,sticky=W)

lablel28Entry=Entry(Items2frame,font=('arial',15),bd=5,width=8)
lablel28Entry.grid(row=8,column=1,padx=15,pady=3)
lablel28Entry.insert(0,0)


#3rd items
Items3frame=LabelFrame(menuframe,text='SANDWICHES',font=('helvetica',13,'bold'),bg='gray20',fg='red',bd=5,relief=GROOVE)
Items3frame.grid(row=0,column=2,padx=0,pady=2)

lablel31=Label(Items3frame,text='VEG SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel31.grid(row=0,column=0,padx=16,pady=3,sticky=W)

lablel31Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel31Entry.grid(row=0,column=1,padx=16,pady=3)
lablel31Entry.insert(0,0)

lablel32=Label(Items3frame,text='PANEER SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel32.grid(row=2,column=0,padx=16,pady=3,sticky=W)

lablel32Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel32Entry.grid(row=2,column=1,padx=16,pady=3)
lablel32Entry.insert(0,0)

lablel33=Label(Items3frame,text='CHICKEN SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel33.grid(row=3,column=0,padx=16,pady=3,sticky=W)

lablel33Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel33Entry.grid(row=3,column=1,padx=16,pady=3)
lablel33Entry.insert(0,0)

lablel34=Label(Items3frame,text='EGG SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel34.grid(row=4,column=0,padx=16,pady=3,sticky=W)

lablel34Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel34Entry.grid(row=4,column=1,padx=16,pady=3)
lablel34Entry.insert(0,0)

lablel35=Label(Items3frame,text='SEAFOOD SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel35.grid(row=5,column=0,padx=16,pady=3,sticky=W)

lablel35Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel35Entry.grid(row=5,column=1,padx=16,pady=3)
lablel35Entry.insert(0,0)

lablel36=Label(Items3frame,text='BEEF SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel36.grid(row=6,column=0,padx=16,pady=3,sticky=W)

lablel36Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel36Entry.grid(row=6,column=1,padx=16,pady=3)
lablel36Entry.insert(0,0)

lablel37=Label(Items3frame,text='MEAT BALL SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel37.grid(row=7,column=0,padx=16,pady=3,sticky=W)

lablel37Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel37Entry.grid(row=7,column=1,padx=16,pady=3)
lablel37Entry.insert(0,0)

lablel38=Label(Items3frame,text='PRAWN SANDWICH',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
lablel38.grid(row=8,column=0,padx=16,pady=3,sticky=W)

lablel38Entry=Entry(Items3frame,font=('arial',15),bd=5,width=8)
lablel38Entry.grid(row=8,column=1,padx=16,pady=3)
lablel38Entry.insert(0,0)


#BILLING AREA
billframe=Frame(menuframe,bd=4,relief=GROOVE)
billframe.grid(row=0,column=3,padx=2,pady=2)

billframelable=Label(billframe,text='BILL SCREEN',font=('helvetica',13,'bold'),bd=5,fg='red',bg='gray20',relief=GROOVE)
billframelable.pack(fill=X)


Scrollbar=Scrollbar(billframe,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)


textarea=Text(billframe,height=19,width=40,yscrollcommand=Scrollbar.set)
textarea.pack(fill=X)
Scrollbar.config(command=textarea.yview)


#for BILL MENU
billingmenuframe=Frame(root,bg='gray20',bd=4,relief=GROOVE)
billingmenuframe.pack(fill=X)

fItemsframe=LabelFrame(billingmenuframe,text='BILL MENU',font=('helvetica',13,'bold'),bg='gray20',fg='red',bd=5,relief=GROOVE)
fItemsframe.grid(row=0,column=0,padx=10)

hotlablel=Label(fItemsframe,text='HOT BEVERAGES PRICE',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
hotlablel.grid(row=0,column=0,padx=10,pady=3,sticky=W)

hotlablelEntry=Entry(fItemsframe,font=('arial',15),bd=5,width=8)
hotlablelEntry.grid(row=0,column=1,padx=10,pady=3)

hotlablel1=Label(fItemsframe,text='FRENCH FRIES PRICE',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
hotlablel1.grid(row=1,column=0,padx=10,pady=3,sticky=W)

hotlablel1Entry=Entry(fItemsframe,font=('arial',15),bd=5,width=8)
hotlablel1Entry.grid(row=1,column=1,padx=10,pady=3)

hotlablel2=Label(fItemsframe,text='SANDWICHES PRICE',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
hotlablel2.grid(row=2,column=0,padx=10,pady=3,sticky=W)

hotlablel2Entry=Entry(fItemsframe,font=('arial',15),bd=5,width=8)
hotlablel2Entry.grid(row=2,column=1,padx=10,pady=3)


# BILL TAX SECTION
hot_taxlablel=Label(fItemsframe,text='HOT BEVERAGES TAX',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
hot_taxlablel.grid(row=0,column=2,padx=10,pady=3,sticky=W)

hot_taxlablelEntry=Entry(fItemsframe,font=('arial',15),bd=5,width=8)
hot_taxlablelEntry.grid(row=0,column=3,padx=10,pady=3)

hot_taxlablel1=Label(fItemsframe,text='FRENCH FRIES TAX',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
hot_taxlablel1.grid(row=1,column=2,padx=10,pady=3,sticky=W)

hot_taxlablel1Entry=Entry(fItemsframe,font=('arial',15),bd=5,width=8)
hot_taxlablel1Entry.grid(row=1,column=3,padx=10,pady=3)

hot_taxlablel2=Label(fItemsframe,text='SANDWICHES TAX',font=('helvetica',10,'bold'),bg='gray20',fg='sandy brown')
hot_taxlablel2.grid(row=2,column=2,padx=10,pady=3,sticky=W)

hot_taxlablel2Entry=Entry(fItemsframe,font=('arial',15),bd=5,width=8)
hot_taxlablel2Entry.grid(row=2,column=3,padx=10,pady=3)


#for final calculations button
buttonframe=Frame(billingmenuframe,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,padx=3)

totalbutton=Button(buttonframe,text='Total',font=('helvetica',15,'bold'),bg='gray20',fg='sandy brown',bd=5,width=8,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=25)


billbutton=Button(buttonframe,text='Bill',font=('helvetica',15,'bold'),bg='gray20',fg='sandy brown',bd=5,width=8,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=25)

printbutton=Button(buttonframe,text='Print',font=('helvetica',15,'bold'),bg='gray20',fg='sandy brown',bd=5,width=8,command=print_bill)
printbutton.grid(row=0,column=2,pady=20,padx=25)

clearbutton=Button(buttonframe,text='Clear',font=('helvetica',15,'bold'),bg='gray20',fg='sandy brown',bd=5,width=8,command=clear)
clearbutton.grid(row=0,column=3,pady=20,padx=25)


root.mainloop()# help to view our window


