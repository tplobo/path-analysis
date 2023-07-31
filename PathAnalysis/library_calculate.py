import os
from collections import OrderedDict

def init(context):
    ExtAPI.Log.WriteMessage("Initialize Linearized Results calculation library...")

# Define solution file path
def build_fullpath():
    filename = "linearized_data.CSV"
    desktoppath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    #folderpath = r"C:\Users\ea5322\Desktop"
    fullpath = os.path.join(desktoppath,filename)
    return fullpath
print('Solution file path function defined!')
    
# Define stress solution extraction
def extract_stress_solution(lin_eq_stress_object):
    output = OrderedDict()
    output['Membrane'] = lin_eq_stress_object.Membrane.Value
    output['Bending-Inside'] = lin_eq_stress_object.BendingInside.Value
    output['Bending-Outside'] = lin_eq_stress_object.BendingOutside.Value
    output['Membrane+Bending-Inside'] = lin_eq_stress_object.MembraneBendingInside.Value
    output['Membrane+Bending-Center'] = lin_eq_stress_object.MembraneBendingCenter.Value
    output['Membrane+Bending-Outside'] = lin_eq_stress_object.MembraneBendingOutside.Value
    output['Peak-Inside'] = lin_eq_stress_object.PeakInside.Value
    output['Peak-Center'] = lin_eq_stress_object.PeakCenter.Value
    output['Peak-Outside'] = lin_eq_stress_object.PeakOutside.Value
    output['Total-Inside'] = lin_eq_stress_object.TotalInside.Value
    output['Total-Center'] = lin_eq_stress_object.TotalCenter.Value
    output['Total-Outside'] = lin_eq_stress_object.TotalOutside.Value
    return output
print('Stress solution extraction function defined!')

# Define temperature solution extraction
def extract_temperature_solution(lin_temp_object):
    output = OrderedDict()
    output['Minimum Temp'] = lin_temp_object.Minimum.Value
    output['Maximum Temp'] = lin_temp_object.Maximum.Value
    output['Average Temp'] = lin_temp_object.Average.Value
    return output
print('Temperature solution extraction function defined!')

# Retrieve all paths from model
def retrieve_path_objects():
    all_path_objects = DataModel.GetObjectsByType(DataModelObjectCategory.Path)
    all_path_names = []
    for path_object in all_path_objects:
        path_name = path_object.Name
        all_path_names.append(path_name)
    return all_path_names
print('Model paths retrieval function defined!')

# Solve individual path
def solve_path(path_name):
    
    #Select Relevant Solution (Static Structural)
    mySol = DataModel.AnalysisList[1].Solution
    mypath = DataModel.GetObjectsByName(path_name)[0]
    
    # Get Stress on path
    linearized_equivalent_stress = mySol.AddLinearizedEquivalentStress()
    linearized_equivalent_stress.Location = mypath
    linearized_equivalent_stress.EvaluateAllResults()
    linearized_equivalent_stress.Name = 'Linearized Equivalent Stress ' + path_name
    
    # Get Temp on path
    linearized_temp = mySol.AddUserDefinedResult()
    linearized_temp.Expression = r'BFE'
    linearized_temp.Location = mypath
    linearized_temp.EvaluateAllResults()
    linearized_temp.Name = 'Temperature ' + path_name

    # Create output
    lin_eq_stress_object = linearized_equivalent_stress
    lin_temp_object = linearized_temp
    return lin_eq_stress_object, lin_temp_object
print('Path solving function defined!')

# Merge dictionaries
def merge_two_dicts(x, y):
    z = x.copy()
    for (key,value) in y.items():
        z[key] = value
    return z
print('Dictionary merging function defined!')

# Calculate and export all paths
def calculate_and_export(analysis):

    # Specify unit
    ExtAPI.Application.ActiveUnitSystem = MechanicalUnitSystem.StandardNMM
    
    # Build paths
    all_path_names = retrieve_path_objects()
    print('All path names retrieved!')
    
    # Build dictionary of solutions
    all_solutions = OrderedDict()
    for path_name in all_path_names:
        
        # Compute Stress and Temperature Objects
        lin_eq_stress_object, lin_temp_object = solve_path(path_name)
        
        # Extract solutions
        output_stress = extract_stress_solution(lin_eq_stress_object)
        output_temperature = extract_temperature_solution(lin_temp_object)
        
        # Merge outputs
        output =merge_two_dicts(output_stress, output_temperature)
        
        # Store solution
        all_solutions[path_name] = output
    print('All solutions retrieved!')
    
    # Export solution to file
    with open(build_fullpath(), 'w') as f:
        
        # Print headers in file
        first_key = next(iter(all_solutions)) 
        first_solution = all_solutions[first_key]
        all_keys = []
        for key in first_solution.keys():
            all_keys.append(key)
        str_values = ', '.join(all_keys)
        f.write('PATH, '+ str_values + '\n')
    
        # Print solutions in file
        for (path,solution) in all_solutions.items():
            all_values = []
            for (key,value) in solution.items():
                all_values.append(str(value))
            str_values = ', '.join(all_values)
            f.write(path + ', '+ str_values + '\n')
    print('All solutions exported!')
