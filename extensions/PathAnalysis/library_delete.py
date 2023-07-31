def init(context):
    ExtAPI.Log.WriteMessage("Initialize Linearized Results deletion library...")

# Validate list of results
def validate_results_list(results_list):
    if results_list:
        return results_list
    else:
        return []

# Retrieve all stress results
def retrieve_stress_results():
    all_stress_results = DataModel.GetObjectsByType(DataModelObjectCategory.LinearizedStressResult)
    return validate_results_list(all_stress_results)

# Retrieve all user results
def retrieve_user_results():
    all_user_results = DataModel.GetObjectsByType(DataModelObjectCategory.UserDefinedResult)
    return validate_results_list(all_user_results)

# Filter results list by expression
def filter_results_list(results_list,expression):
    if len(results_list) != 0:
        all_filtered_results = []
        for result in results_list:
            if result.Expression == expression:
                all_filtered_results.append(result)
        return all_filtered_results

# Delete all results in list
def delete_results_in_list(results_list):
    if len(results_list) != 0:
        for result in results_list:
            result.Delete()

# Delete all stress results
def delete_stress_results(analysis):
    all_stress_results = retrieve_stress_results()
    delete_results_in_list(all_stress_results)
        
# Delete all user results
def delete_user_results(analysis):
    all_user_results = retrieve_user_results(analysis)
    delete_results_in_list(all_user_results)

# Delete all temperature results
def delete_temperature_results(analysis):
    #ExtAPI.Log.WriteMessage("Test 1")
    all_user_results = retrieve_user_results()
    all_temperature_results = filter_results_list(all_user_results,'BFE')
    delete_results_in_list(all_temperature_results)

# Delete all results
def delete_all_results(analysis):
    delete_stress_results(analysis)
    delete_user_results(analysis)
    delete_temperature_results(analysis)
