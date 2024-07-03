#function to convert cm to mm
def cm_to_mm(cm_val):
    mm = cm_val * 10
    return mm
    
#START
print("One Calculator to Calculate Them All!\n")

#ask for user input
ring_diameter = float(input("Diameter of a ring (in cm)?"))
height = float(input(" Height of a ring (in mm)?"))

#calculate and output volume of the ring without cutout
cm_val = 1/2*ring_diameter

def vwo(height):
    volume_wo_co = cm_to_mm(cm_val)**2 * height * 3.14
    return volume_wo_co
  
print(f' Volume of a ring without the inner cutout is: ' + str(vwo(height)) + ' mm^3')

#ask for user input for the ratio of the inner cutout
ratio_inner_diameter = float(input("Ratio of the inner cutout diameter (as a decimal)?"))

#calculate and output volume of inner cutout and ring
inner_dia = ratio_inner_diameter * cm_to_mm(cm_val)

def vi(inner_dia, height):
    volume_inner = 3.14 * (inner_dia**2) * height
    return volume_inner
    
print(f' Volume of the inner cutout is: ' + str(round(vi(inner_dia, height),2)) + ' mm^3')

#calculate and output volume of ring
volume = vwo(height) - vi(inner_dia, height)

print(f'Volume of a ring with the inner cutout is: ' + str(round(volume,2)) + ' mm^3\n')

#start rings of power
print("***Rings of Power***\n")

#ask user for input
rings = int(input("Number of rings?"))
material_cost = int(input(" Cost of the material (in cents per cubic inch)?"))
forging_cost = int(input(" Forging cost (in cents per ring)?"))

#calculate and output the total amount of material needed 

def amount(rings, volume):
	amount = rings * volume
	return amount

print(f' Total material needed is: ' + str(round(amount(rings, volume), 2)) + ' mm^3')

#calculate and output the total # of cubes

def total_cubes():
	cubes = amount(rings, volume) / 25.4 ** 3
	rounded_cubes = int(cubes+1)-int(int(cubes+1)-cubes)
	return rounded_cubes
	
print(f'Total number of cubes to purchase is: ' + str(total_cubes()) + ' cube(s)')
	
#calculate and output the total cost of Rings of Power

def total_cost(material_cost, rings, forging_cost):
    cost = (material_cost * total_cubes()) + (rings * forging_cost)
    return cost

def d():
    dollars = total_cost(material_cost, rings, forging_cost) // 100
    return dollars
    
def c():
    cents = total_cost(material_cost, rings, forging_cost) % 100
    return cents
    
print(f'Cost for the Rings of Power is: '+str(d())+' dollar(s) and '+str(c())+' cent(s)!\n')

#start of the One Ring calculations
print("***The One Ring***\n")

#user input for one ring calculations
onering_material = int(input("Cost of the material (in cents per cubic inch)? "))

#calculate and output number of cubes to purchase for one ring

def cubes_one(volume):
	onering_cubes = volume / 25.4 ** 3
	rounded_onering_cubes = int(onering_cubes+1) - int(int(onering_cubes+1)-onering_cubes)
	return rounded_onering_cubes

print(f'Number of cubes to purchase is: ' + str(cubes_one(volume)) + ' cube(s)')

#calculate and output the total cost for one ring

def total_onering(onering_material,forging_cost):
    one_cost = (onering_material * cubes_one(volume)) + (3 * forging_cost)
    return one_cost

def d_o():
    dollars_one = total_onering(onering_material, forging_cost) // 100
    return dollars_one
    
def ct_o():
    cents_one = total_onering(onering_material, forging_cost) % 100
    return cents_one

print(f'Cost for the One Ring is: '+str(d_o())+' dollar(s) and '+str(ct_o())+' cent(s)!\n')

#conclude

print("This Shall Not Fail!")