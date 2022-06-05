# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:59:27 2022

@author: pranav
"""

data={
    "transactionId":"cc04a8c0-dd8c-40e3-94b8-f63c435554460",
    "clientName":"cvs-rxregaudit",
    "totalPages":1,
    "sourceModelName":"cvs-rxregaudit_compose_model",
    "composeModelName":"cvs-rxregaudit_compose_model_04082022_FR3_1",
    "composeModelId":"8ea6f064-b709-11ec-a920-005056aa00ce",
    "document":None,
    "pages":[
        {
            "pageNumber":1,
            "statusCode":200,
            "status":"succeeded",
            "error":None,
            "sourceModelName":"cvs-rxregaudit_controlled_sub_inventory_oklahoma",
            "modelName":"cvs-rxregaudit_ControlledSubInventory",
            "model_Id":"27b8a658-b709-11ec-ae47-005056aa00ce",
            "modelConfidence":0.877,
            "keyValuePairs":[
            [
                [
					{
						"key":"pharmacy_address_line1",
                        "value":"1601 Northwestern Ave",
                        "confidence":0.99,
						"positionConfidence":0.99,
                        "ocrConfidence":[
                        0.966,
						0.736,
						0.782
                        ],
						"boundingBox":[
                        307,670,1125,670,1125,742,307,742
                        ],
                        "source":"form recognizer"
					},
				]
			],
			[
				[
					{
						"key":"chk_reasonforinventory_annualinventory",
                        "value":"unselected",
                        "confidence":0.994,
						"positionConfidence":0.99,
                        "ocrConfidence":[
                        1
                        ],
						"boundingBox":[
                        450,1379,511,1379,511,1438,450,1438
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"chk_reasonforinventory_pharmacyclosing",
                        "value":"unselected",
                        "confidence":0.995,
						"positionConfidence":0.995,
                        "ocrConfidence":[
                        1
                        ],
						"boundingBox":[
                        1511,1295,1572,1295,1572,1355,1511,1355
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"chk_time_inventory_conducted_close",
                        "value":"selected",
                        "confidence":0.994,
						"positionConfidence":0.994,
                        "ocrConfidence":[
                        1
                        ],
						"boundingBox":[
                        222,1087,284,1087,284,1146,222,1146
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"pharmacy_address_cityzipcode",
                        "value":"Taylor, ok , 12331",
                        "confidence":0.527,
						"positionConfidence":0.527,
                        "ocrConfidence":[
                        0.992,0.955,0.846
                        ],
						"boundingBox":[
                        469,750,1097,750,1097,814,469,814
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"chk_time_inventory_conducted_24-hour",
                        "value":"unselected",
                        "confidence":0.995,
						"positionConfidence":0.995,
                        "ocrConfidence":[
                         1
                        ],
						"boundingBox":[
                        1078,1088,1140,1088,1140,1148,1078,1148
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"chk_reasonforinventory_ownershipchange",
                        "value":"selected",
                        "confidence":0.995,
						"positionConfidence":0.995,
                        "ocrConfidence":[
                         1
                        ],
						"boundingBox":[
                        983,1298,1045,1298,1045,1355,983,1355
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"chk_reasonforinventory_changeofpic",
                        "value":"selected",
                        "confidence":0.995,
						"positionConfidence":0.995,
                        "ocrConfidence":[
                         1
                        ],
						"boundingBox":[
                        157,1295,220,1295,220,1355,157,1355
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"pharmacy_no",
                        "value":"62345",
                        "confidence":0.992,
						"positionConfidence":0.992,
                        "ocrConfidence":[
                         0.859
                        ],
						"boundingBox":[
                        1658,7461877,746,1877,808,1658,808
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"pharmacy_store_no",
                        "value":"CVS 62345",
                        "confidence":0.99,
						"positionConfidence":0.99,
                        "ocrConfidence":[
                         0.919,0.79
                        ],
						"boundingBox":[
                        417,594,877,594,877,663,417,663
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"chk_time_inventory_conducted_startofbiz",
                        "value":"unselected",
                        "confidence":0.995,
						"positionConfidence":0.995,
                        "ocrConfidence":[
                         1
                        ],
						"boundingBox":[
                        545,1090,608,1090,608,1148,545,1148
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"phone_number",
                        "value":"634-142-1130",
                        "confidence":0.994,
						"positionConfidence":0.994,
                        "ocrConfidence":[
                         0.966
                        ],
						"boundingBox":[
                        1645,685,1990,685,1990,737,1645,737
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"inventory_conducted_date",
                        "value":"12-18-321",
                        "confidence":0.773,
						"positionConfidence":0.773,
                        "ocrConfidence":[
                         0.745
                        ],
						"boundingBox":[
                        1698,609,2029,609,2029,668,1698,668
                        ],
                        "source":"form recognizer"
						
					}
				]
			],
			[
				[
					{
						"key":"inventory_conducted_date",
                        "value":"null",
                        "confidence":0,
						"source":"form recognizer parsed"
						
					}
				]
			],
			[
				[
					{
						"key":"ReasonforInventory",
                        "value":"ChangeinPIC",
                        "probability":0.43,
						"boundingBox":[
                        1625,648,2026,648,2026,768,1626,768
                        ],
						"source":"custom vision"
						
					},
					{
						"key":"Signature",
						"value":"Detected",
						"probability":0.96,
						"boundingbox":[438,2424,1117,2424,1117,2593,438,2593],
						"souce":"custom vision"
					}
				]
			],
			],
			"ocrText":[],
			"tables":{}
		}
		]
}

kv_pairs = data['pages'][0]['keyValuePairs']

field_extractor={}
str_1=None

for el in kv_pairs:
    for idx in el:
        for i in idx:
            
            #Check if Pharmacy Number is present
            
            if(i['key']=="pharmacy_store_no"):
                
                header = i['key']
                field_extractor[header]=list()
                
                val = i['value']
                field_extractor[header].append(val)
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            # Date Conducted 
            
            if(i['key']=="inventory_conducted_date" and i['source']=='form recognizer'):
                
                header = i['key']
                field_extractor[header]=list()
                
                val = i['value']
                
                field_extractor[header].append(val)
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            #Address
            if(i['key']=='pharmacy_address_line1'):
                
                header='address'
                field_extractor[header]=list()
                
                val = i['value']
                
                field_extractor[header].append(val)
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            #Phone Number
            
            if(i['key']=='phone_number'):
                
                header = i['key']
                
                field_extractor[header]=list()
                
                val = i['value']
                
                field_extractor[header].append(val)
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            #City State Zip
            if(i['key']=="pharmacy_address_cityzipcode"):
               
               header = i['key']
               
               
               str_1 = i['value']
               split_str= str_1.split(",")
               
               
               if(len(i['ocrConfidence']) == len(split_str)):
                   
                   #Check for City
                   
                   field_extractor['city']=list()
                   field_extractor['city'].append(split_str[0])
                   field_extractor['city'].append(i['ocrConfidence'][0])
                   
                   compliance=None
                   
                   if(i['ocrConfidence'][0] >=0.8):
                       compliance='Y'
                   else:
                       compliance='I'
                   
                   field_extractor['city'].append(compliance)
                   
                   
                   #Check for State
                   
                   field_extractor['state']=list()
                   field_extractor['state'].append(split_str[1])
                   field_extractor['state'].append(i['ocrConfidence'][1])
                   
                   compliance=None
                   
                   if(i['ocrConfidence'][1] >=0.8):
                       compliance='Y'
                   else:
                       compliance='I'
                   
                   field_extractor['state'].append(compliance)
                   
                   #Check for Zip
                   
                   field_extractor['zip']=list()
                   field_extractor['zip'].append(split_str[2])
                   field_extractor['zip'].append(i['ocrConfidence'][1])
                   
                   compliance=None
                   
                   if(i['ocrConfidence'][2] >=0.8):
                       compliance='Y'
                   else:
                       compliance='I'
                   
                   field_extractor['zip'].append(compliance)
            
            #Pharmacy Number
            if(i['key']=='pharmacy_no'):
                 
                header = i['key']
                
                field_extractor[header]=list()
                
                val = i['value']
                
                field_extractor[header].append(val)
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            #Inventory Date Conducted
            
            if(i['key']=="inventory_conducted_date" and i['source']=='form recognizer'):
                
                header = i['key']
                field_extractor[header]=list()
                
                val = i['value']
                
                field_extractor[header].append(val)
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
                
            #Check Inventory Conducted
            
            # 1 Inventory conducted at Close
            if(i['key']=="chk_time_inventory_conducted_close"):
                
                header = i['key']
                field_extractor[header]=list()
                
                val = i['value']
                field_extractor[header].append(val)
                
                if(val=='selected'):
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
                else:
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
            
            #2 Inventory conducted at Start of business
            if(i['key']=="chk_time_inventory_conducted_startofbiz"):
               
               header=i['key']
               field_extractor[header]=list()
               
               val = i['value']
               field_extractor[header].append(val)
               
               if(val=='selected'):
                   field_extractor[header].append(i['confidence'])
                   field_extractor[header].append('')
               else:
                   field_extractor[header].append(i['confidence'])
                   field_extractor[header].append('')
            
            #3 Inventory conducted 24 Hour Pharmacy
            if(i['key']=="chk_time_inventory_conducted_24-hour"):
               
               
               header=i['key']
               field_extractor[header]=list()
               
               val = i['value']
               field_extractor[header].append(val)
               
               if(val=='selected'):
                   field_extractor[header].append(i['confidence'])
                   field_extractor[header].append('')
               else:
                   field_extractor[header].append(i['confidence'])
                   field_extractor[header].append('')
            
            #Reason for Inventory
            
            #1 Change of pharmacy in charge
            
            if(i['key']=="chk_reasonforinventory_changeofpic"):
               
               
               header = i['key']
               field_extractor[header]=list()
                
               val = i['value']
               field_extractor[header].append(val)
               
               if(val=='selected'):
                   field_extractor[header].append(i['confidence'])
                   field_extractor[header].append('')
               else:
                   field_extractor[header].append(i['confidence'])
                   field_extractor[header].append('')
                   
            #2 Ownership change
            
            if(i['key']=="chk_reasonforinventory_ownershipchange"):
                
                header = i['key']
                field_extractor[header]=list()
                 
                val = i['value']
                field_extractor[header].append(val)
                
                if(val=='selected'):
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
                else:
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
            
            # 3 Pharmacy closing
            if(i['key']=="chk_reasonforinventory_pharmacyclosing"):
                
                header = i['key']
                field_extractor[header]=list()
                 
                val = i['value']
                field_extractor[header].append(val)
                
                if(val=='selected'):
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
                else:
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
            
            # 4 Annual inventory for renewal
            if(i['key']=="chk_reasonforinventory_annualinventory"):
                
                header = i['key']
                field_extractor[header]=list()
                 
                val = i['value']
                field_extractor[header].append(val)
                
                if(val=='selected'):
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
                else:
                    field_extractor[header].append(i['confidence'])
                    field_extractor[header].append('')
            
            #Signature
            if(i['key']=="Signature"):
                
                header = i['key']
                field_extractor[header]=list()
                
                val = i['value']
                field_extractor[header].append(val)
                
            
            
            #effective_date
            if(i['key']=="effective_date"):
                
                header = i['key']
                field_extractor[header]=list()
                val = i['value']
                
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            #outgoing pic
            if(i['key']=='outgoing_pic'):
                
                header = i['key']
                field_extractor[header]=list()
                val = i['value']
                
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            #incoming pic
            if(i['key']=='incoming_pic'):
                
                header = i['key']
                field_extractor[header]=list()
                val = i['value']
                
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
            #Does_this_employment_at_this_location_for_outgoing_pic
            if(i['key']=='Does_this_employment_at_this_location_for_outgoing_pic'):
                
                header = i['key']
                field_extractor[header]=list()
                val = i['value']
                
                field_extractor[header].append(i['ocrConfidence'][0])
                
                compliance=None
                
                if(i['ocrConfidence'][0] >=0.8):
                    compliance='Y'
                else:
                    compliance='I'
                
                field_extractor[header].append(compliance)
            
                
#print(field_extractor)           


output_section={}

inventory_when_conducted={'selected':0,'unselected':0}



reason_for_inventory={'selected':0,'unselected':0}

city_state_zip=[]

for i in field_extractor:
    
    #Pharmacy Store Number
    if(i=='pharmacy_store_no'):
        
        output_section[i]=field_extractor[i][2]
        
        
    
    if(i=='inventory_conducted_date'):
        
        output_section[i]=field_extractor[i][2]
        
       
    
    if(i=='address'):
        
        output_section[i]=field_extractor[i][2]
        
       
    
    if(i=='phone_number'):
        
        output_section[i]=field_extractor[i][2]
        
        
    
    if(i=='pharmacy_no'):
        output_section[i]=field_extractor[i][2]
        
   
    
    if(i=='city'):
       
        city_state_zip.append(field_extractor[i][2])
        
    
    if(i=='state'):
        city_state_zip.append(field_extractor[i][2])
    
    if(i=='zip'):
        city_state_zip.append(field_extractor[i][2])
    
    """
     Inventory When Conducted
    
    """
    
    #Closed
    if(i=='chk_time_inventory_conducted_close'):
       
       if(field_extractor[i][0]=='selected'):
           inventory_when_conducted['selected']=inventory_when_conducted['selected']+1
           
           inventory_when_conducted[i]=field_extractor[i][1]
       
       if(field_extractor[i][0]=='unselected'):
           inventory_when_conducted['unselected']=inventory_when_conducted['unselected']+1
    
    #Start Of Business
    if(i=='chk_time_inventory_conducted_startofbiz'):
        
        if(field_extractor[i][0]=='selected'):
            inventory_when_conducted['selected']=inventory_when_conducted['selected']+1
            
            inventory_when_conducted[i]=field_extractor[i][1]
        
        if(field_extractor[i][0]=='unselected'):
            inventory_when_conducted['unselected']=inventory_when_conducted['unselected']+1
    
    #24 -Hour
    if(i=='chk_time_inventory_conducted_24-hour'):
        if(field_extractor[i][0]=='selected'):
            inventory_when_conducted['selected']=inventory_when_conducted['selected']+1
            
            inventory_when_conducted[i]=field_extractor[i][1]
        
        if(field_extractor[i][0]=='unselected'):
            inventory_when_conducted['unselected']=inventory_when_conducted['unselected']+1
    
    """
    Reason for Inventory 
    """
    
    #Change of Pharmacist in Charge
    if(i=='chk_reasonforinventory_changeofpic'):
        
        if(field_extractor[i][0]=='selected'):
            reason_for_inventory['selected']=reason_for_inventory['selected']+1
            
            reason_for_inventory[i]=field_extractor[i][1]
        
        if(field_extractor[i][0]=='unselected'):
           reason_for_inventory['unselected']=reason_for_inventory['unselected']+1
    
    
    #Ownership Change
    if(i=='chk_reasonforinventory_ownershipchange'):
        
        if(field_extractor[i][0]=='selected'):
            reason_for_inventory['selected']=reason_for_inventory['selected']+1
            
            reason_for_inventory[i]=field_extractor[i][1]
        
        if(field_extractor[i][0]=='unselected'):
            reason_for_inventory['unselected']=reason_for_inventory['unselected']+1
    
    #Pharmacy Closing
    if(i=='chk_reasonforinventory_pharmacyclosing'):
        
        if(field_extractor[i][0]=='selected'):
            reason_for_inventory['selected']=reason_for_inventory['selected']+1
            
            reason_for_inventory[i]=field_extractor[i][1]
        
        if(field_extractor[i][0]=='unselected'):
            reason_for_inventory['unselected']=reason_for_inventory['unselected']+1
    
    #Annual Inventory
    if(i=='chk_reasonforinventory_annualinventory'):
       
       if(field_extractor[i][0]=='selected'):
           reason_for_inventory['selected']=reason_for_inventory['selected']+1
           
           reason_for_inventory[i]=field_extractor[i][1]
       
       if(field_extractor[i][0]=='unselected'):
           reason_for_inventory['unselected']=reason_for_inventory['unselected']+1
    
    #Signature
      
    if(i=='Signature'):
        if(field_extractor[i][0]=='Detected'):
            output_section['SignatureOfRph']='Y'
        else:
            output_section['SignatureOfRph']='N'
    
    
   
        
    
        
    
        
        
#Checks for individual City State Zip, confidence score for each
def determine_csz(c_s_z):
    
    res=None
    
    if(len(c_s_z)==3):
        for i in c_s_z:
            
            if(i=='Y'):
                res='Y'            
            elif(i!='Y'):
                res='I'
                break
            else:
                res='I'
    
    return res
        
    
def determine_inventory_conducted(i_w_c):
    
    res_iwc=None
    
    if(i_w_c['selected']>1):
        res_iwc='N'
    elif(i_w_c['selected']==1):
        res_iwc='Y'
    else:
        res_iwc='N'
    
    if(res_iwc=='Y'):
        for i in i_w_c:
            if(i!='selected' and i!='unselected'):
                if(i_w_c[i]>=0.8):
                    return 'Y'
                else:
                    return 'I'
    else:
        return res_iwc
    

def determin_reason_for_inventory(r_f_i):
    
    res_rfi= None
    
    if(r_f_i['selected']>1):
        res_rfi='N'
    elif(r_f_i['selected']==1):
        res_rfi='Y'
    else:
        res_rfi='N'
    
    if(res_rfi=='Y'):
        for i in r_f_i:
            if(i!='selected' and i!='unselected'):
                if(r_f_i[i]>=0.8):
                    return 'Y'
                else:
                    return 'I'
    else:
        return res_rfi
    
    
    

#def check_change_PIC_section(data):
def check_change_PIC_section(data):
    
    if(('incoming_pic' not in data) and ('outgoing_pic' not in data)):
        
        return 'N'
    
    elif('outgoing_pic' in data):
        
        if(data['outgoing_pic'][2]=='Y'):
            
            if('does_this_employment_at_this_location_for_outgoing_pic' in data):
                
                if(data['does_this_employment_at_this_location_for_outgoing_pic'][0]=='selected'):
                    
                    #print('send this as YESS')
                    #print(data['does_this_employment_at_this_location_for_outgoing_pic'])
                    if(data['does_this_employment_at_this_location_for_outgoing_pic'][1]<0.8):
                        #print('Send I')
                        return 'I'
                    
                    if(data['does_this_employment_at_this_location_for_outgoing_pic'][1]>0.8):
                        #print('say Ayye')
                        return 'Y'
                
                if(data['does_this_employment_at_this_location_for_outgoing_pic'][0]!='selected'):
                    print('Send this as NOo')
                    return 'N'
        
        else:
            return 'N'
    
    elif('incoming_pic' in data):
        
        if(data['incoming_pic'][2]=='Y'):
            return 'Y'
        else:
            return 'N'
    
    else:
        return 'N'
        
    
    
        
    
    

    


    
    


output_section['city_state_zip']=determine_csz(city_state_zip)        

output_section['Inventory_When_Conducted']=determine_inventory_conducted(inventory_when_conducted)         

output_section['Reason_For_Inventory']=determin_reason_for_inventory(reason_for_inventory)


InvReasonCompliant=None

for i in reason_for_inventory:
    if(i=='chk_reasonforinventory_changeofpic'):
       
        if('effective_date' not in field_extractor):
            
            InvReasonCompliant='N'
            continue
        if(field_extractor['effective_date']):
            a = check_change_PIC_section(field_extractor)
            InvReasonCompliant = a
            
            #print(InvReasonCompliant)
        

#print(InvReasonCompliant)        
if(InvReasonCompliant != 'None'):
    output_section['InvReasonCompliant']=InvReasonCompliant



#print(reason_for_inventory)

#for i in reason_for_inventory:
#    if(i=='chk_reasonforinventory_changeofpic'):
#        check_change_PIC_section(field_extractor)

        

   # if(i=='state'):
        
#print(reason_for_inventory)

#print(inventory_when_conducted)

print(output_section)

        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            



