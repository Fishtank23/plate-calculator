# Hevy plate calculator function
import math 

#Create dictionary with common equipment and weights to select from
avail_equip = {
    'barbell': 45,
    'hex bar': 55,
    'trap bar': 55,
    'curl bar': 27
}

def equip_list(equipment):
    """User enters equipment and it's checked if it is in list
    user has opportunity to add it to list with weight of equipment"""
    if equipment not in avail_equip.keys():
     print(f"Check avail_equip dictionary, equipment: {equipment} not found")
     add_eq_wt_prompt = input(f"\n How much does {equipment} weigh in pounds? ")
     add_eq_wt_prompt = int(add_eq_wt_prompt)
     avail_equip[equipment] = add_eq_wt_prompt
#equip_list(equipment = 'bar')

#List of possible weights to select that I have available
possible_weights = [2.5, 5, 10, 25, 35, 45]
#sort largest to smallest
possible_weights.sort(reverse=True)

def plate_calculator():
    """User enters equipment used. Only one should be selected.
        User enters total weight for the exercise"""
    equipment = input(f"\n What equipment are you using? ")
    total_weight = int(input(f"\n What is the total weight in pounds for the exercise? "))
    if equipment not in avail_equip.keys():
        equip_list(equipment=equipment)
        bar_wt = avail_equip[equipment]
    else:
        bar_wt = avail_equip[equipment]
    weight = total_weight - bar_wt
    weight_side = math.floor(weight/2)
    if weight_side < 0:
         print(f"\n Equipment: {equipment} weighs more than total desired weight: {total_weight}. \n\tCheck total weight.")
         return
    if weight_side == 0:
        print(f"No plates required, total weight and equipment weight match")
        return
    print(f"\nload weight for one side: {weight_side} pounds") 
    remain_weight = weight_side
    total_plates = []
    while remain_weight >= 2.5:
            for ws in possible_weights:
                if ws <= remain_weight:
                    #print(f"{ws} less than {weight_side}")
                    plates = ws
                    total_plates.append(plates)
                    remain_weight = remain_weight - plates
                    print(f"\tRemaining weight for plates: {remain_weight} pounds")
                    
                    break
    if remain_weight > 0 and remain_weight < 2.5:
            actual = total_weight - remain_weight
            print(f"\nNo plates available less than 2.5 pounds \nActual weight: {actual} pounds")
    print(f"\tTotal Plates to load: {total_plates} for {total_weight} pounds")    
plate_calculator()


