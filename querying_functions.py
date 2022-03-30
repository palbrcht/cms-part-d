import pandas
import requests

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
###  Last name is required.
###  First name is optional.
###
###  Example use:
###

fetch_provider('INSERT_LAST_NAME' , 'INSERT_FIRST_NAME')
