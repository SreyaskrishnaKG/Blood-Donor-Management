import streamlit as st
from  DonorView import BloodDonorManager

donorobj=BloodDonorManager()
tab1,tab2,tab3,car4=st.tabs(["Add donor","View donors","update donors","delete donors"])
with tab1:
    st.header("ADD NEW DONORS....")
    name=st.text_input("Enter donor name ::")
    phone=st.text_input("Enter the donor phone number ::")
    blood_group=st.selectbox("Select blood group ",["A+","A-","B+","B-","AB+","AB+"])
    city=st.text_input("Enter the donor city ::")
    last_dona=st.date_input("Enter the donation date ::")
    if st.button("SUBMIT"):
        donorobj.post(name=name,blood_group=blood_group,phone=phone,
                      city=city,last_donation=last_dona)
        st.success("Donor added successfully.............")
        
with tab2:
    st.header("VIEW DONOR DETAILS................")

    data = donorobj.get()

    st.table(data)
    

with tab3:
    st.header("Update donor details")
    data =donorobj.get()
    blood_groups = ["A", "A-", "B+", "B-", "AB+", "AB-"]
    if data:
        donor_ids=[r[0] for r in data]
        IDs=st.selectbox("select donor ID ",donor_ids,key="update_id")
        data=donorobj.get_object(ID=IDs)
        print(data)
        name=st.text_input("enter your name",value=data[1])
        phone=st.text_input("enter the donor phone number ",data[3])
        blood_groups=st.selectbox("select your blood groups ",blood_groups,
                                 index=blood_groups.index(data[2]),
                                 key="update_blood_group")
        
        CITY=st.text_input("enter donor city ",value=data[4])
        last_donation=st.date_input("last donation date :",value=data[5])
        
        if st.button("update"):
            print(donorobj.put(id=IDs,
                                         name=name,
                                         phone=phone,
                                         blood_group=blood_groups,
                                         city=CITY,
                                         last_dona=last_donation))
            status,message =donorobj.put(id=IDs,
                                         name=name,
                                         phone=phone,
                                         blood_group=blood_groups,
                                         city=CITY,
                                         last_dona=last_donation)
            if status:
                st.success(message)
                st.rerun()
            else:
                st.error(message)
        else:
            print("donor not found...................")
        
                    
            
        
        
        
    
