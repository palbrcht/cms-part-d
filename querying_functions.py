import pandas
import requests


class cms_query(object):

        ###
        ###  Example use:  fetch_provider('Smith' , 'John')
        ###
        ###  Last name is required.
        ###  First name is optional.
        ###

    def fetch_provider(provider_last_name, provider_first_name = None):
        cms_domain = 'https://data.cms.gov/data-api/v1/dataset/5a27f7a8-c7af-434f-a26c-54db03e22cd1/data?'
        if provider_first_name == None:
            api_filter_last_name = ('&filter[Prscrbr_Last_Org_Name]=' + provider_last_name)
            query_string = (cms_domain + api_filter_last_name )
        if provider_first_name != None:
            api_filter_last_name = ('&filter[Prscrbr_Last_Org_Name]=' + provider_last_name)
            api_filter_first_name = ('&filter[Prscrbr_First_Name]=' + provider_first_name)
            query_string = (cms_domain + api_filter_last_name + api_filter_first_name)
        api_request = requests.get(query_string)
        json_data = api_request.json()
        placeholder_df = pandas.DataFrame.from_dict(json_data)
        print(placeholder_df)
        return(placeholder_df)

    ###
    ### Example:  fetch_state('TN')
    ###
    def fetch_state(state_abbreviation):
        cms_domain = 'https://data.cms.gov/data-api/v1/dataset/5a27f7a8-c7af-434f-a26c-54db03e22cd1/data?'
        api_filter_last_name = ('&filter[Prscrbr_State_Abrvtn]=' + state_abbreviation)
        query_string = (cms_domain + api_filter_last_name )

        api_request = requests.get(query_string)
        json_data = api_request.json()
        placeholder_df = pandas.DataFrame.from_dict(json_data)
        print(placeholder_df)
        return(placeholder_df)

    ###
    ### Example: fetch_city('Memphis' , 'TN')
    ###
    def fetch_city(city_name, state_abbreviation):
        cms_domain = 'https://data.cms.gov/data-api/v1/dataset/5a27f7a8-c7af-434f-a26c-54db03e22cd1/data?'
        api_filter_last_name = ('&filter[Prscrbr_State_Abrvtn]=' + state_abbreviation + '&filter[Prscrbr_City]=' + city_name)
        query_string = (cms_domain + api_filter_last_name )
        api_request = requests.get(query_string)
        json_data = api_request.json()
        placeholder_df = pandas.DataFrame.from_dict(json_data)
        print(placeholder_df)
        return(placeholder_df)

    ###
    ###  TODO
    ###
    ### 1. Add component for BOTH claims and cost
    ### 2. Probably need a way to tidy up the if logic
    ###

    def fetch_generic_drug(generic_drug_name, claims_count = None , claims_indication = None , total_cost = None, cost_indication = None):
        cms_domain = 'https://data.cms.gov/data-api/v1/dataset/5a27f7a8-c7af-434f-a26c-54db03e22cd1/data?'

        if claims_count == None and total_cost == None:
            api_filter = ('&filter[Gnrc_Name]=' + generic_drug_name)
            query_string = (cms_domain + api_filter)
        if claims_count != None and total_cost == None:
            if claims_indication == 'greater':
                api_filter = ('&filter[Gnrc_Name]=' + generic_drug_name + '&filter[name-filter][condition][path]=Tot_Clms&filter[name-filter][condition][operator]=>&filter[name-filter][condition][value][1]=' + str(claims_count))
                query_string = (cms_domain + api_filter)
                print(query_string)
            if claims_indication == 'lesser':
                api_filter = ('&filter[Gnrc_Name]=' + generic_drug_name + '&filter[name-filter][condition][path]=Tot_Clms&filter[name-filter][condition][operator]=<&filter[name-filter][condition][value][1]=' + str(claims_count))
                query_string = (cms_domain + api_filter)
        if claims_count == None and total_cost != None:
            if cost_indication == 'greater':
                api_filter = ('&filter[Gnrc_Name]=' + generic_drug_name + '&filter[name-filter][condition][path]=Tot_Drug_Cst&filter[name-filter][condition][operator]=>&filter[name-filter][condition][value][1]=' + str(total_cost))
                query_string = (cms_domain + api_filter)
                print(query_string)
            if cost_indication == 'lesser':
                api_filter = ('&filter[Gnrc_Name]=' + generic_drug_name + '&filter[name-filter][condition][path]=Tot_Drug_Cst&filter[name-filter][condition][operator]=<&filter[name-filter][condition][value][1]=' + str(total_cost))
                query_string = (cms_domain + api_filter)
                print(query_string)

        ##if claims_count != None and total_cost != None:

        api_request = requests.get(query_string)
        json_data = api_request.json()
        placeholder_df = pandas.DataFrame.from_dict(json_data)
        print(placeholder_df)
        #placeholder_df.to_csv('part_d_data_export.csv', header=True, index=False)
        return(placeholder_df)

### Examples: 
### 
### fetch_generic_drug('Oxycodone Hcl')
### 
### fetch_generic_drug('Oxycodone Hcl')
### fetch_generic_drug(generic_drug_name = 'Atorvastatin Calcium' , claims_count = 1500 , claims_indication = 'greater')
### fetch_generic_drug(generic_drug_name = 'Atorvastatin Calcium' , total_cost = 50000 , cost_indication = 'greater')

